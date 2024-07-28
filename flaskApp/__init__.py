import os
import shutil
from flask import Flask
from flaskApp.routes import main_blueprint

def App():
    #create new folders
    os.makedirs(os.path.join('flaskApp','images'),exist_ok=True)
    os.makedirs(os.path.join('flaskApp','inpainted'),exist_ok=True)
    os.makedirs(os.path.join('flaskApp','masks'),exist_ok=True)

    app = Flask(__name__)
    app.register_blueprint(main_blueprint)

    return app


