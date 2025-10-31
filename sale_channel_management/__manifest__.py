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
        'security/ir.model.access.csv',
        'views/sale_channel_views.xml',
        'views/sale_channel_menu.xml',
        'views/sale_order_views.xml',

    ],          
    'installable': True,  
    'application': True,  # para que aparezca en Apps

}