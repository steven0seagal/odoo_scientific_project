# Scientific Project Manager

![Odoo Version](https://img.shields.io/badge/Odoo-15.0-blue)
![License](https://img.shields.io/badge/License-LGPL--3-green)
![Version](https://img.shields.io/badge/Version-15.0.1.0.0-orange)

Welcome to the **Scientific Project Manager** documentation! This comprehensive Odoo 15.0 addon is designed to manage scientific research projects, experiments, researchers, laboratory equipment, and documentation in research institutions and laboratories.

## Overview

Scientific Project Manager provides a complete project management solution designed specifically for scientific research institutions. It provides tools to manage the entire research lifecycle, from project planning and experiment tracking to equipment scheduling and document management.

## Key Features

### 📊 Project Management
- Complete project lifecycle tracking (Draft → In Progress → Done/Cancelled)
- Principal investigator and collaborator assignment
- Funding source tracking
- Document attachment and management
- Activity tracking with Odoo Chatter

### 🔬 Experiment Tracking
- Full scientific method workflow (Introduction, Hypothesis, Methodology, Results, Conclusion)
- Equipment and reagent assignment
- Researcher assignment
- Multiple view types (Tree, Form, Kanban)

### ✅ Task Management
- Multi-researcher task assignment
- Task status tracking
- Link tasks to parent projects
- Calendar and Kanban views

### 👥 Researcher Management
- Complete researcher profiles with contact information
- Categorization (Student, Professor, Researcher)
- Tag-based organization with color coding
- Automatic user account creation

### 📄 Document Management
- Multiple document types (Research Papers, Reports, Proposals, etc.)
- Document status workflow
- Confidentiality levels
- Multi-author support

### 🔧 Equipment & Inventory
- Equipment status tracking
- Maintenance scheduling
- Reagent inventory management
- Location tracking

### 📅 Resource Scheduling
- Equipment usage scheduling
- Researcher time allocation
- Visual calendar view
- Conflict prevention

## Quick Navigation

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } __Getting Started__

    ---

    Install and configure Scientific Project Manager in minutes

    [:octicons-arrow-right-24: Installation Guide](getting-started/installation.md)

-   :material-book-open-variant:{ .lg .middle } __User Guide__

    ---

    Learn how to use all features effectively

    [:octicons-arrow-right-24: User Guide](user-guide/overview.md)

-   :material-api:{ .lg .middle } __API Reference__

    ---

    Complete technical documentation for developers

    [:octicons-arrow-right-24: API Reference](api-reference/overview.md)

-   :material-shield-lock:{ .lg .middle } __Security__

    ---

    Configure security groups and access control

    [:octicons-arrow-right-24: Security Guide](security/overview.md)

</div>

## Target Users

- **Research Institutions** - Universities, research labs, academic departments
- **R&D Departments** - Corporate research and development teams
- **Clinical Research** - Clinical trial management, medical research
- **Scientific Consulting** - Research consulting firms

## Technology Stack

- **Odoo Version**: 15.0
- **Python**: 3.7+
- **PostgreSQL**: 10+
- **Dependencies**: `base`, `mail`

## Module Structure

```
scientific_project/
├── models/          # Business logic (13 models)
├── views/           # User interface (32+ views)
├── security/        # Access control
└── static/          # Assets (CSS, JS, images)
```

## What's Next?

!!! tip "New to Scientific Project Manager?"
    Start with the [Installation Guide](getting-started/installation.md) to set up the module, then follow the [Quick Start Guide](getting-started/quick-start.md) to create your first project.

!!! info "For Developers"
    Check out the [API Reference](api-reference/overview.md) for complete technical documentation and the [Developer Guide](developer-guide/architecture.md) for extending the module.

!!! warning "Security Important"
    Before deploying to production, review the [Security Guide](security/overview.md) to configure proper access controls.

## Support & Community

- **Documentation**: You're reading it!
- **Issues**: [GitHub Issues](https://github.com/steven0seagal/odoo_scientific_project/issues)
- **Source Code**: [GitHub Repository](https://github.com/steven0seagal/odoo_scientific_project)

## License

This module is licensed under LGPL-3 (GNU Lesser General Public License v3.0).

---

**Ready to get started?** Head over to the [Installation Guide](getting-started/installation.md)!
