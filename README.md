# Odoo Scientific Project Manager

![Odoo Version](https://img.shields.io/badge/Odoo-15.0-blue)
![License](https://img.shields.io/badge/License-LGPL--3-green)
![Version](https://img.shields.io/badge/Version-15.0.1.0.0-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

A comprehensive Odoo 15.0 application for managing scientific research projects, experiments, laboratory equipment, and documentation in research institutions and laboratories.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Security](#security)
- [Development & Maintenance](#development--maintenance)
- [Contributing](#contributing)
- [Support](#support)

## Overview

**Scientific Project Manager** is a complete project management solution designed specifically for scientific research institutions. It provides tools to manage the entire research lifecycle, from project planning and experiment tracking to equipment scheduling and document management.

### Target Users

- **Research Institutions** - Universities, research labs, academic departments
- **R&D Departments** - Corporate research and development teams
- **Clinical Research** - Clinical trial management, medical research
- **Scientific Consulting** - Research consulting firms

### Technology Stack

- **Odoo Version**: 15.0
- **Python**: 3.7+
- **PostgreSQL**: 10+
- **Docker**: Supported via Docker Compose
- **Dependencies**: `base`, `mail`

---

## Key Features

### 📊 Project Management
- Complete project lifecycle tracking (Draft → In Progress → Done/Cancelled)
- Principal investigator and collaborator assignment
- Funding source tracking
- Document attachment and management
- Activity tracking with Odoo Chatter
- Multiple view types: Tree, Form, Kanban, Calendar

### 🔬 Experiment Tracking
- Full scientific method workflow:
  - Introduction and background
  - Hypothesis formulation
  - Methodology documentation
  - Results recording
  - Conclusion and analysis
- Equipment and reagent assignment
- Researcher assignment
- Project integration

### ✅ Task Management
- Multi-researcher task assignment
- Task status tracking (Planning → In Progress → Completed/Cancelled)
- Link tasks to parent projects
- Document attachments
- Calendar and Kanban views for workflow management

### 👥 Researcher Management
- Complete researcher profiles with contact information
- Categorization (Student, Professor, Researcher)
- Specialization tracking
- Tag-based organization with color coding
- Automatic user account creation
- Comprehensive activity overview (projects, tasks, experiments)

### 📄 Document Management
- Multiple document types:
  - Research Papers
  - Reports
  - Proposals
  - Ethical Approvals
  - Experimental Protocols
- Document status workflow (Draft → Submitted → Approved → Published)
- File upload capability
- Confidentiality levels (Public, Internal, Confidential)
- Multi-author support
- Version tracking

### 🔧 Equipment & Inventory Management
- Equipment status tracking (Available, In Use, Maintenance)
- Maintenance scheduling
- Care taker assignment
- Location tracking
- Reagent/inventory management with quantity tracking
- Link to experiments and documents

### 📅 Resource Scheduling
- Equipment usage scheduling
- Researcher time allocation
- Experiment scheduling
- Visual calendar view (weekly)
- Conflict prevention
- Kanban and tree views

### 🎨 User Interface Features
- Multiple view types for each module:
  - **Tree Views**: List views with sorting and filtering
  - **Form Views**: Detailed forms with organized tabs
  - **Kanban Views**: Card-based views with smart grouping
  - **Calendar Views**: Time-based planning views
- Status bars with clickable state transitions
- Organized notebook tabs for related data
- Custom CSS styling for better UX

---

## Installation

### Prerequisites

- Odoo 15.0 or higher
- Python 3.7+
- PostgreSQL 10+
- Docker and Docker Compose (for containerized deployment)

### Docker Installation (Recommended)

This repository includes a complete Docker Compose setup for quick deployment:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/steven0seagal/odoo_scientific_project.git
   cd odoo_scientific_project
   ```

2. **Start the containers**:
   ```bash
   docker-compose up -d
   ```

3. **Access Odoo**:
   - Open your browser to `http://localhost:8069`
   - Create a database and install the "Scientific Project Manager" module

### Manual Installation

1. **Copy the module** to your Odoo addons directory:
   ```bash
   cp -r odoo/addons/scientific_project /path/to/odoo/addons/
   ```

2. **Restart Odoo server**:
   ```bash
   sudo systemctl restart odoo
   ```

3. **Update the addons list**:
   - Go to Apps menu
   - Click "Update Apps List"
   - Search for "Scientific Project Manager"
   - Click "Install"

### Nginx Configuration (Production)

For production deployment with Nginx reverse proxy:

```bash
# Install Nginx
sudo apt update
sudo apt install nginx
sudo ufw allow "Nginx Full"

# Create Odoo configuration
sudo nano /etc/nginx/sites-available/odoo.conf
```

**odoo.conf**:
```nginx
server {
    listen       80;
    listen       [::]:80;
    server_name  your_domain_here;

    access_log  /var/log/nginx/odoo.access.log;
    error_log   /var/log/nginx/odoo.error.log;

    location / {
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-Host $host;
      proxy_set_header X-Forwarded-Proto https;
      proxy_pass http://localhost:8069;
  }
}
```

**Enable the configuration**:
```bash
sudo ln -s /etc/nginx/sites-available/odoo.conf /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx.service
```

### SSL Certificate with Certbot

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your_domain_here
```

---

## Quick Start

### 1. Access the Module

After installation, find **Scientific Project** in the Odoo main menu.

### 2. Create Your First Researcher

1. Navigate to **Scientific Project → Researchers**
2. Click **Create**
3. Fill in researcher information:
   - Name, email, phone
   - Research type (Student/Professor/Researcher)
   - Specialization
   - Tags for categorization
4. The system will automatically create a user account

### 3. Create Your First Project

1. Navigate to **Scientific Project → Projects**
2. Click **Create**
3. Fill in:
   - **Name**: Project title
   - **Start Date** and **End Date**
   - **Description**: Project overview
   - **Principal Investigator**: Select from researchers
4. Click **Save**

### 4. Create an Experiment

1. Navigate to **Scientific Project → Experiments**
2. Click **Create**
3. Complete the experiment form:
   - Basic info (name, dates, status)
   - Introduction and hypothesis
   - Methodology
   - Assign researchers and equipment
4. Update results and conclusions as the experiment progresses

### 5. Schedule Equipment

1. Navigate to **Scientific Project → Schedule**
2. Click **Create** or use Calendar view
3. Select:
   - Equipment
   - Researcher
   - Time slot (start and end date/time)
   - Related experiment

For a complete walkthrough, see the [Quick Start Guide](docs/docs/getting-started/quick-start.md).

---

## Documentation

Comprehensive documentation is available:

- **[Documentation Portal](docs/docs/index.md)** - Main documentation hub
- **[Installation Guide](docs/docs/getting-started/installation.md)** - Detailed installation instructions
- **[Quick Start Guide](docs/docs/getting-started/quick-start.md)** - Get started in 10 minutes
- **[User Guide](docs/docs/user-guide/overview.md)** - Complete feature documentation
- **[API Reference](odoo/addons/scientific_project/API_REFERENCE.md)** - Model and field reference
- **[Security Guide](docs/docs/security/overview.md)** - Security configuration
- **[FAQ](docs/docs/faq.md)** - Frequently asked questions

### Module Structure

```
odoo_scientific_project/
├── docker-compose.yml          # Docker orchestration
├── odoo/
│   └── addons/
│       └── scientific_project/
│           ├── __init__.py
│           ├── __manifest__.py
│           ├── models/         # 13 business models
│           │   ├── project.py
│           │   ├── task.py
│           │   ├── experiment.py
│           │   ├── researcher.py
│           │   ├── document.py
│           │   ├── equipment.py
│           │   ├── reagents.py
│           │   ├── schedule.py
│           │   └── ...
│           ├── views/          # 32+ UI views
│           │   ├── project.xml
│           │   ├── task.xml
│           │   ├── experiment.xml
│           │   └── ...
│           ├── security/       # Access control
│           │   └── ir.model.access.csv
│           ├── static/         # CSS, JS, images
│           ├── README.md
│           ├── DOCUMENTATION.md
│           ├── API_REFERENCE.md
│           └── SECURITY.md
└── docs/                       # MkDocs documentation
    ├── mkdocs.yml
    └── docs/
        ├── getting-started/
        ├── user-guide/
        ├── api-reference/
        └── security/
```

---

## Security

### ⚠️ Important Security Notice

**Default Configuration**: The module ships with open access - all authenticated users have full CRUD permissions on all models. This is suitable for **development and testing only**.

**Before deploying to production**, you **must** implement proper security groups and access controls.

### Security Features

- **Access Rights**: Model-level CRUD permissions
- **Record Rules**: Row-level security filtering
- **Field-Level Security**: Restrict visibility of specific fields
- **Confidentiality Levels**: Public, Internal, Confidential document classification
- **Audit Trails**: Activity tracking via Odoo Chatter (Projects and Tasks)

### Security Audit

A comprehensive security audit has been conducted. Key findings:

- **Security Score**: 4/10 (current) → 8/10 (with fixes)
- **Critical Issues**: 3 (hardcoded credentials, broken access control, insecure user creation)
- **High Issues**: 3 (file upload validation, input validation, date validation)
- **Medium Issues**: 3 (record rules, audit trails, uniqueness constraints)

See [SECURITY_AUDIT_REPORT.md](SECURITY_AUDIT_REPORT.md) for complete details.

### Recommended Security Groups

| Group | Description | Permissions |
|-------|-------------|-------------|
| **Manager** | Lab managers, directors | Full access to all features |
| **Principal Investigator** | Project leads | Manage own projects, create experiments |
| **User** | Researchers, lab members | View projects, update assigned tasks/experiments |
| **Viewer** | Students, observers | Read-only access to public data |

### Security Checklist

Pre-Production:
- [ ] Security groups defined
- [ ] Access rights configured
- [ ] Record rules implemented
- [ ] Database credentials moved to environment variables
- [ ] File upload validation added
- [ ] Email validation implemented
- [ ] Audit logging enabled

Production:
- [ ] HTTPS enabled
- [ ] Strong password policy
- [ ] Two-factor authentication for admins
- [ ] Regular security audits
- [ ] Backup and recovery tested

For complete security configuration, see [Security Guide](docs/docs/security/overview.md) and [SECURITY.md](odoo/addons/scientific_project/SECURITY.md).

---

## Development & Maintenance

### Developer Setup

```bash
# Clone the repository
git clone https://github.com/steven0seagal/odoo_scientific_project.git
cd odoo_scientific_project

# Start development environment
docker-compose up -d

# View logs
docker-compose logs -f odoo

# Stop containers
docker-compose down
```

### Database Management

```bash
# Backup database
docker-compose exec db pg_dump -U odoo postgres > backup.sql

# Restore database
docker-compose exec -T db psql -U odoo postgres < backup.sql
```

### Module Development

**Odoo Configuration**:
- Edit `odoo/etc/odoo.conf` for custom configuration
- Module code is in `odoo/addons/scientific_project/`
- Custom addons can be added to `odoo/addons/`

**Development Workflow**:
1. Make changes to module code
2. Restart Odoo container: `docker-compose restart odoo`
3. Update module in Odoo UI (Apps → Scientific Project Manager → Upgrade)

### Testing

```bash
# Run Odoo with test mode
docker-compose run --rm odoo odoo --test-enable --stop-after-init -d test_db -i scientific_project
```

### Code Quality

**Best Practices**:
- Follow Odoo coding guidelines
- Use proper field validation with `@api.constrains`
- Implement audit trails with `tracking=True`
- Add SQL constraints for data integrity
- Document all models and fields

**Static Analysis**:
```bash
# Install pylint-odoo
pip install pylint-odoo

# Run analysis
pylint --load-plugins=pylint_odoo odoo/addons/scientific_project/
```

### Performance Optimization

- Use proper database indexes for frequently queried fields
- Implement computed fields with `store=True` where appropriate
- Use `@api.depends` correctly for computed fields
- Archive old records instead of deleting
- Regular database maintenance (VACUUM, ANALYZE)

### Maintenance Tasks

**Regular Tasks**:
- Weekly database backups
- Monthly security updates
- Quarterly access rights review
- Monitor disk space usage
- Review error logs

**Upgrade Process**:
1. Backup database and filestore
2. Test upgrade on staging environment
3. Review and update custom code for compatibility
4. Perform upgrade on production
5. Verify all functionality
6. Monitor for issues

### Troubleshooting

Common issues and solutions:

**Issue**: Module not appearing in Apps list
- **Solution**: Update apps list, check module path in addons_path

**Issue**: Permission denied errors
- **Solution**: Check file ownership: `chown -R 101:101 odoo/addons/scientific_project/`

**Issue**: Database connection errors
- **Solution**: Verify PostgreSQL is running, check credentials

**Issue**: Container startup failures
- **Solution**: Check logs with `docker-compose logs odoo`

For more troubleshooting, see the [documentation](docs/docs/faq.md).

---

## Contributing

We welcome contributions! Here's how you can help:

1. **Report Bugs**: Submit issues on [GitHub Issues](https://github.com/steven0seagal/odoo_scientific_project/issues)
2. **Suggest Features**: Open a feature request with detailed description
3. **Submit Pull Requests**:
   - Fork the repository
   - Create a feature branch (`git checkout -b feature/AmazingFeature`)
   - Commit your changes (`git commit -m 'Add some AmazingFeature'`)
   - Push to the branch (`git push origin feature/AmazingFeature`)
   - Open a Pull Request
4. **Improve Documentation**: Help make the docs better
5. **Share Use Cases**: Tell us how you use the module

### Development Guidelines

- Follow Odoo development best practices
- Write clear commit messages
- Add tests for new features
- Update documentation for changes
- Ensure security best practices
- Test thoroughly before submitting PR

---

## Roadmap

### Planned Features

- [ ] Advanced security groups (Manager, User, Read-only)
- [ ] Gantt chart view for project timelines
- [ ] Budget tracking and expense management
- [ ] Integration with laboratory instruments
- [ ] Sample tracking system
- [ ] Advanced reporting and analytics
- [ ] Publication management views
- [ ] Data management views
- [ ] Partner/Collaborator portal
- [ ] Email notifications and alerts
- [ ] Mobile app support
- [ ] API endpoints for external integrations

---

## Support

### Getting Help

- **Documentation**: Check the [comprehensive documentation](docs/docs/index.md)
- **FAQ**: Review [frequently asked questions](docs/docs/faq.md)
- **Issues**: Report bugs on [GitHub Issues](https://github.com/steven0seagal/odoo_scientific_project/issues)
- **Discussions**: Join the community discussions

### Commercial Support

For commercial support, customization, or implementation services, please contact the maintainers via GitHub.

---

## License

This module is licensed under **LGPL-3** (GNU Lesser General Public License v3.0).

See the [LICENSE](LICENSE) file for details.

---

## Changelog

### Version 15.0.1.0.0 (Current)

**Release Date**: 2024-11

**Features**:
- Core project management with lifecycle tracking
- Complete experiment workflow following scientific method
- Task management with multi-researcher assignment
- Researcher profiles with automatic user creation
- Document management with confidentiality levels
- Equipment and reagent inventory tracking
- Resource scheduling with calendar views
- Multiple view types (Tree, Form, Kanban, Calendar)
- Chatter integration for communication
- Tag-based organization system

**Documentation**:
- Comprehensive user documentation
- API reference
- Security guides
- Security audit report

---

## Credits

### Maintainer

This module is maintained by the Scientific Project Manager development team.

### Contributors

- Development Team
- Community Contributors

---

**Made with ❤️ for the scientific community**

For the latest updates and documentation, visit the [GitHub Repository](https://github.com/steven0seagal/odoo_scientific_project).
