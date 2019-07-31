
from flask import Blueprint

course = Blueprint('course',__name__, url_prefix='/courses')


@course.route('/')
def index():

    return render_template('courses.html')

