from flask import Blueprint, jsonify, session, request
from app.models import User, db, Project, Section 
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime

today = datetime.today(); 
auth_routes = Blueprint('auth', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


@auth_routes.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        print("here")
        return current_user.to_dict()
    return {'errors': ['Unauthorized']}


@auth_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    form = LoginForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # Add the user to the session, we are logged in!
        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/logout')
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User(
            full_name=form.data['fullname'],
            email=form.data['email'],
            password=form.data['password']
        )
        db.session.add(user)
        db.session.commit()  
        #Inventory 
        project3 = Project( 
            title='Inventory',
            description='This is a test description',
            owner_id=user.id,
            type = 1,
            created_at = today,
            updated_at = today
            )

        #Workers
        project4 = Project(
            title='Employees', 
            description='This is a test description',
            owner_id=user.id,
            type = 2,
            created_at = today,
            updated_at = today
            )
        
        #To DO  
        project5 = Project(
            title='To Do',
            description='This is a test description', 
            owner_id=user.id,
            type = 3, 
            created_at = today,
            updated_at = today
            )  

        db.session.add(project3)
        db.session.add(project4)  
        db.session.add(project5)
        project3.project_members.append(user)
        project4.project_members.append(user)  
        project5.project_members.append(user)  
        db.session.commit() 
        #Inventory 
        section9 = Section(
            project_id=project3.id,
            board_column=0,
            tasks_order=[],
            title='On Shelf',
            created_at = today,
            updated_at = today
            )
        section10 = Section(
            project_id=3,
            board_column=1,
            tasks_order=[],
            title='In Transit',
            created_at = today,
            updated_at = today
            ) 
        section11 = Section(
            project_id=project3.id,
            board_column=2,
            tasks_order=[],
            title='Production',
            created_at = today,
            updated_at = today
            )
        section12 = Section(
            project_id=project3.id,
            board_column=3,
            title='Broken',
            tasks_order=[],
            created_at = today,
            updated_at = today
            )

        #Employees 
        section13 = Section(
            project_id=project4.id,
            board_column=0,
            tasks_order=[],
            title='Available',
            created_at = today,
            updated_at = today
            )
        section14 = Section(
            project_id=project4.id,
            board_column=1,
            tasks_order=[],
            title='UnActive',
            created_at = today,
            updated_at = today
            )
        section15 = Section(
            project_id=project4.id,
            board_column=2,
            tasks_order=[],
            title='Trainees',
            created_at = today,
            updated_at = today
            ) 
        section16 = Section(
            project_id=project4.id,
            board_column=3,
            title='Applicants',
            tasks_order=[],
            created_at = today,
            updated_at = today
            )  
    
        #To Do 
        section17 = Section(
            project_id=project5.id,
            board_column=0,
            tasks_order=[],
            title='Recently assigned', 
            created_at = today,
            updated_at = today
            )
        section18 = Section(
            project_id=project5.id,
            board_column=1,
            tasks_order=[],
            title='Do today', 
            created_at = today,
            updated_at = today
            )
        section19 = Section(
            project_id=project5.id,
            board_column=2,
            tasks_order=[],
            title='Do next week', 
            created_at = today,
            updated_at = today
            )
        section20 = Section(
            project_id=project5.id,
            board_column=3, 
            title='Do later',
            tasks_order=[],
            created_at = today,
            updated_at = today
            ) 

        db.session.add(section9)  
        db.session.add(section10)
        db.session.add(section11)
        db.session.add(section12)
        db.session.add(section13)
        db.session.add(section14)
        db.session.add(section15)
        db.session.add(section16)
        db.session.add(section17) 
        db.session.add(section18)
        db.session.add(section19)
        db.session.add(section20) 
        db.session.commit()
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': ['Unauthorized']}, 401
