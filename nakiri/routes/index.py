from flask import Blueprint, g

from nakiri.decorators import authentication
from nakiri.models.user import User

blueprint = Blueprint('index', __name__)


@blueprint.route('/')
def index() -> dict:
    return {
        'name': 'Nakiri',
        'version': 1.0
    }


@blueprint.route('/whoami')
@authentication.token_required
def whoami() -> dict:
    user = User.query.filter_by(id=g.token['user']).first()

    return {
        'id':       user.id,
        'username': user.username,
    }
