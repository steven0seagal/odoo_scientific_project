
{
    'name' : 'Scientific Project Manager',
    'version' : '15.0.1.0.0',
    'summary' : 'Scientific Project Manager',
    'sequence' : -99,
    'description' : 'Scientific Project Manager',
    'category' : 'Project',
    'website' : 'www.example.com',
    'depends' : ['mail','base'],
    'data' : [
        'security/security.xml',  # Must be loaded before ir.model.access.csv
        'security/ir.model.access.csv',
        'views/project.xml',
        'views/task.xml',
        'views/document.xml',
        'views/experiment.xml',
        'views/researcher.xml',
        'views/equipment.xml',
        'views/reagents.xml',
        'views/schedule.xml',
    ],
    'demo' : [],
    'qweb' : [],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}

