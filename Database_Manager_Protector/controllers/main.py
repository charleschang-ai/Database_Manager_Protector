from odoo.addons.web.controllers.database import Database
import odoo
from odoo import http
from odoo.http import request


class DatabasePlus(Database):

    @http.route('/web/database/manager', type='http', auth="none")
    def manager(self, **kw):

        master_pwd = kw.get('master_pwd')
        if not master_pwd:
            return request.render('Database_Manager_Protector.template_db_manager_masterpwd')

        odoo.service.db.check_super(master_pwd)
        if request.db:
            request.env.cr.close()
        return self._render_template()

    @http.route('/web/database/selector', type='http', auth="none")
    def selector(self, **kw):

        master_pwd = kw.get('master_pwd')
        if not master_pwd:
            return request.render('Database_Manager_Protector.template_db_manager_masterpwd')

        odoo.service.db.check_super(master_pwd)
        if request.db:
            request.env.cr.close()
        return self._render_template()


