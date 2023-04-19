from flask import Flask, jsonify
import socket

app = Flask(__name__)
request_count = 0

ip_address = socket.gethostbyname(socket.gethostname())

@app.route("/")
def get_host_info():
    global request_count
    request_count += 1
    return jsonify({
        "ip_address": ip_address,
        "request_count": request_count
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
