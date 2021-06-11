from flask import Blueprint, current_app, render_template

from bdauth.auth import login_required


bp = Blueprint('debug', __name__, url_prefix='/debug')


@bp.route("/")
@login_required
def item(item="None"):
    return 'debug'
