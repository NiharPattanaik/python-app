from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/info')
def info():
    return jsonify(
        {
            'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'hostname' : socket.gethostname(),
            'message': 'You are doing great, human!!!, Wow its working',
            'Deployed On': 'Kubernetes'

        }
    )


@app.route('/api/v1/healthz')
def healthz():
    return jsonify(
        {'status': 'UP'}
    ), 200

# main driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0")
