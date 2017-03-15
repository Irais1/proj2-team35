from flask import Flask, render_template, request, url_for, redirect, url_for
from string import Template
import requests
import os
from beats import mixAudio
from Werkzeug.utils import secure_filename


HTML_TEMPLATE = Template
music_dir = '/home/flask/flaskmedia/static/music'

UPLOAD_FOLDER = '/home/flask/flaskmedia/static/music'
ALLOWED_EXTENSIONS = set(['wav'])
#music_dir2 = '/home/flask/flaskmedia/static/music'
#music_dir3 = '/home/flask/flaskmedia/static/music'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def homepage():
	return render_template("proj2.html")
	
def allowed_file(filename):
	return '.' in filename and \
	filename.rsplit('.',1)[1].lower()in ALLOWED_EXTENSIONS
	
	
@app.route('/',methods = ['GET', 'POST'])	
def upload_file():
	if request.method == 'POST':
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename=='':
		flash('No file selected')
		return redirect (request.url)
	if file and allowed_file(file.filename):
		file_name= secure_file(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return redirect (url_for('uploaded_file',filename = filename))
			
	
@app.route('/')
@app.route('/home')
def index():
	music_files = [f for f in os.listdir(music_dir) if f.endswith('wav')]
	music_files_number = len(music_files)
	return render_template("proj2.html",
               title = 'Home',
               music_files_number = music_files_number,
               music_files = music_files)

	
@app.route('/results', methods = ['GET', 'POST'])
def results():
    return render_template("results.html")
    
def getAudio():
    mixFile = mixAudio()
    return mixFile
app.jinja_env.globals.update(getAudio=getAudio)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port = int (os.getenv('PORT', 8080)), host = os.getenv('IP', '0.0.0.0'))

