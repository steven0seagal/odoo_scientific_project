
{
    'name': 'Scientific Project Manager',
    'version': '15.0.2.1.0',
    'summary': 'Complete project management for scientific research institutions',
    'sequence': -99,
    'description': """
Scientific Project Manager
==========================
A comprehensive Odoo application for managing scientific research projects, experiments,
laboratory equipment, publications, and research data.

Key Features:
- Project lifecycle management with tracking and collaboration
- Experiment workflow following the scientific method
- Task management with multi-researcher assignment
- Publication tracking and management
- Research data management with version control
- Equipment and reagent inventory management
- Resource scheduling with conflict detection
- Partner and collaborator management
- Role-based access control (Manager, PI, User, Viewer)
- Document management with confidentiality levels
    """,
    'category': 'Project',
    'website': 'https://github.com/steven0seagal/odoo_scientific_project',
    'depends': ['mail', 'base'],
    'data': [
        # Security
        'security/security.xml',
        'security/ir.model.access.csv',

        # Views
        'views/menu.xml',
        'views/project.xml',
        'views/task.xml',
        'views/experiment.xml',
        'views/researcher.xml',
        'views/document.xml',
        'views/equipment.xml',
        'views/reagents.xml',
        'views/schedule.xml',
        'views/publication.xml',
        'views/data_management.xml',
        'views/partner.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

