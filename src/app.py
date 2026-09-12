# '/api/V1/details'
# '/api/V1/healthz'
from flask import Flask,jsonify
import datetime;
import socket

app = Flask(__name__)
hostname = socket.gethostname()

@app.route('/api/V1/details')
def hello_world():
    return jsonify({'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'hostname': hostname,
                     'message': 'Hello World', 'status': 'success', 'code': 200,'title':'Flask API'}),200

@app.route('/api/V1/healthz')
def health_check():
    return jsonify({'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'hostname': hostname, 'message': 'Health Check', 'status': 'success', 'code': 200,'title':'Flask API'}),200
if __name__ == '__main__':
    app.run(host="0.0.0.0")