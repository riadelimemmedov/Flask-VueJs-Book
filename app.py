from flask import Flask, jsonify,render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask_cors import CORS

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


#!pingPongView
@app.route('/ping',methods=['GET','POST'])
def pingPongView():
    return jsonify('Ping!')

#!allBookView
@app.route('/books',methods=['GET','POST'])
def allBookView():
    # if request.method == 'POST':
    #     title_book = request.form.get('title_book')
    #     author_book = request.form.get('author_book')
    #     created_book = Book(title_book=title_book,author_book=author_book)
    #     db.session.add(created_book)
    #     db.session.commit()
    #     print('Insert successfully database')
    # return render_template('index.html')
    
    books = Book.query.all()
    dictdata = [book.to_dict() for book in books]
    return jsonify({'status':'Success','books':dictdata})

#?__name__ == '__main__'
if __name__ == "__main__":
    db.create_all()
    app.run()