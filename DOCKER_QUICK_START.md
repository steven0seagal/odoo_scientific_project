# Docker Quick Start Guide

This guide provides quick instructions for building and running the Odoo Scientific Project containers.

## Prerequisites

- Docker installed and running
- Docker Compose installed (included with Docker Desktop)
- At least 4GB of free RAM
- Ports 8069 (Odoo) and 8000 (docs) available

## Quick Start

### One-Command Start

Start all services in the background:

```bash
./docker-start.sh all -d
```

Access the services:
- **Odoo**: http://localhost:8069
- **Documentation**: http://localhost:8000

### Step-by-Step Start

1. **Make the script executable** (first time only):
   ```bash
   chmod +x docker-start.sh
   ```

2. **Start the services**:
   ```bash
   # Start all services with output visible
   ./docker-start.sh all

   # OR start in background (detached mode)
   ./docker-start.sh all -d
   ```

3. **Check status**:
   ```bash
   ./docker-start.sh status
   ```

4. **View logs**:
   ```bash
   # View Odoo logs
   ./docker-start.sh logs odoo

   # View documentation logs
   ./docker-start.sh logs docs

   # View all logs
   ./docker-start.sh logs all
   ```

## Common Commands

### Starting Services

```bash
# Start everything
./docker-start.sh all

# Start only Odoo (database + web)
./docker-start.sh odoo

# Start only documentation
./docker-start.sh docs

# Start in background
./docker-start.sh all -d

# Force rebuild before starting
./docker-start.sh all --build
```

### Stopping Services

```bash
# Stop all containers
./docker-start.sh stop
```

### Restarting Services

```bash
# Restart all containers
./docker-start.sh restart
```

### Viewing Logs

```bash
# View logs for a specific service
./docker-start.sh logs odoo
./docker-start.sh logs docs

# View all logs
./docker-start.sh logs all
```

### Container Status

```bash
# Show status of all containers
./docker-start.sh status
```

### Cleanup

```bash
# Remove all containers, volumes, and networks
./docker-start.sh clean
```

**⚠️ Warning**: The `clean` command removes all data including the database!

## First Time Setup

When you run the script for the first time:

1. A default `.env` file is created in the `odoo/` directory
2. Docker images are pulled (this may take a few minutes)
3. Containers are created and started

### Default Configuration

The default `.env` file contains:

```env
DB_USER=odoo
DB_PASSWORD=odoo
DB_NAME=postgres
DB_HOST=db
DB_PORT=5432
PGDATA=/var/lib/postgresql/data/pgdata
```

**For production use**, update these values before starting:

```bash
nano odoo/.env
# Edit the values
./docker-start.sh all -d
```

## Service Details

### Odoo Service

- **URL**: http://localhost:8069
- **Components**:
  - PostgreSQL database (port 5432 internal)
  - Odoo web application (port 8069)
- **Volumes**:
  - `odoo/addons/` → `/mnt/extra-addons` (your custom modules)
  - `odoo/config/` → `/etc/odoo` (configuration files)
  - Database data (persistent volume)

### Documentation Service

- **URL**: http://localhost:8000
- **Technology**: MkDocs with Material theme
- **Features**:
  - Live reload during development
  - Full-text search
  - Mobile-responsive design
- **Volumes**:
  - `docs/docs/` → Documentation source (read-only)
  - `docs/mkdocs.yml` → Configuration (read-only)

## Troubleshooting

### Docker Not Running

**Error**: `Docker is not running or not installed`

**Solution**:
- Start Docker Desktop (macOS/Windows)
- Or start Docker daemon: `sudo systemctl start docker` (Linux)

### Port Already in Use

**Error**: `Bind for 0.0.0.0:8069 failed: port is already allocated`

**Solution**:
```bash
# Find what's using the port
sudo lsof -i :8069

# Kill the process or stop the service
# OR edit docker-compose.yml to use a different port
```

### Permission Denied

**Error**: `Permission denied` when running the script

**Solution**:
```bash
chmod +x docker-start.sh
```

### Containers Won't Start

**Solution 1** - Check logs:
```bash
./docker-start.sh logs odoo
```

**Solution 2** - Clean rebuild:
```bash
./docker-start.sh clean
./docker-start.sh all --build
```

### Database Connection Failed

**Solution**:
1. Ensure the database container is running:
   ```bash
   ./docker-start.sh status
   ```

2. Check database logs:
   ```bash
   cd odoo && docker-compose logs db
   ```

3. Verify `.env` file exists and has correct values

### Out of Memory

**Solution**:
- Increase Docker's memory allocation in Docker Desktop settings
- Recommended: At least 4GB RAM

## Advanced Usage

### Running Individual Services

Start only specific services using docker-compose directly:

```bash
# Start only database
cd odoo && docker-compose up db

# Start only Odoo web (requires db running)
cd odoo && docker-compose up web

# Start docs only
cd docs && docker-compose up
```

### Viewing Container Details

```bash
# List all project containers
docker ps --filter "name=scientific-project\|odoo"

# Inspect a specific container
docker inspect scientific-project-docs

# Execute commands in a container
docker exec -it scientific-project-docs /bin/bash
```

### Custom Configuration

#### Changing Ports

Edit `docker-compose.yml` files to modify port mappings:

**Odoo** (`odoo/docker-compose.yml`):
```yaml
ports:
  - "8069:8069"  # Change first number to use different host port
```

**Docs** (`docs/docker-compose.yml`):
```yaml
ports:
  - "8000:8000"  # Change first number to use different host port
```

#### Adding Environment Variables

Edit `odoo/.env` file to add custom environment variables:
```env
# Add your custom variables
CUSTOM_VAR=value
```

## Production Deployment

For production deployment:

1. **Update environment variables**:
   ```bash
   nano odoo/.env
   ```
   - Use strong passwords
   - Set secure database credentials

2. **Use specific image versions**:
   Edit `docker-compose.yml` to pin versions:
   ```yaml
   image: odoo:16.0  # Instead of odoo:16
   image: postgres:13.10  # Instead of postgres:13
   ```

3. **Configure reverse proxy**:
   - Set up nginx or traefik
   - Enable HTTPS with SSL certificates
   - See `docs/docker-compose.yml` for nginx example

4. **Set up backups**:
   ```bash
   # Backup database
   docker exec odoo_db pg_dump -U odoo odoo > backup.sql

   # Backup volumes
   docker run --rm -v odoo_web-data:/data -v $(pwd):/backup \
     ubuntu tar czf /backup/odoo-data.tar.gz /data
   ```

## Getting Help

```bash
# Show script help
./docker-start.sh --help

# Check Docker version
docker --version
docker-compose --version

# View all running containers
docker ps

# View all containers (including stopped)
docker ps -a
```

## Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Odoo Docker Documentation](https://hub.docker.com/_/odoo)
- [Project README](README.md)
- [Claude Configuration](.claude/README.md)
