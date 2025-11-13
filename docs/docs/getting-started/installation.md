# Installation Guide

This guide will walk you through installing the Scientific Project Manager addon for Odoo 15.0.

## Prerequisites

Before installing, ensure you have the following:

- Odoo 15.0 or higher
- Python 3.7+
- PostgreSQL 10+
- Sufficient database permissions
- Access to Odoo addons directory

## Installation Methods

### Method 1: Standard Installation

#### Step 1: Clone the Repository

```bash
cd /path/to/odoo/addons
git clone https://github.com/steven0seagal/odoo_scientific_project.git
cd odoo_scientific_project
```

#### Step 2: Copy Module to Addons Directory

```bash
cp -r odoo/addons/scientific_project /path/to/odoo/addons/
```

#### Step 3: Update Addons List

1. Restart your Odoo server
2. Login as administrator
3. Navigate to **Apps** menu
4. Click **Update Apps List**
5. Confirm the update

#### Step 4: Install the Module

1. In the Apps menu, search for "Scientific Project Manager"
2. Click the **Install** button
3. Wait for installation to complete

### Method 2: Docker Installation

If you're using Docker, add the module to your custom addons directory.

#### Step 1: Update docker-compose.yml

```yaml
version: '3'
services:
  odoo:
    image: odoo:15.0
    depends_on:
      - db
    ports:
      - "8069:8069"
    volumes:
      - odoo-data:/var/lib/odoo
      - ./odoo/addons/scientific_project:/mnt/extra-addons/scientific_project
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo
      - DB_NAME=postgres

  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
    volumes:
      - postgres-data:/var/lib/postgresql/data

volumes:
  odoo-data:
  postgres-data:
```

#### Step 2: Start Services

```bash
docker-compose up -d
```

#### Step 3: Install via Web Interface

1. Open browser to http://localhost:8069
2. Create database or login
3. Go to Apps menu
4. Update Apps List
5. Install "Scientific Project Manager"

### Method 3: Development Installation

For development purposes with auto-reload:

```bash
# Clone repository
git clone https://github.com/steven0seagal/odoo_scientific_project.git
cd odoo_scientific_project

# Start Odoo with dev mode
odoo-bin --addons-path=/path/to/addons,./odoo/addons \
         --db-filter=^dev_database$ \
         -d dev_database \
         -i scientific_project \
         --dev=all
```

## Verification

After installation, verify the module is working:

### 1. Check Module is Installed

```bash
# Via Odoo shell
odoo-bin shell -d your_database

>>> env['ir.module.module'].search([('name', '=', 'scientific_project')])
# Should return module record with state='installed'
```

### 2. Access the Menu

1. Login to Odoo
2. Look for "Scientific Project" in the main menu
3. You should see submenus: Projects, Tasks, Experiments, etc.

### 3. Test Basic Functionality

Create a test project:

1. Navigate to **Scientific Project → Projects**
2. Click **Create**
3. Fill in required fields
4. Click **Save**

If successful, the module is properly installed!

## Dependencies

The module automatically installs these dependencies:

- `base` - Odoo core functionality (always available)
- `mail` - Messaging and activity tracking

No additional Python packages are required.

## Database Configuration

### Recommended Settings

For optimal performance, configure PostgreSQL:

```sql
-- Increase shared buffers
shared_buffers = 256MB

-- Increase work memory
work_mem = 64MB

-- Enable query optimization
effective_cache_size = 1GB
```

### Create Dedicated Database

```bash
# Create database for scientific projects
createdb -U odoo scientific_projects

# Initialize with Odoo
odoo-bin -d scientific_projects --init=scientific_project --stop-after-init
```

## Troubleshooting Installation

### Issue: Module Not Appearing

**Solution**:
1. Verify module is in addons path
2. Check `__manifest__.py` is present
3. Restart Odoo server
4. Update Apps List

### Issue: Installation Fails

**Causes**:
- Missing dependencies
- Database connection issues
- Insufficient permissions

**Solution**:
```bash
# Check logs
tail -f /var/log/odoo/odoo-server.log

# Verify dependencies
odoo-bin --addons-path=/path/to/addons --test-enable -d test_db -i scientific_project --stop-after-init
```

### Issue: ImportError

**Solution**:
```bash
# Ensure Python path includes module
export PYTHONPATH=/path/to/odoo:$PYTHONPATH

# Verify module structure
ls -la /path/to/addons/scientific_project/
# Should show __init__.py, __manifest__.py, models/, views/, security/
```

## Post-Installation Steps

After successful installation:

1. **Configure Security** - See [Security Guide](../security/overview.md)
2. **Import Initial Data** - Add researchers, equipment
3. **Create User Accounts** - Assign users to appropriate groups
4. **Customize Views** - Adapt to your organization's needs

## Upgrading

To upgrade to a new version:

```bash
# Backup database first!
pg_dump database_name > backup.sql

# Pull latest code
cd /path/to/odoo_scientific_project
git pull origin main

# Upgrade module
odoo-bin -u scientific_project -d database_name
```

## Uninstallation

To uninstall the module:

!!! warning "Data Loss Warning"
    Uninstalling will **permanently delete** all projects, experiments, and related data!

```bash
# Via command line
odoo-bin shell -d database_name

>>> env['ir.module.module'].search([('name', '=', 'scientific_project')]).button_immediate_uninstall()
```

Or via web interface:
1. Apps menu
2. Search "Scientific Project Manager"
3. Click **Uninstall**

## Next Steps

- [Quick Start Guide](quick-start.md) - Create your first project
- [Configuration](configuration.md) - Configure the module
- [Docker Setup](docker-setup.md) - Detailed Docker setup guide

## Getting Help

- Check [Troubleshooting](../troubleshooting.md) for common issues
- Review [FAQ](../faq.md) for frequently asked questions
- Open an issue on [GitHub](https://github.com/steven0seagal/odoo_scientific_project/issues)
