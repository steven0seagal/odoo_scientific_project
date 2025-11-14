
{
    'name': 'Scientific Project Manager',
    'version': '15.0.2.0.0',
    'summary': 'Production-Ready Scientific Project Management with Dashboard & Analytics',
    'sequence': -99,
    'description': """
        Scientific Project Manager
        ==========================

        A production-ready system for managing scientific research projects, including:
        - Dashboard with 16 real-time analytics
        - Project and experiment tracking with Gantt views
        - Publication management with DOI validation
        - Data management and versioning
        - Partner and collaborator management
        - Equipment and reagent inventory
        - Task management with priority and smart scheduling
        - 5-tier role-based access control (RBAC)
        - Document management with confidentiality levels
        - Email notifications and automated workflows

        Version 15.0.2.0.0 Features:
        - Professional dashboard with quick actions
        - 5 security groups with 65 access rules
        - 4 HTML email templates for notifications
        - 6 automated and scheduled actions
        - Smart buttons for one-click navigation
        - Gantt views for timeline visualization
        - 40+ computed fields for real-time insights
        - Complete data validation (email, DOI, dates, budgets)
        - Enhanced UX with color-coded displays
        - Publication and data lifecycle management
    """,
    'category': 'Project',
    'author': 'Scientific Project Team',
    'website': 'www.example.com',
    'license': 'LGPL-3',
    'depends': ['mail', 'base', 'base_automation'],
    'data': [
        # Security
        'security/security.xml',
        'security/ir.model.access.csv',

        # Data
        'data/mail_templates.xml',
        'data/automated_actions.xml',

        # Views - project.xml must be loaded first as it defines the main menu
        'views/project.xml',
        'views/dashboard.xml',
        'views/task.xml',
        'views/document.xml',
        'views/experiment.xml',
        'views/researcher.xml',
        'views/equipment.xml',
        'views/reagents.xml',
        'views/schedule.xml',
        'views/publication.xml',
        'views/data_management.xml',
        'views/partner.xml',
        'views/researcher_invitation_wizard.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

