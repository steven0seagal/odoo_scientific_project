# Scientific Project Manager

[![Odoo Version](https://img.shields.io/badge/Odoo-18.0-blue)](https://www.odoo.com/)
[![License](https://img.shields.io/badge/License-LGPL--3-green)](https://www.gnu.org/licenses/lgpl-3.0.en.html)
[![Version](https://img.shields.io/badge/Version-18.0.1.0.0-orange)](https://github.com/)

A comprehensive Odoo 18.0 addon for managing scientific research projects, experiments, researchers, laboratory equipment, and documentation in research institutions and laboratories.

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

### 📊 Project Management
- Complete project lifecycle tracking (Draft → In Progress → Done/Cancelled)
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
- Equipment and reagent assignment
- Researcher assignment
- Multiple view types (Tree, Form, Kanban)

### ✅ Task Management
- Multi-researcher task assignment
- Task status tracking (Planning → In Progress → Completed/Cancelled)
- Link tasks to parent projects
- Document attachments
- Calendar and Kanban views

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
- Status bars with clickable state transitions
- Organized notebook tabs for related data
- Custom CSS styling for better UX

## Installation

### Prerequisites

- Odoo 18.0 or higher
- Python 3.10+
- PostgreSQL 13+

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
    image: odoo:18.0
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
├── __init__.py                  # Module initialization
├── __manifest__.py              # Module manifest and configuration
├── README.md                    # This file
├── DOCUMENTATION.md             # Detailed feature documentation
├── API_REFERENCE.md             # Model and field reference
├── SECURITY.md                  # Security configuration guide
│
├── models/                      # Business logic
│   ├── __init__.py
│   ├── project.py              # Projects
│   ├── task.py                 # Tasks
│   ├── experiment.py           # Experiments
│   ├── researcher.py           # Researchers and Tags
│   ├── document.py             # Documents
│   ├── equipment.py            # Equipment
│   ├── reagents.py             # Reagents/Chemicals
│   ├── schedule.py             # Resource Scheduling
│   ├── funding.py              # Funding Sources
│   ├── publication.py          # Publications
│   ├── data.py                 # Data Management
│   ├── partner.py              # Partners/Collaborators
│   └── static/src/styles.css   # Custom CSS
│
├── views/                       # User interface definitions
│   ├── project.xml             # Project views and main menu
│   ├── task.xml                # Task views
│   ├── experiment.xml          # Experiment views
│   ├── researcher.xml          # Researcher views
│   ├── document.xml            # Document views
│   ├── equipment.xml           # Equipment views
│   ├── reagents.xml            # Reagent views
│   └── schedule.xml            # Schedule views
│
└── security/                    # Access control
    └── ir.model.access.csv     # Model access rights
```

## Documentation

Comprehensive documentation is available in the following files:

- **[DOCUMENTATION.md](DOCUMENTATION.md)** - Detailed feature guide with usage examples
- **[API_REFERENCE.md](API_REFERENCE.md)** - Complete model and field reference
- **[SECURITY.md](SECURITY.md)** - Security configuration and best practices

## Configuration

### Menu Structure

The module adds a main menu "Scientific Project" with the following submenus:
- Projects
- Tasks
- Experiments
- Researchers
- Documents
- Equipment
- Reagents
- Schedule

### Access Rights

By default, all models have full CRUD access (Create, Read, Update, Delete) with no group restrictions. For production environments, it's recommended to implement proper security groups. See [SECURITY.md](SECURITY.md) for details.

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
- **Supported**: Odoo 18.0
- **Application Type**: Full Application
- **Auto Install**: No

### Models
- 13 models covering all aspects of scientific project management
- Integrated with Odoo's mail system for activity tracking
- Relational database design with proper foreign keys

### Views
- 4 types of views: Tree, Form, Kanban, Calendar
- Responsive design
- Custom CSS styling
- Status bars with smart buttons

### Performance
- Optimized for research teams of 10-1000 users
- Efficient database queries
- Scalable architecture

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

### Version 18.0.1.0.0 (Current)
- Migrated to Odoo 18.0
- Updated deprecated `track_visibility` to `tracking=True`
- Modernized view widget references
- Updated Docker configuration to Odoo 18 and PostgreSQL 15
- All core features maintained and compatible

### Version 15.0.1.0.0
- Initial release
- Core project management features
- Experiment tracking
- Task management
- Researcher profiles
- Document management
- Equipment and reagent tracking
- Resource scheduling
- Multiple view types (Tree, Form, Kanban, Calendar)

---

**Made with ❤️ for the scientific community**
