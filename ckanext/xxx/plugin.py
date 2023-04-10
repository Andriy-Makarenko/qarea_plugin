from flask import Blueprint
import ckan.plugins as plugins
import ckan.plugins.toolkit as tk


header = Blueprint('users', __name__)

@header.route('/users/datasets/')
def users_datasets():
        if  tk.h.check_access('sysadmin'):
            return tk.render('users_datasets.html', {'request': tk.request})
        raise tk.NotAuthorized


class XxxPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)

    # IConfigurer
    def update_config(self, config_):
        tk.add_template_directory(config_, 'templates')
        tk.add_public_directory(config_, 'public')
        tk.add_resource('assets', 'xxx')

    # IBlueprint
    def get_blueprint(self):
        return [header]
