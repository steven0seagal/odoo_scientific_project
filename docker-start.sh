#!/bin/bash

# Scientific Project Manager - Docker Quick Start Script
# This script provides a fast way to build and run the containerized environment

set -e  # Exit on error

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ODOO_DIR="$SCRIPT_DIR/odoo"
DOCS_DIR="$SCRIPT_DIR/docs"

# Function to print colored messages
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to display usage
show_usage() {
    cat << EOF
Usage: $0 [COMMAND] [OPTIONS]

Commands:
    odoo                Build and start Odoo container
    docs                Build and start documentation container
    all                 Build and start all containers (default)
    stop                Stop all running containers
    restart             Restart all containers
    clean               Stop and remove all containers, networks, and volumes
    logs [SERVICE]      Show logs for specified service (odoo/docs/all)
    status              Show status of all containers

Options:
    -d, --detach        Run containers in detached mode (background)
    -b, --build         Force rebuild images before starting
    -h, --help          Show this help message

Examples:
    $0 all              Start all services
    $0 odoo -d          Start Odoo in background
    $0 docs --build     Rebuild and start docs
    $0 logs odoo        Show Odoo logs
    $0 clean            Clean up all containers

EOF
}

# Function to check if Docker is running
check_docker() {
    if ! docker info > /dev/null 2>&1; then
        print_error "Docker is not running or not installed"
        print_info "Please start Docker and try again"
        exit 1
    fi
    print_success "Docker is running"
}

# Function to create .env file if it doesn't exist
create_env_file() {
    if [ ! -f "$ODOO_DIR/.env" ]; then
        print_warning ".env file not found in odoo directory"
        print_info "Creating default .env file..."
        cat > "$ODOO_DIR/.env" << 'ENVEOF'
# PostgreSQL Configuration
DB_USER=odoo
DB_PASSWORD=odoo
DB_NAME=postgres
DB_HOST=db
DB_PORT=5432
PGDATA=/var/lib/postgresql/data/pgdata
ENVEOF
        print_success "Created default .env file at $ODOO_DIR/.env"
        print_warning "Please review and update the configuration if needed"
    fi
}

# Function to start Odoo containers
start_odoo() {
    local BUILD_FLAG=""
    local DETACH_FLAG=""

    [ "$FORCE_BUILD" = true ] && BUILD_FLAG="--build"
    [ "$DETACH_MODE" = true ] && DETACH_FLAG="-d"

    print_info "Starting Odoo containers..."
    cd "$ODOO_DIR"
    create_env_file

    docker-compose up $BUILD_FLAG $DETACH_FLAG

    if [ "$DETACH_MODE" = true ]; then
        print_success "Odoo containers started in background"
        print_info "Access Odoo at: http://localhost:8069"
        print_info "View logs with: $0 logs odoo"
    fi
}

# Function to start documentation containers
start_docs() {
    local BUILD_FLAG=""
    local DETACH_FLAG=""

    [ "$FORCE_BUILD" = true ] && BUILD_FLAG="--build"
    [ "$DETACH_MODE" = true ] && DETACH_FLAG="-d"

    print_info "Starting documentation containers..."
    cd "$DOCS_DIR"

    docker-compose up $BUILD_FLAG $DETACH_FLAG

    if [ "$DETACH_MODE" = true ]; then
        print_success "Documentation containers started in background"
        print_info "Access documentation at: http://localhost:8000"
        print_info "View logs with: $0 logs docs"
    fi
}

# Function to start all containers
start_all() {
    print_info "Starting all containers..."

    # Start docs in background
    DETACH_MODE=true start_docs

    # Start Odoo with user's detach preference
    start_odoo

    if [ "$DETACH_MODE" = true ]; then
        print_success "All containers started successfully"
        echo ""
        print_info "Service URLs:"
        echo "  - Odoo:          http://localhost:8069"
        echo "  - Documentation: http://localhost:8000"
    fi
}

# Function to stop all containers
stop_all() {
    print_info "Stopping all containers..."

    cd "$ODOO_DIR"
    docker-compose down 2>/dev/null || true

    cd "$DOCS_DIR"
    docker-compose down 2>/dev/null || true

    print_success "All containers stopped"
}

# Function to restart all containers
restart_all() {
    print_info "Restarting all containers..."
    stop_all
    sleep 2
    start_all
}

# Function to clean up containers, volumes, and networks
clean_all() {
    print_warning "This will remove all containers, volumes, and networks"
    read -p "Are you sure? (y/N) " -n 1 -r
    echo

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        print_info "Cleaning up..."

        cd "$ODOO_DIR"
        docker-compose down -v 2>/dev/null || true

        cd "$DOCS_DIR"
        docker-compose down -v 2>/dev/null || true

        print_success "Cleanup completed"
    else
        print_info "Cleanup cancelled"
    fi
}

# Function to show logs
show_logs() {
    local SERVICE=$1

    case $SERVICE in
        odoo)
            print_info "Showing Odoo logs (Ctrl+C to exit)..."
            cd "$ODOO_DIR"
            docker-compose logs -f
            ;;
        docs)
            print_info "Showing documentation logs (Ctrl+C to exit)..."
            cd "$DOCS_DIR"
            docker-compose logs -f
            ;;
        all|"")
            print_info "Showing all logs (Ctrl+C to exit)..."
            (cd "$ODOO_DIR" && docker-compose logs -f) &
            (cd "$DOCS_DIR" && docker-compose logs -f) &
            wait
            ;;
        *)
            print_error "Unknown service: $SERVICE"
            print_info "Valid services: odoo, docs, all"
            exit 1
            ;;
    esac
}

# Function to show container status
show_status() {
    print_info "Container Status:"
    echo ""

    print_info "Odoo Containers:"
    cd "$ODOO_DIR"
    docker-compose ps

    echo ""
    print_info "Documentation Containers:"
    cd "$DOCS_DIR"
    docker-compose ps
}

# Main script logic
COMMAND=${1:-all}
FORCE_BUILD=false
DETACH_MODE=false

# Parse options
shift || true
while [ $# -gt 0 ]; do
    case $1 in
        -d|--detach)
            DETACH_MODE=true
            shift
            ;;
        -b|--build)
            FORCE_BUILD=true
            shift
            ;;
        -h|--help)
            show_usage
            exit 0
            ;;
        *)
            # Assume it's a service name for logs command
            if [ "$COMMAND" = "logs" ]; then
                SERVICE_NAME=$1
            fi
            shift
            ;;
    esac
done

# Check Docker is running
check_docker

# Execute command
case $COMMAND in
    odoo)
        start_odoo
        ;;
    docs)
        start_docs
        ;;
    all)
        start_all
        ;;
    stop)
        stop_all
        ;;
    restart)
        restart_all
        ;;
    clean)
        clean_all
        ;;
    logs)
        show_logs "${SERVICE_NAME:-all}"
        ;;
    status)
        show_status
        ;;
    -h|--help|help)
        show_usage
        ;;
    *)
        print_error "Unknown command: $COMMAND"
        echo ""
        show_usage
        exit 1
        ;;
esac

exit 0
