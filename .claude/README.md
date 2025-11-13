# Claude Code Configuration

This directory contains Claude Code configuration and hooks for the Odoo Scientific Project.

## Session Start Hook

The `sessionStart` script automatically runs when a new Claude Code session begins. It:

- Checks Docker status
- Displays running container information
- Shows quick start commands
- Provides project structure overview
- Validates environment configuration

## Quick Start Commands

### Using docker-start.sh

The project includes a comprehensive Docker management script:

```bash
# Start all services
./docker-start.sh all

# Start all services in background
./docker-start.sh all -d

# Start only Odoo
./docker-start.sh odoo

# Start only documentation
./docker-start.sh docs

# Force rebuild and start
./docker-start.sh all --build

# Stop all containers
./docker-start.sh stop

# View logs
./docker-start.sh logs odoo
./docker-start.sh logs docs
./docker-start.sh logs all

# Show container status
./docker-start.sh status

# Restart all services
./docker-start.sh restart

# Clean up (removes containers, volumes, networks)
./docker-start.sh clean

# Show help
./docker-start.sh --help
```

## Project Structure

```
odoo_scientific_project/
├── .claude/                 # Claude Code configuration
│   ├── sessionStart        # Session initialization hook
│   └── README.md           # This file
├── odoo/                   # Odoo application
│   ├── docker-compose.yml  # Odoo container configuration
│   ├── .env               # Environment variables (created on first run)
│   ├── addons/            # Odoo addons/modules
│   └── config/            # Odoo configuration files
├── docs/                   # Documentation
│   ├── Dockerfile         # Documentation container image
│   ├── docker-compose.yml # Documentation container configuration
│   └── docs/              # MkDocs source files
├── docker-start.sh         # Quick start script
└── README.md              # Project documentation
```

## Access Points

When containers are running:

- **Odoo Application**: http://localhost:8069
- **Documentation**: http://localhost:8000

## Environment Configuration

The Odoo container requires a `.env` file in the `odoo/` directory. This file is automatically created with default values on first run:

```env
DB_USER=odoo
DB_PASSWORD=odoo
DB_NAME=postgres
DB_HOST=db
DB_PORT=5432
PGDATA=/var/lib/postgresql/data/pgdata
```

Update these values according to your requirements before starting in production.

## Development Workflow

1. **Start Development Environment**:
   ```bash
   ./docker-start.sh all -d
   ```

2. **View Logs During Development**:
   ```bash
   ./docker-start.sh logs odoo
   ```

3. **Restart After Configuration Changes**:
   ```bash
   ./docker-start.sh restart
   ```

4. **Stop When Done**:
   ```bash
   ./docker-start.sh stop
   ```

## Troubleshooting

### Docker Not Running
If you see "Docker is not running", start Docker Desktop or the Docker daemon.

### Port Conflicts
If ports 8069 (Odoo) or 8000 (docs) are already in use:
- Stop the conflicting service
- Or modify the port mappings in the respective `docker-compose.yml` files

### Container Issues
To fully clean up and start fresh:
```bash
./docker-start.sh clean
./docker-start.sh all --build
```

## Additional Resources

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Odoo Documentation](https://www.odoo.com/documentation)
- [MkDocs Documentation](https://www.mkdocs.org/)
