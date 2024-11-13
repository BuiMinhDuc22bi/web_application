from flask import Blueprint , render_template

table_bp = Blueprint('table', __name__)

@table_bp.route('/table')
def table():
    # Define data to display in the table
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
        {"name": "David", "age": 28}
    ]
    return render_template("table.html", data=data)
