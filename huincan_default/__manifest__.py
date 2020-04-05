# -----------------------------------------------------------------------------
#
#    Copyright (C) 2020  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
{
    'name': 'huincan',
    'version': '13.0.0.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Default Application',
    'summary': 'Customization for huincan',
    'author': 'jeo Software',
    'depends': [
        # basic applications
        'sale_management',
        'purchase',
        'mrp',
        'project',

        # minimum modules for argentinian localizacion + utilities + fixes
        #'standard_depends_ee',
    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    #
    # Here begins docker-odoo-environment manifest
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    'limit_request': '8196',
    'limit_memory_soft': '640000000',
    'limit_memory_hard': '760000000',
    'limit_time_cpu': '60',
    'limit_time_real': '120',

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'license': 'EE',

    # port where odoo starts serving pages
    'port': '8069',

    # list of url repos to install in the form 'repo-url directory'
    'git-repos': [
        'https://github.com/jobiols/cl-huincan.git',

        'https://github.com/jobiols/odoo-addons.git',
        'https://github.com/ingadhoc/odoo-argentina.git',
        'https://github.com/ingadhoc/argentina-sale.git',
        'https://github.com/ingadhoc/account-financial-tools.git',
        'https://github.com/ingadhoc/account-payment.git',
        'https://github.com/ingadhoc/miscellaneous.git',
        'https://github.com/ingadhoc/argentina-reporting.git',
        'https://github.com/ingadhoc/reporting-engine.git',
        'https://github.com/ingadhoc/aeroo_reports.git',
        'https://github.com/ingadhoc/sale.git',
        'https://github.com/ingadhoc/product.git',
        'https://github.com/ingadhoc/stock.git',
        'https://github.com/ingadhoc/account-invoicing.git',
        'https://github.com/ingadhoc/patches.git',
        'https://github.com/ingadhoc/multi-company.git',

        'https://github.com/oca/partner-contact.git',
        'https://github.com/oca/web.git',
        'https://github.com/oca/server-tools.git',
        'https://github.com/oca/social.git',
        'https://github.com/oca/server-ux.git',
        'https://github.com/oca/server-brand.git',
        'https://github.com/oca/manufacture.git',
        'https://github.com/oca/manufacture-reporting.git',
        'https://github.com/oca/management-system.git',
        'https://github.com/oca/sale-workflow.git',
        'https://github.com/oca/stock-logistics-warehouse.git',
        'https://github.com/oca/stock-logistics-reporting.git',
        'https://github.com/oca/stock-logistics-workflow.git',
        'https://github.com/oca/queue.git',
        'https://github.com/oca/operating-unit.git',
        'https://github.com/oca/multi-company.git'
    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo jobiols/odoo-ent:13.0e',
        'postgres postgres:10.1-alpine',
        'nginx nginx'
    ]
}
