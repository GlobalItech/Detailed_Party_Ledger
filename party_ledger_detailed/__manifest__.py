{
    'name': 'Partner Ledger Detailed',
    'author': 'Itech Resources',
    'company': 'ItechResources',
    'depends': [
                'base',
                'sale',
                'account',
                'account_accountant',      
                ],
    'data': [
            'wizard/wizard.xml',
            'views/report_temp.xml',
            'views/report_call.xml'
            ],
    'installable': True,
    'auto_install': False,
    'price':'20.0',
    'currency': 'EUR',
}
