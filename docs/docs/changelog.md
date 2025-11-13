# Changelog

All notable changes to the Scientific Project Manager will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned Features

- Advanced security groups (Manager, PI, User, Viewer)
- Gantt chart view for project timelines
- Budget tracking and expense management
- Sample tracking system
- Advanced reporting and analytics
- Publication management views
- Data management views
- Email notifications and alerts
- Mobile app support

## [15.0.1.0.0] - 2025-11-13

### Added

#### Core Features
- **Project Management Module**
  - Create and manage research projects
  - Track project lifecycle (Draft → In Progress → Done/Cancelled)
  - Assign principal investigators and collaborators
  - Link funding sources
  - Attach documents
  - Activity tracking with Odoo chatter

- **Task Management Module**
  - Create tasks linked to projects
  - Assign multiple researchers to tasks
  - Task status tracking (Planning → In Progress → Completed/Cancelled)
  - Calendar and Kanban views
  - Document attachment support

- **Experiment Tracking Module**
  - Full scientific method workflow
  - Introduction, Hypothesis, Methodology, Results, Conclusion sections
  - Link to parent projects
  - Assign researchers and equipment
  - Experiment status tracking
  - Multiple view types

- **Researcher Management Module**
  - Complete researcher profiles
  - Contact information management
  - Researcher categorization (Student, Professor, Researcher)
  - Tag-based organization with color coding
  - Automatic Odoo user account creation
  - Activity overview (projects, tasks, experiments, documents)

#### Supporting Features
- **Document Management**
  - Multiple document types (Research Paper, Report, Proposal, Ethical Approval, Protocol)
  - Document status workflow (Draft → Submitted → Approved → Published)
  - File upload capability
  - Confidentiality levels (Public, Internal, Confidential)
  - Multi-author support
  - Version tracking

- **Equipment Management**
  - Equipment inventory tracking
  - Status management (Available, In Use, Maintenance)
  - Maintenance scheduling
  - Care taker assignment
  - Location tracking
  - Link to experiments and documents

- **Reagent/Inventory Management**
  - Reagent tracking with quantities
  - Location management
  - Status tracking (Available, Not Available, In Delivery)
  - Link to experiments
  - Type categorization

- **Resource Scheduling**
  - Equipment usage scheduling
  - Researcher time allocation
  - Visual calendar view (weekly)
  - Kanban board for schedule management
  - Experiment linkage

#### Data Models
- **Funding Sources**
  - Track funding with budget and dates
  - Link to projects

- **Publications**
  - Publication management (title, authors, journal, DOI)
  - Link to projects, experiments, and tasks

- **Data Management**
  - Data type tracking (Raw, Processed)
  - Storage location tracking
  - Access control documentation

- **Partners**
  - External collaborator management
  - Partner type (University, Industry, Government)
  - Contact information

#### Views
- **Tree Views** for all main models
- **Form Views** with organized tabs and sections
- **Kanban Views** for visual workflow management
- **Calendar Views** for timeline visualization

#### Technical Features
- Integration with Odoo mail system (chatter, activities, followers)
- Field tracking for audit trails
- Many2many relationships for flexible data linking
- Selection fields for controlled vocabulary
- Binary fields for file uploads

#### Documentation
- Comprehensive README.md with installation guide
- Detailed DOCUMENTATION.md with feature descriptions
- Complete API_REFERENCE.md for developers
- SECURITY.md with security configuration guide
- MkDocs-powered documentation site with Material theme

### Security Notes
⚠️ **Default Configuration**: All users have full access (no group restrictions)
- Suitable for development and testing
- Production deployment requires security configuration
- See SECURITY.md for recommended implementation

### Known Limitations
- No built-in security groups (must be configured)
- Views not created for funding, publication, data_management, partner models
- No automated workflows or state transitions
- Limited field validation
- menu.xml file is empty (menus defined in view files)
- scientific.tags model defined in two files (researcher.py and tag.py)

### Dependencies
- Odoo 15.0
- Python 3.7+
- PostgreSQL 10+
- Required Odoo modules: `base`, `mail`

### File Structure
```
scientific_project/
├── __init__.py
├── __manifest__.py
├── models/ (13 model files)
├── views/ (8 view files)
├── security/ (1 access control file)
└── Documentation (4 comprehensive docs)
```

## Version History

### Version Numbering

Format: `ODOO_VERSION.MAJOR.MINOR.PATCH`

- **Odoo Version**: 15.0 (Odoo version compatibility)
- **Major**: Breaking changes
- **Minor**: New features, backward compatible
- **Patch**: Bug fixes

Example: `15.0.1.0.0`
- Odoo 15.0
- Major version 1
- Minor version 0
- Patch version 0

## Migration Guide

### From Initial Development

If upgrading from development version:

1. **Backup Database**
   ```bash
   pg_dump database > backup_$(date +%Y%m%d).sql
   ```

2. **Update Code**
   ```bash
   git pull origin main
   ```

3. **Upgrade Module**
   ```bash
   odoo-bin -u scientific_project -d database --stop-after-init
   ```

4. **Test Functionality**
   - Verify all views load
   - Test CRUD operations
   - Check relationships
   - Review security settings

### Breaking Changes

None yet (initial release)

## Roadmap

### Version 15.0.2.0.0 (Planned)

- [ ] Implement security groups
- [ ] Add views for funding, publication, data management, partner models
- [ ] Improve menu organization
- [ ] Add computed fields (project progress, task completion rates)
- [ ] Add field validations and constraints

### Version 15.0.3.0.0 (Future)

- [ ] Gantt chart views
- [ ] Budget tracking
- [ ] Sample tracking system
- [ ] Advanced reporting
- [ ] Email notifications
- [ ] Automated workflows

### Version 16.0.1.0.0 (Future)

- Port to Odoo 16.0
- Update for compatibility
- Leverage new Odoo features

## Contributing

See [Contributing Guide](developer-guide/contributing.md) for:
- How to report bugs
- How to suggest features
- Pull request process
- Coding standards

## Support

- **Documentation**: This site
- **Issues**: [GitHub Issues](https://github.com/steven0seagal/odoo_scientific_project/issues)
- **Discussions**: [GitHub Discussions](https://github.com/steven0seagal/odoo_scientific_project/discussions)

## License

Licensed under LGPL-3 (GNU Lesser General Public License v3.0)

---

[Unreleased]: https://github.com/steven0seagal/odoo_scientific_project/compare/v15.0.1.0.0...HEAD
[15.0.1.0.0]: https://github.com/steven0seagal/odoo_scientific_project/releases/tag/v15.0.1.0.0
