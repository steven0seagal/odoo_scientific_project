
{
    'name': 'Scientific Project Manager',
    'version': '15.0.1.0.0',
    'summary': 'Comprehensive Scientific Project Management System',
    'sequence': -99,
    'description': """
        Scientific Project Manager
        ==========================

        A comprehensive system for managing scientific research projects, including:
        - Project and experiment tracking
        - Publication management
        - Data management and versioning
        - Partner and collaborator management
        - Equipment and reagent inventory
        - Task management and scheduling
        - Role-based access control
        - Document management

        Features:
        - Multi-level security with role-based access
        - Computed fields for better insights
        - Data validation and constraints
        - Email notifications and activity tracking
        - Comprehensive reporting
    """,
    'category': 'Project',
    'author': 'Scientific Project Team',
    'website': 'www.example.com',
    'license': 'LGPL-3',
    'depends': ['mail', 'base'],
    'data': [
        # Security
        'security/security.xml',
        'security/ir.model.access.csv',

        # Data
        'data/mail_templates.xml',
        'data/automated_actions.xml',

        # Views
        'views/dashboard.xml',
        'views/project.xml',
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
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

