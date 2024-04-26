from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Service B!"

@app.route('/connect-c')
def connect_service_c():
    response = requests.get("http://service-c:5002")
    return f"Service B received: {response.text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
