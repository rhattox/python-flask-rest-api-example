from flask import Blueprint, request
from ..models.user import User
user = Blueprint('user', __name__)

@user.route('/user/register', methods=['POST'])
def register():
    if request.method == 'POST':
        if request.is_json:
            email = request.json['email']
            password = request.json['password']
            return f'Registred: {email}'
        else:
            return f'It needs to be JSON!!'
    else:
        return f"Method not allowed {request.method}!"