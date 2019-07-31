from datetime import datetime
from flask import Flask, render_template
from simpledu.models import db, Course
from simpledu.config import configs
from flask_migrate import Migrate
def create_app(config):

    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    Migrate(app,db)
    register_blueprints(app)
    return app

def register_blueprints(app):
    from simpledu.handlers import front,course,admin
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)

if __name__ == '__main__':
    app.run()

