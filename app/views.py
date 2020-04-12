from app import app
from app.covid import Covid,File
from flask import Flask, jsonify, send_file, request, redirect, url_for, render_template
import os
from os import listdir
from os.path import isfile, join
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'app/data/'
app.secret_key = '/\x8c\x9a\xadT\xdf\x1b\xf0\r\x87\xa9\x1aV\xd5\x04\xbc\x0c\xff|\x15\x0edmd'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
MODEL_PATH = 'app/models/covid_model.h5'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

file_obj=File()
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def index():
    # Main page
    # heatmap_path='app/static/heatmap/'
    # heatmap_files=[f for f in listdir(heatmap_path) if isfile(join(heatmap_path, f))]
    # [os.remove(heatmap_path+heatmap_file) for heatmap_file in heatmap_files]
    return render_template('index.html')

@app.route('/heatmap.html', methods=['GET'])
def heatmap():
    FILE=file_obj.get_filename()
    return render_template('heatmap.html',image_path=FILE)


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message': 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file = str(UPLOAD_FOLDER+filename)
            if isfile(file) == False:
                return jsonify({'message': 'File not found'})
            preds = Covid(file, MODEL_PATH).covid_predict()
            file_obj.__init__(filename)
            os.remove(file)
            return preds
        else:
            resp = jsonify(
                {'message': 'Allowed file types are jpg, jpeg, png'})
            resp.status_code = 400
            return resp
    return redirect('/')
