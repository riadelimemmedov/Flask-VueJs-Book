from flask import Flask, jsonify
from flask_cors import CORS

#*configution
DEBUG=True
#rm -fr .git => delete repo permanently

#*instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#*enable CORS
cors = CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/ping',methods=['GET'])
def pingPongView():
    return jsonify('Pong!')

if __name__ == "__main__":
    app.run()