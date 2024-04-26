from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Service A!"

@app.route('/connect-b')
def connect_service_b():
    response = requests.get("http://service-b:5001")
    return f"Service A received: {response.text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
