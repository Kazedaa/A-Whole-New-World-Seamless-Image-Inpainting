import os
from flask import render_template, redirect, send_from_directory, redirect
from flask import current_app, request
from flask import Blueprint
from flaskApp.PatchGANgenerator import inpaint, format

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files or request.files['file'].filename== '':
        return redirect(request.url)
    
    file = request.files['file']
    # Save the uploaded file to a folder on the server
    file.save('flaskApp/images/' + file.filename)
    
    #convert it into the right format
    format(file.filename)

    # Display the uploaded image
    return render_template('upload.html', filename=file.filename)

@main_blueprint.route('/images/<filename>')
def display_image(filename):
    root_dir = current_app.root_path
    return send_from_directory(os.path.join(root_dir, 'images'), filename)

@main_blueprint.route('/result',methods=['POST'])
def result():
    data = request.get_json()[0]
    filename = data['file'][len('http://127.0.0.1:5000/images/'):]
    inpaint(filename , int(data['x']) , int(data['y']))
    return render_template("result.html" , filename=filename)

@main_blueprint.route('/masks/<filename>')
def masked(filename):
    root_dir = current_app.root_path
    return send_from_directory(os.path.join(root_dir, 'masks'), filename)

@main_blueprint.route('/inpainted/<filename>')
def inpainted(filename):
    root_dir = current_app.root_path
    return send_from_directory(os.path.join(root_dir, 'inpainted'), filename)

@main_blueprint.route('/redirect')
def redirect_to_home():
    return redirect('/')