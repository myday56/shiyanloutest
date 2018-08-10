import os,json
from flask import Flask,render_template,abort
app = Flask(__name__)
path = '/home/shiyanlou/files/'
files_list = os.listdir(path)
files_dict = {}
for files in files_list:
	with open(path+files) as f:
		filename = files.split('.')[0]
		files_dict[filename] = json.loads(f.read())


@app.route('/')
def index():

    return render_template('index.html',files_dict=files_dict)
@app.route('/files/<filename>')
def file(filename):
    if filename not in files_dict:
        abort(404)	
    return render_template('file.html',filename=filename,files_dict=files_dict)
 
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()