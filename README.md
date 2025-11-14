# Odoo Scientific Project Manager

![Odoo Version](https://img.shields.io/badge/Odoo-18.0-blue)
![License](https://img.shields.io/badge/License-LGPL--3-green)
![Version](https://img.shields.io/badge/Version-18.0.1.0.0-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

A comprehensive Odoo 18.0 application for managing scientific research projects, experiments, laboratory equipment, publications, data management, and partner collaborations in research institutions and laboratories.

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

- **Odoo Version**: 18.0
- **Python**: 3.7+
- **PostgreSQL**: 10+
- **Docker**: Supported via Docker Compose
- **Dependencies**: `base`, `mail`

---

## Key Features

### 📊 Project Management
- Complete project lifecycle tracking (Draft → In Progress → Done/Cancelled)
- Principal investigator and collaborator assignment
- **Smart Buttons** for quick navigation to related records:
  - Tasks count and navigation
  - Experiments count and navigation
  - Documents count and navigation
  - Publications count and navigation
- **Dashboard Metrics**:
  - Progress percentage (based on completed tasks)
  - Team size calculation
  - Days remaining until project end
  - Overdue alerts with days count
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
- **Smart Metrics**:
  - Duration calculation (in days)
  - Researcher count
  - Completion status (sections filled: x/4)
  - Days remaining until completion
- Equipment and reagent assignment
- Researcher assignment
- Project integration with cascade deletion
- Status tracking (Planning → Running → Completed/Cancelled)

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
- Conflict prevention and double-booking detection
- Kanban and tree views

### 📚 Publication Management
- Complete publication lifecycle tracking:
  - Status workflow: Draft → Submitted → Under Review → Revision → Accepted → Published/Rejected
  - Multiple publication types: Journal Article, Conference Paper, Book Chapter, Thesis, Preprint, Poster
- **Publication Metrics**:
  - Impact factor tracking (up to 3 decimal places)
  - Citation count management
  - DOI and URL linking
- **Date Tracking**:
  - Publication date
  - Submission date
  - Acceptance date
- Multi-author support with researcher integration
- Project integration for tracking research outputs
- Link to related experiments and tasks
- Abstract and keywords management
- **View Types**: Tree (with status-based coloring), Form, Kanban (grouped by status), Search with filters
- Full audit trail with activity tracking

### 💾 Data Management
- **Comprehensive Dataset Tracking**:
  - Data types: Raw Data, Processed Data, Analysis Results, Metadata
  - File formats: CSV, Excel, JSON, XML, HDF5, and more
  - Version control for dataset evolution
- **Access Control**:
  - Access levels: Public, Internal, Restricted, Confidential
  - Storage location tracking (physical or cloud)
- **File Management**:
  - Binary file upload with automatic size calculation
  - File size tracking in bytes
  - Upload date and last modified timestamps
- **Integration**:
  - Link to projects and experiments
  - Researcher attribution (uploaded by)
- **View Types**: Tree (color-coded by access level), Form, Kanban (grouped by data type), Search with advanced filters
- Security-aware record rules based on access levels

### 🤝 Partner & Collaborator Management
- **Partner Organization Tracking**:
  - Partner types: Academic, Industry, Government, Non-profit
  - Collaboration types: Research Collaboration, Funding Partner, Data Sharing, Equipment Sharing, Joint Publication
  - Status tracking: Active, Inactive, Pending
- **Contact Information**:
  - Complete address management (street, city, state, zip, country)
  - Email and phone contact details
  - Website URL linking
- **Collaboration Details**:
  - Start and end dates for partnerships
  - Multi-project linking
  - Organization affiliation
  - Partnership descriptions and notes
- **View Types**: Tree (with status indicators), Form (with statusbar), Kanban (grouped by partner type), Search with filters
- Full activity tracking and communication history

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

- Odoo 18.0 or higher
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

2. **Configure environment variables** (Recommended for production):
   ```bash
   cd odoo
   cp .env.example .env
   # Edit .env and set a strong database password
   nano .env
   ```

3. **Start the containers**:
   ```bash
   docker-compose up -d
   ```

4. **Access Odoo**:
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

A comprehensive security audit has been conducted and **all critical and high priority security issues have been resolved**.

- **Security Score**: ~~4/10~~ → **8/10** ✅
- **Critical Issues**: ~~3~~ → **0** (All resolved)
- **High Issues**: ~~3~~ → **0** (All resolved)
- **Medium Issues**: ~~3~~ → **0** (All resolved)

See [SECURITY_AUDIT_REPORT.md](SECURITY_AUDIT_REPORT.md) for complete details.

#### ✅ Security Improvements Implemented (2025-11-13)

**Critical Security Fixes:**
1. ✅ **Database Credentials Secured**: Moved hardcoded credentials to environment variables (.env)
2. ✅ **Access Control Implemented**: Created comprehensive security groups (Manager, PI, User, Read-only)
3. ✅ **User Creation Secured**: Fixed insecure automatic user creation with password generation and validation
4. ✅ **Record-Level Security**: Implemented granular record rules for data isolation

**High Priority Fixes:**
5. ✅ **File Upload Validation**: Added size limits (50MB documents, 5MB images) and type restrictions
6. ✅ **Email Validation**: Implemented RFC 5322 email validation
7. ✅ **Date Range Validation**: All models now validate start/end dates
8. ✅ **Equipment Conflict Detection**: Schedule validation prevents double-booking

**Data Integrity:**
9. ✅ **Audit Trails**: Added mail.thread tracking to all critical models (document, experiment, equipment, researcher)
10. ✅ **Uniqueness Constraints**: SQL constraints prevent duplicate projects, equipment, emails, and tags
11. ✅ **Default Values**: All status fields have proper defaults
12. ✅ **Model Ordering**: Consistent sorting across all models

**Code Quality:**
13. ✅ **Fixed Typo**: Changed `raport_created` to `report_created` in experiment model
14. ✅ **Tracking Consistency**: All models use modern `tracking=True` instead of deprecated methods
15. ✅ **Input Validation**: Comprehensive validation on all user inputs

### Recommended Security Groups

| Group | Description | Permissions |
|-------|-------------|-------------|
| **Manager** | Lab managers, directors | Full access to all features |
| **Principal Investigator** | Project leads | Manage own projects, create experiments |
| **User** | Researchers, lab members | View projects, update assigned tasks/experiments |
| **Viewer** | Students, observers | Read-only access to public data |

### Security Checklist

Pre-Production:
- [x] Security groups defined ✅
- [x] Access rights configured ✅
- [x] Record rules implemented ✅
- [x] Database credentials moved to environment variables ✅
- [x] File upload validation added ✅
- [x] Email validation implemented ✅
- [x] Audit logging enabled ✅
- [x] Date range validation added ✅
- [x] SQL uniqueness constraints added ✅

Production (Manual Configuration Required):
- [ ] HTTPS enabled
- [ ] Strong password policy enforced in Odoo settings
- [ ] Two-factor authentication for admins
- [ ] Regular security audits scheduled
- [ ] Backup and recovery tested
- [ ] Update .env file with strong passwords (see odoo/.env.example)

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

### Completed Features ✅

- [x] Advanced security groups (Manager, PI, User, Read-only) ✅
- [x] Publication management views ✅
- [x] Data management views ✅
- [x] Partner/Collaborator management ✅
- [x] Project dashboard with smart buttons ✅
- [x] Computed fields for metrics and analytics ✅

### Planned Features

- [ ] Gantt chart view for project timelines
- [ ] Budget tracking and expense management
- [ ] Integration with laboratory instruments
- [ ] Sample tracking system
- [ ] Advanced reporting and analytics dashboards
- [ ] Email notifications and automated alerts
- [ ] Workflow automation rules
- [ ] Mobile app support
- [ ] API endpoints for external integrations
- [ ] External partner portal for collaborators

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

### Version 18.0.1.0.0 (Current)

**Release Date**: 2025-11-13

**New Features**:
- 📚 **Publication Management System**
  - Complete publication lifecycle (Draft → Published)
  - Impact factor and citation tracking
  - Multi-author support
  - DOI and URL management
  - Full views: Tree, Form, Kanban, Search
- 💾 **Data Management System**
  - Dataset tracking with version control
  - File upload with size tracking
  - Access level control (Public, Internal, Restricted, Confidential)
  - Multiple format support (CSV, Excel, JSON, XML, HDF5)
  - Full views: Tree, Form, Kanban, Search
- 🤝 **Partner & Collaborator Management**
  - Partner organization tracking
  - Collaboration type management
  - Complete contact information
  - Multi-project linking
  - Full views: Tree, Form, Kanban, Search
- 📊 **Enhanced Project Dashboard**
  - Smart buttons for quick navigation (Tasks, Experiments, Documents, Publications)
  - Progress percentage calculation
  - Team size metrics
  - Days remaining/overdue alerts
- 🔬 **Enhanced Experiment Tracking**
  - Duration calculation
  - Researcher count
  - Completion status tracking
  - Days remaining until completion

**Security Enhancements** (See SECURITY_IMPROVEMENTS.md):
- ✅ Comprehensive security groups (Manager, PI, User, Read-only)
- ✅ Record-level access rules for all models including new ones
- ✅ Database credential protection with environment variables
- ✅ File upload validation (50MB documents, 5MB images)
- ✅ Email and date validation across all models
- ✅ Equipment conflict detection
- ✅ Audit trails on all critical models
- ✅ SQL uniqueness constraints
- Security score improved: 4/10 → 8/10

**Code Quality Improvements**:
- Fixed critical typo (raport_created → report_created)
- Added default status values to all models
- Consistent model ordering
- Enhanced field definitions with proper attributes
- Comprehensive input validation

**Documentation**:
- Updated README with all new features
- Security improvements documentation
- API reference updates
- Security audit report

### Version 15.0.1.0.0 (Previous)

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
