import os,json
from datetime import *
from flask import Flask,render_template,abort
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
client = MongoClient('127.0.0.1',27017)
db_mongo = client.shiyanlou
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)
class File(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('files',lazy='dynamic'))
    content = db.Column(db.Text)

    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content
    def __repr__(self):
        return '<File %r>'% self.title
    def add_tag(self,tag_name):
        rec = db_mongo.tagrec.find_one({'id':self.id})
        if rec == None:
            new = {'id':self.id,'tags':[tag_name]}
            db_mongo.tagrec.insert_one(new)
        else:
            list = rec['tags']
            list.append(tag_name)
            db_mongo.tagrec_update_one({'id':self.id},{'$set':{'tags':list}})
    def remove_tag(self,tag_name):
        rec = db_mongo.tagrec.find_one({'id':self.id})
        if rec == None:
            return
        else:
            list = rec['tags']
            list.remove(tag_name)
            db_mongo.tagrec.update_one({'id':self.id},{'$set':{'tags':list}})

    def tags(self):
        rec = db_mongo.tagrec.find_one({'id':self.id})
        if rec == None:
            return None
        else:
            return rec['tags']
class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return '<Category %r>'% self.name

@app.route('/')
def index():
    files_list = File.query.all()
    return render_template('index.html',files_list=files_list)
@app.route('/files/<file_id>')
def file(file_id):
    files_dict = File.query.filter_by(id = file_id).first()
    if files_dict == None:
        abort(404) 
    else:
        return render_template('file.html',files_dict=files_dict)
 
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()
