from flask import Flask, jsonify
import socket

app = Flask(__name__)

ip_address = socket.gethostbyname(socket.gethostname())

@app.route('/')
def get_host_info():
    return jsonify({'host_ip': ip_address})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
