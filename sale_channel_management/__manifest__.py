{
    'name': 'Sale channel Managment',
    'version': '1.0',
    'author': 'Ramiro, Alfredo, Manu',
    'category': 'Sales',
    'depends': [
        'base',
        'sale_management',
        'stock',
        'account'],
    'data': [
        'views/sale_channel_views.xml',
        'views/sale_channel_menu.xml',
    ],          
    'installable': True,  
    'application': True,  # para que aparezca en Apps

}