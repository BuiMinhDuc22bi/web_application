from flask import Blueprint
import math
factorial_bp = Blueprint('factorial',__name__) 

@factorial_bp.route('/factorial/<int:num>')
def factorial(num):
    #calculate the factorial of the number
    result = math.factorial(num)
    return f"The factorial of {num} is {result}"


