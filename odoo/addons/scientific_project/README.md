# Scientific Project Manager

[![Odoo Version](https://img.shields.io/badge/Odoo-15.0-blue)](https://www.odoo.com/)
[![License](https://img.shields.io/badge/License-LGPL--3-green)](https://www.gnu.org/licenses/lgpl-3.0.en.html)
[![Version](https://img.shields.io/badge/Version-15.0.2.0.0-orange)](https://github.com/)
[![Status](https://img.shields.io/badge/Status-Production_Ready-success)](https://github.com/)

A comprehensive Odoo 15.0 addon for managing scientific research projects, experiments, researchers, laboratory equipment, and documentation in research institutions and laboratories.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Module Structure](#module-structure)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Support](#support)

## Overview

**Scientific Project Manager** is a complete project management solution designed specifically for scientific research institutions. It provides tools to manage the entire research lifecycle, from project planning and experiment tracking to equipment scheduling and document management.

### Target Users

- Research Institutions
- University Laboratories
- Research & Development Departments
- Clinical Research Organizations
- Scientific Consulting Firms

## Key Features

### 📊 Dashboard & Analytics ✨ NEW
- **Real-time metrics**: 16 computed statistics (projects, tasks, experiments, publications, resources)
- **User-specific filtering**: "My Projects", "My Tasks" for personalized views
- **Quick actions**: One-click navigation to key areas
- **Actionable insights**: Overdue task alerts, completion tracking
- **Professional design**: Stat buttons, icons, conditional displays

### 📊 Project Management
- Complete project lifecycle tracking (Draft → In Progress → Done/Cancelled)
- **Smart buttons**: Quick access to experiments, tasks, documents, publications, funding
- **Computed fields**: Budget totals, completion percentage, days remaining, task counts
- **Gantt view**: Visual timeline for project planning ✨ NEW
- **Workflow actions**: Start, complete, cancel, archive projects with one click ✨ NEW
- Principal investigator and collaborator assignment
- Funding source tracking
- Document attachment and management
- Activity tracking with Odoo Chatter

### 🔬 Experiment Tracking
- Full scientific method workflow
  - Introduction and background
  - Hypothesis formulation
  - Methodology documentation
  - Results recording
  - Conclusion and analysis
- **Computed fields**: Duration, overdue status, completion tracking ✨ NEW
- **Clone functionality**: Duplicate experiments for similar studies ✨ NEW
- **Email notifications**: Automatic alerts on completion ✨ NEW
- Equipment and reagent assignment
- Researcher assignment
- Multiple view types (Tree, Form, Kanban)
- **Enhanced forms**: Priority ribbons, status badges, color-coded displays ✨ NEW

### ✅ Task Management
- **Priority system**: 3-star priority ranking ✨ NEW
- **Gantt view**: Visual task scheduling and timeline management ✨ NEW
- **Modern Kanban**: Drag-and-drop with avatars, badges, and progress indicators ✨ NEW
- **Intelligent tracking**: Auto-computed progress (on_track/at_risk/overdue) ✨ NEW
- **Email notifications**: Assignment alerts, due date reminders ✨ NEW
- **Computed fields**: Days remaining, duration, overdue status, completion time ✨ NEW
- Multi-researcher task assignment
- Task status tracking (Todo → In Progress → Completed/Cancelled)
- Link tasks to parent projects and experiments
- Document attachments
- **Color-coded displays**: Red (overdue), Green (completed), Blue (in progress) ✨ NEW
- Calendar and enhanced Kanban views

### 👥 Researcher Management
- Complete researcher profiles with contact information
- Categorization (Student, Professor, Researcher)
- Specialization tracking
- Tag-based organization with color coding
- **Enhanced user creation**: Automatic account generation with error handling ✨ NEW
- **Email validation**: Ensures valid contact information ✨ NEW
- Comprehensive activity overview (projects, tasks, experiments)

### 📚 Publication Management ✨ NEW
- **Complete workflow**: Draft → Submitted → Under Review → Published
- **DOI validation**: Automatic format checking (10.xxxx/xxxxx)
- **Author management**: Link researchers to publications
- **Journal tracking**: Publication venue, impact factor, citation count
- **Multiple views**: Tree, Form, Kanban, Search with filters
- **Publication type**: Journal, Conference, Book Chapter, Thesis, Report

### 💾 Data Management ✨ NEW
- **Dataset lifecycle**: Draft → Active → Archived → Deprecated
- **Version control**: Track dataset versions and changes
- **Access levels**: Public, Internal, Restricted, Confidential
- **Checksums**: MD5 hashing for data integrity
- **Storage tracking**: File size, format, location
- **Complete CRUD interface**: Professional forms and views

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

### 🔧 Equipment Management
- Equipment status tracking (Available, In Use, Maintenance)
- Maintenance scheduling
- Care taker assignment
- Location tracking
- Link to experiments and documents

### 🧪 Reagent/Inventory Management
- Reagent availability and quantity tracking
- Location management
- Status tracking (Available, Not Available, In Delivery)
- Link to experiments and projects

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
  - **Gantt Views**: Timeline visualization for projects and tasks ✨ NEW
- **Smart buttons**: One-click navigation between related records ✨ NEW
- **Color-coded displays**: Status-based coloring throughout the interface ✨ NEW
- Status bars with clickable state transitions
- Organized notebook tabs for related data
- Custom CSS styling for better UX

### 🔐 Security & Access Control ✨ NEW
- **Role-Based Access Control (RBAC)**: 5-tier security system
  - **Observer**: Read-only access to public data
  - **Technician**: Basic operations on equipment and schedules
  - **Researcher**: Full research operations (experiments, tasks, publications)
  - **Principal Investigator**: Project management and team oversight
  - **Manager**: Full administrative access to all features
- **65 Access Rules**: Granular permissions across 13 models
- **Record Rules**: User-specific and role-based data filtering
- **Data Validation**: Email, DOI, date, and budget validation
- **Audit Trails**: Complete activity tracking via Chatter

### 📧 Automation & Notifications ✨ NEW
- **4 Email Templates**: Professional HTML notifications
  - Task assignment alerts
  - Due date reminders
  - Project status changes
  - Experiment completion notifications
- **4 Automated Actions**: Triggered workflows
  - Task assignment notifications
  - Project status change alerts
  - Experiment completion notices
  - Auto-project updates from tasks
- **2 Scheduled Actions**: Recurring tasks
  - Daily overdue task reminders
  - Weekly PI project summaries (optional)
- **Intelligent suggestions**: Auto-suggest project closure when all tasks complete

## Installation

### Prerequisites

- Odoo 15.0 or higher
- Python 3.7+
- PostgreSQL 10+

### Dependencies

This module depends on the following Odoo modules:
- `base` - Core Odoo functionality
- `mail` - Messaging and activity tracking

### Installation Steps

1. **Clone or copy the module** to your Odoo addons directory:
   ```bash
   cd /path/to/odoo/addons
   git clone <repository-url> scientific_project
   ```

2. **Update the addons list**:
   - Restart your Odoo server
   - Go to Apps menu
   - Click "Update Apps List"

3. **Install the module**:
   - Search for "Scientific Project Manager"
   - Click "Install"

### Docker Installation

If you're using Docker, add the module to your custom addons directory and update your `docker-compose.yml`:

```yaml
version: '3'
services:
  odoo:
    image: odoo:15.0
    volumes:
      - ./odoo/addons/scientific_project:/mnt/extra-addons/scientific_project
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo
```

## Quick Start

### 1. Access the Module

After installation, you'll find "Scientific Project" in the main menu.

### 2. Create Your First Project

1. Navigate to **Scientific Project → Projects**
2. Click **Create**
3. Fill in the required fields:
   - **Name**: Project title
   - **Start Date** and **End Date**
   - **Description**: Project overview
   - **Principal Investigator**: Select from researchers
4. Click **Save**

### 3. Add Researchers

1. Navigate to **Scientific Project → Researchers**
2. Click **Create**
3. Enter researcher information:
   - Name, email, phone
   - Research type (Student/Professor/Researcher)
   - Specialization
   - Tags for categorization
4. The system will automatically create a user account

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
2. Click **Create**
3. Select:
   - Equipment
   - Researcher
   - Time slot (start and end date/time)
   - Related experiment
4. View schedules in Calendar view for easy planning

## Module Structure

```
scientific_project/
├── __init__.py                      # Module initialization
├── __manifest__.py                  # Module manifest and configuration
├── README.md                        # This file
├── DOCUMENTATION.md                 # Detailed feature documentation
├── API_REFERENCE.md                 # Model and field reference
├── SECURITY.md                      # Security configuration guide
├── IMPROVEMENTS_IMPLEMENTED.md      # Phase 1 improvements (Security, Models, Views) ✨ NEW
├── PHASE2_IMPROVEMENTS.md           # Phase 2 improvements (UX, Smart Buttons, Gantt) ✨ NEW
├── PHASE3_NOTIFICATIONS.md          # Phase 3 improvements (Emails, Automation) ✨ NEW
├── PHASE4_DASHBOARD.md              # Phase 4 improvements (Dashboard, Analytics) ✨ NEW
├── IMPLEMENTATION_COMPLETE.md       # Complete implementation summary ✨ NEW
│
├── models/                          # Business logic (14 models)
│   ├── __init__.py
│   ├── project.py                  # Projects (enhanced with 7 computed fields) ✨
│   ├── task.py                     # Tasks (enhanced with priority, 5 computed fields) ✨
│   ├── experiment.py               # Experiments (fixed typo, 8 computed fields) ✨
│   ├── researcher.py               # Researchers (enhanced user creation) ✨
│   ├── document.py                 # Documents
│   ├── equipment.py                # Equipment
│   ├── reagents.py                 # Reagents/Chemicals
│   ├── schedule.py                 # Resource Scheduling
│   ├── funding.py                  # Funding Sources
│   ├── publication.py              # Publications (complete rewrite) ✨
│   ├── data.py                     # Data Management (complete rewrite) ✨
│   ├── partner.py                  # Partners/Collaborators (enhanced) ✨
│   ├── dashboard.py                # Dashboard & Analytics ✨ NEW
│   └── static/src/styles.css       # Custom CSS
│
├── views/                           # User interface definitions (40+ views)
│   ├── dashboard.xml               # Dashboard view ✨ NEW
│   ├── project.xml                 # Project views (enhanced with smart buttons, Gantt) ✨
│   ├── task.xml                    # Task views (complete rewrite, Kanban, Gantt) ✨
│   ├── experiment.xml              # Experiment views (enhanced forms) ✨
│   ├── researcher.xml              # Researcher views
│   ├── document.xml                # Document views
│   ├── equipment.xml               # Equipment views
│   ├── reagents.xml                # Reagent views
│   ├── schedule.xml                # Schedule views
│   ├── publication.xml             # Publication views ✨ NEW
│   ├── data_management.xml         # Data management views ✨ NEW
│   └── partner.xml                 # Partner views ✨ NEW
│
├── data/                            # Data files ✨ NEW
│   ├── mail_templates.xml          # Email notification templates (4) ✨ NEW
│   └── automated_actions.xml       # Automated & scheduled actions (6) ✨ NEW
│
└── security/                        # Access control
    ├── security.xml                # Security groups & record rules ✨ NEW
    └── ir.model.access.csv         # Model access rights (65 rules) ✨
```

## Documentation

Comprehensive documentation is available in the following files:

### Core Documentation
- **[DOCUMENTATION.md](DOCUMENTATION.md)** - Detailed feature guide with usage examples
- **[API_REFERENCE.md](API_REFERENCE.md)** - Complete model and field reference
- **[SECURITY.md](SECURITY.md)** - Security configuration and best practices

### Implementation Guides ✨ NEW
- **[IMPROVEMENTS_IMPLEMENTED.md](IMPROVEMENTS_IMPLEMENTED.md)** - Phase 1: Security, Models & Views
- **[PHASE2_IMPROVEMENTS.md](PHASE2_IMPROVEMENTS.md)** - Phase 2: UX Enhancement & Gantt Views
- **[PHASE3_NOTIFICATIONS.md](PHASE3_NOTIFICATIONS.md)** - Phase 3: Email Notifications & Automation
- **[PHASE4_DASHBOARD.md](PHASE4_DASHBOARD.md)** - Phase 4: Dashboard & Analytics
- **[IMPLEMENTATION_COMPLETE.md](IMPLEMENTATION_COMPLETE.md)** - Complete implementation summary with testing checklist

## Configuration

### Menu Structure

The module adds a main menu "Scientific Project" with the following submenus:
- **Dashboard** - Overview and analytics ✨ NEW (Top menu item)
- Projects
- Tasks
- Experiments
- Publications ✨ NEW
- Data Management ✨ NEW
- Researchers
- Partners ✨ NEW
- Documents
- Equipment
- Reagents
- Schedule

### Access Rights ✨ UPDATED

**Production-Ready Security**: The module now includes a complete Role-Based Access Control (RBAC) system with 5 security groups:

| Group | Description | Access Level |
|-------|-------------|--------------|
| **Observer** | Students, visitors | Read-only access to public data |
| **Technician** | Lab technicians | Equipment and schedule management |
| **Researcher** | Research staff | Full access to experiments, tasks, publications |
| **Principal Investigator** | Project leads | Project management and team oversight |
| **Manager** | Lab managers | Full administrative access |

**Security Features**:
- **65 Access Rules**: Granular CRUD permissions across all 13 models
- **Record Rules**: User-specific data filtering (e.g., "My Projects", "My Tasks")
- **Field Validation**: Email, DOI, date, and budget constraints
- **Audit Trails**: Complete activity tracking via Odoo Chatter

See [SECURITY.md](SECURITY.md) and [IMPROVEMENTS_IMPLEMENTED.md](IMPROVEMENTS_IMPLEMENTED.md) for detailed configuration.

### Customization

The module is designed to be easily customizable:
- Add custom fields in model files
- Extend views with inherited views
- Add custom business logic with Python
- Create custom reports
- Integrate with external systems via Odoo's API

## Use Cases

### Academic Research Institution
- Track multiple research projects across departments
- Manage student, faculty, and post-doc researchers
- Schedule shared laboratory equipment
- Track grant funding and publications
- Maintain compliance documentation

### Clinical Research Organization
- Manage clinical trials and study protocols
- Track patient data and experimental results
- Schedule medical equipment and facilities
- Maintain regulatory documentation
- Track multi-site collaborations

### R&D Department
- Coordinate product development projects
- Track experimental iterations
- Manage lab inventory and equipment
- Document intellectual property
- Collaborate with external partners

## Technical Specifications

### Odoo Version
- **Supported**: Odoo 15.0
- **Application Type**: Full Application
- **Auto Install**: No
- **Version**: 15.0.2.0.0
- **Status**: Production Ready ✨

### Models
- **14 models** covering all aspects of scientific project management ✨
- **1 TransientModel** for dashboard (real-time analytics without DB overhead) ✨
- Integrated with Odoo's mail system for activity tracking
- Relational database design with proper foreign keys
- **40+ computed fields** for automatic calculations ✨
- **Comprehensive validation** with constraints and domain filters ✨

### Views
- **5 types of views**: Tree, Form, Kanban, Calendar, Gantt ✨
- **40+ views** across all modules ✨
- **Smart buttons** for one-click navigation ✨
- **Color-coded displays** throughout ✨
- Responsive design
- Custom CSS styling
- Status bars with clickable state transitions
- **Professional dashboard** with stat buttons and quick actions ✨

### Automation ✨ NEW
- **4 Email Templates**: HTML notifications with inline CSS
- **4 Automated Actions**: Event-triggered workflows
- **2 Scheduled Actions**: Daily and weekly recurring tasks
- **Intelligent workflows**: Auto-suggestions and status updates

### Security ✨ NEW
- **5 Security Groups**: Observer, Technician, Researcher, PI, Manager
- **65 Access Rules**: Granular CRUD permissions
- **Record Rules**: Row-level security and user-specific filtering
- **Data Validation**: Email, DOI, date, and budget constraints

### Performance
- Optimized for research teams of 10-1000 users
- **Efficient queries**: `search_count()` for statistics ✨
- **User context**: `@api.depends_context('uid')` for personalized data ✨
- **TransientModel dashboard**: No database storage, always fresh data ✨
- Scalable architecture

## Roadmap

### ✅ Completed Features (Version 15.0.2.0.0)
- [x] **Advanced security groups** - 5-tier RBAC system (Observer, Technician, Researcher, PI, Manager) ✅
- [x] **Gantt chart views** - Project and task timeline visualization ✅
- [x] **Publication management** - Complete workflow with DOI validation ✅
- [x] **Data management views** - Dataset lifecycle management ✅
- [x] **Partner/Collaborator management** - Enhanced partner views ✅
- [x] **Email notifications** - 4 HTML templates for key events ✅
- [x] **Automated workflows** - 4 triggered actions + 2 scheduled tasks ✅
- [x] **Dashboard & Analytics** - 16 real-time statistics with quick actions ✅
- [x] **Smart buttons** - One-click navigation throughout ✅
- [x] **Computed fields** - 40+ auto-calculated fields ✅
- [x] **Budget tracking** - Via funding sources model ✅

### 🚀 Planned Features
- [ ] Budget reports and visualizations
- [ ] Integration with laboratory instruments (LIMS)
- [ ] Sample tracking and inventory system
- [ ] Advanced charts and graphs on dashboard
- [ ] Mobile app support
- [ ] API endpoints for external integrations
- [ ] Custom report builder
- [ ] Multi-language support
- [ ] Advanced search and filtering
- [ ] Export to various formats (PDF, Excel, CSV)

## Contributing

We welcome contributions! Here's how you can help:

1. **Report Bugs**: Submit issues on GitHub
2. **Suggest Features**: Open a feature request
3. **Submit Pull Requests**: Fork, create a branch, and submit PR
4. **Improve Documentation**: Help us make docs better
5. **Share Use Cases**: Tell us how you use the module

### Development Setup

```bash
# Clone the repository
git clone <repository-url>

# Install development dependencies
pip install -r requirements.txt

# Run tests (when available)
python -m pytest tests/
```

## Support

### Getting Help
- **Documentation**: Check DOCUMENTATION.md for detailed guides
- **Issues**: Report bugs on GitHub
- **Community**: Join discussions on Odoo forums

### Commercial Support
For commercial support, customization, or implementation services, please contact:
- Website: www.example.com
- Email: support@example.com

## License

This module is licensed under LGPL-3 (GNU Lesser General Public License v3.0).

See the [LICENSE](LICENSE) file for details.

## Credits

### Contributors
- Development Team
- Community Contributors

### Maintainer
This module is maintained by the Scientific Project Manager team.

## Changelog

### Version 15.0.2.0.0 (Current) - 2025-11-13 ✨ NEW
**Major Update**: Production-ready with complete RBAC, automation, and analytics

**Phase 4 - Dashboard & Analytics**:
- Added professional dashboard with 16 real-time statistics
- Implemented user-specific filtering (My Projects, My Tasks)
- Created 5 quick action methods for navigation
- Added onboarding tips section

**Phase 3 - Email Notifications & Automation**:
- Created 4 professional HTML email templates
- Implemented 4 automated actions (task assignment, status changes, completions)
- Added 2 scheduled actions (daily overdue reminders, weekly summaries)
- Intelligent workflow suggestions

**Phase 2 - UX Enhancement**:
- Added smart buttons to project forms (5 stat buttons)
- Implemented Gantt views for projects and tasks
- Created modern Kanban view with avatars and badges
- Enhanced task model with priority and 5 computed fields
- Color-coded displays throughout interface

**Phase 1 - Security, Models & Views**:
- Fixed critical typo: `raport_created` → `report_created`
- Implemented 5-tier RBAC system (65 access rules)
- Enhanced 8 models with validation and computed fields
- Created Publication, Data Management, and Partner views
- Added DOI and email validation

**Total Changes**:
- 4,000+ lines of code added
- 14 models (1 new TransientModel)
- 40+ views created/enhanced
- 5 security groups with 65 access rules
- 6 automation workflows
- 5 comprehensive documentation files

### Version 15.0.1.0.0 - 2024-11
**Initial Release**:
- Core project management features
- Experiment tracking following scientific method
- Task management with multi-researcher assignment
- Researcher profiles with automatic user creation
- Document management with confidentiality levels
- Equipment and reagent tracking
- Resource scheduling
- Multiple view types (Tree, Form, Kanban, Calendar)

---

**Made with ❤️ for the scientific community**
