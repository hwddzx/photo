from flask import blueprints

blog_bp = blueprints.Blueprint('blog', __name__)

from . import auth_views
from . import views
