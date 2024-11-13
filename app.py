from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from welcome_route import welcome_bp  # Adjust path if needed
from table_route import table_bp      # Adjust path if needed
from factorial import factorial_bp
from sort import sort_bp
from reverse_string import reverse_bp

app = Flask(__name__, template_folder='C:\\Users\\Admin\\Desktop\\flask_app_test')

# Register the blueprints for other routes
app.register_blueprint(welcome_bp)
app.register_blueprint(table_bp)
app.register_blueprint(factorial_bp)
app.register_blueprint(sort_bp)
app.register_blueprint(reverse_bp)

# Configure the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:duc22bi13085@127.0.0.1:3306/flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the main app
db = SQLAlchemy(app)


# Define the 'students' table model
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    class_name = db.Column(db.String(50), nullable=False)
    mark = db.Column(db.Integer, nullable=False)

# Create a route to initialize the database and create the table
@app.route('/create_table')
def create_table():
    db.create_all()
    return "Table created successfully."


@app.route('/insert_student')
def insert_student():
    # List of multiple students to insert
    students_data = [
        {"name": "John", "class_name": "One", "mark": 80},
        {"name": "Alice", "class_name": "Two", "mark": 90},
        {"name": "Bob", "class_name": "One", "mark": 60},
        {"name": "Charlie", "class_name": "Three", "mark": 50},
    ]
    
    # Loop through the list and add each student
    for student_data in students_data:
        # Check if a student already exists with the same name and class
        existing_student = Student.query.filter_by(
            name=student_data["name"], class_name=student_data["class_name"]
        ).first()
        
        # If the student doesn't exist, insert them
        if not existing_student:
            student = Student(
                name=student_data["name"],
                class_name=student_data["class_name"],
                mark=student_data["mark"]
            )
            db.session.add(student)
    
    # Commit the transaction to save all the unique students
    db.session.commit()
    
    return "Students inserted successfully, duplicates skipped."


@app.route('/update_class')
def update_class():
    # Update the class for students with marks less than 60
    students_to_update = Student.query.filter(Student.mark < 60).all()
    for student in students_to_update:
        student.class_name = "Two"
    db.session.commit()
    return "Class updated for students with marks less than 60."



@app.route('/grouped_students')
def grouped_students():
    # Query students by mark range
    excellent_students = Student.query.filter(Student.mark > 75).all()
    good_students = Student.query.filter(Student.mark.between(60, 75)).all()
    average_students = Student.query.filter(Student.mark < 60).all()

    # Render the students data in HTML tables
    return render_template('students.html', 
                           excellent_students=excellent_students, 
                           good_students=good_students, 
                           average_students=average_students)


@app.route('/')
def hello():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
