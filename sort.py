from flask import Blueprint, request
sort_bp = Blueprint('sort',__name__)

@sort_bp.route('/sort')
def sort_numbers():
    #Get the 'numbers' query parameter from teh url
    number_str = request.args.get('numbers', '')
    
    #if the numbers parameter exists, process it
    if number_str:
        try:
            #Split the number by comas and covert to a list of integers
            numbers = [int(num) for num in number_str.split(',')]
            #Sort the list in ascending order
            numbers.sort()
            return f"Sorted numbers {numbers}"
        except ValueError:
            return "Invalid input, please make sure all values are integers"
    else:
        return "Please provide a list of numbers using the 'numbers' query parameter" 