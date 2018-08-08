import os,json
from flask import Flask,render_template,abort
app = Flask(__name__)
path = '/home/shiyanlou/files/'



@app.route('/')
def index():

    return render_template('index.html')
# @app.errorhandler(404)
@app.route('/files/<filename>')
def file(filename):
    # print(os.getcwd)
    filename = filename + '.json'
    with open(path+filename,'r') as f:
                data = json.load(f)
    return render_template('file.html',filename=filename,data=data)
 
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()