import re
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from flask.json import jsonify
from cnn_model import make_prediction
#from simple_recommender import get_recommendations, api_data
from werkzeug.utils import secure_filename
import os


UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# __name__ tells Flask that this file is the location
# of the module needed to run the server
app = Flask('Recommender App')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/image_upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('download_file', name=filename))
            
            result = make_prediction('uploads/'+filename)
            print(request.args)
            return render_template('results.html',typed= result)
    return render_template('file_upload.html')


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

app.add_url_rule(
    "/uploads/<name>", endpoint="download_file", build_only=True
)


# This is the route that will be used to access the application
@app.route('/')
def hello_world():
    #show_recc = get_recommendations()
    return 'Hello, World!'

# test image path: flask_main/imagetest.png
# This is the route that will be used to access the application
@app.route('/result')
def recommender():
    #result = make_prediction('uploads/imagetest.png')
    result = request.args.get('result')
    print(request.args)
    return render_template('results.html',typed= result)

@app.route('/new')
def index():
    return render_template('site.html')

@app.route('/api')
def api_all():
    #jsonify(api_data)
   
    return  'API page'


# This is the route that will be used to access the application
# executed after using python app.py
if __name__ == "__main__":
    app.run(debug=True, port=5000)
    
    # For deployment, use the following line
    #app.run(host='0.0.0.0', port=5000, debug=True)
