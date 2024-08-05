import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    message = os.environ.get('MESSAGE', 'Hello, Welcome to KodeCamp4.0 DevOps Bootcamp!')
    password = os.environ.get('PASSWORD', 'No password set')
    return f"{message}<br>Password: {password}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

