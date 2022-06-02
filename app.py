from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#*configution
DEBUG=True
#rm -fr .git => delete repo permanently

#*instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#*enable CORS
cors = CORS(app, resources={r'/*': {'origins': '*'}})


#*connect sqlite3 databa my application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/riade/SQLITE/test.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title_book = db.Column(db.String(100),unique=True,nullable=False)
    author_book = db.Column(db.String(100),unique=False,nullable=False)
    is_reading_book = db.Column(db.Boolean,default=False,nullable=False)



@app.route('/ping',methods=['GET','POST'])
def pingPongView():
    data = Book('On the Road','Jack Kerouac',False)
    db.session.add(data)
    db.session.commit()
    print('Insert Data Successfully')
    return jsonify('Pong!')

#?__name__ == '__main__'
if __name__ == "__main__":
    db.create_all()
    app.run()