from flask import Flask, jsonify,render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask_cors import CORS

from datetime import datetime

#*configution
DEBUG=True
#rm -fr .git => delete repo permanently
#npm show bootstrap-vue@* version => return installed packages all version list

#*instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#*enable CORS
cors = CORS(app, resources={r'/*': {'origins': '*'}})


#*connect sqlite3 databa my application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/riade/SQLITE/test.db'
db = SQLAlchemy(app)

#?Book
class Book(db.Model,SerializerMixin):
    id = db.Column(db.Integer,primary_key=True)
    title_book = db.Column(db.String(100),unique=True,nullable=False)
    author_book = db.Column(db.String(100),unique=False,nullable=False)
    is_reading_book = db.Column(db.Boolean,default=False,nullable=False)


class Block(db.Model,SerializerMixin):
    id = db.Column('Block Id',db.Integer,primary_key=True)
    block_number = db.Column('Block Number',db.String(100),unique=False,nullable=False)
    block_miner = db.Column('Block Miner',db.String(100),unique=False,nullable=False)
    created_date = db.Column('Date of Create',db.DateTime,default=datetime.utcnow.strftime('%Y-%d-%m'))
    # time_stamp_unix = use datetime.fromtimestamp method for saving database


#!pingPongView
@app.route('/ping',methods=['GET','POST'])
def pingPongView():
    return jsonify('Ping!')

#!allBookView
@app.route('/books',methods=['GET','POST'])
def allBookView():
    if request.method == 'POST':
        post_data = request.get_json()#JSON.parse(post_data) like
        title = post_data['title']
        author = post_data['author']
        read = post_data['read']
        addedBook = Book(title_book=title,author_book=author,is_reading_book=read)
        db.session.add(addedBook)
        db.session.commit()
        print('Successfully inserted new book data base from vue js')
    #else => first page loading this below code => Book.query.all()
    books = Book.query.all()
    dictdata = [book.to_dict() for book in books]
    return jsonify({'status':'Success','books':dictdata})

#!updateBookView
@app.route('/books/<int:id>',methods=['PUT','DELETE'])
def updateBookView(id):
    if request.method == 'PUT':
        book = Book.query.get(id)
        post_data = request.get_json()
        book.title_book =  post_data['title']
        book.author_book = post_data['author']
        book.is_reading_book = post_data['read']
        db.session.commit()
        print('Successfully Updated Book Data')
    if request.method == 'DELETE':
        deleted_book = Book.query.get(id)
        db.session.delete(deleted_book)
        db.session.commit()
        print('Successfully Deleted Book Data')
    return jsonify({'success_update_book':'success'})

#?__name__ == '__main__'
if __name__ == "__main__":
    db.create_all()
    app.run()