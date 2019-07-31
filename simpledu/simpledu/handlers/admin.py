from flask import Blueprint

admin = Blueprint('admin',__name__, url_prefix='/courses')

@admin.route('/admin')
def admin_index():

    return 'admin'

