from flask import Blueprint

welcome_bp = Blueprint('welcome', __name__)

@welcome_bp.route('/welcome')
def welcome():
    return """
    <h1>Welcome to Flask Development!</h1>
    <p>This is Labwork 3: Flask/MySQL/API</p>
    """
