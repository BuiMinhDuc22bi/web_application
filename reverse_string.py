from flask import Blueprint

reverse_bp = Blueprint('reverse', __name__)

@reverse_bp.route('/reverse_string/<string:text>')
def reverse_string(text):
    #Reverse the String 
    reverse_text = text[::-1]
    return f"Reversed string: {reverse_text}"
