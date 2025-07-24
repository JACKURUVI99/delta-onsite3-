from flask import Flask
import os
Dept = input("enter your dept:")

dept = os.environ.get('DEPT')
app = Flask(__name__)
@app.route('/')
def home():
    return f"Welcome to {dept}"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
