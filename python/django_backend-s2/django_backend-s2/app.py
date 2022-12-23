from flask import Flask, request
from flask_api import status

app = Flask(__name__)

@app.route('/api')
def status():
    return {'status':'is runnig'}

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9000, debug=True)