from io import BytesIO
from flask import Flask, render_template, request, send_file
#from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/projects/')
def projects():
    return render_template('projects.html')

@app.route('/project_1/')
def project_1():
    return render_template('project_1.html')

@app.route('/project_1_dw/')
def project_1_dw():
    path = 'data/project_1.zip'
    return send_file(path, as_attachment=True)

@app.route('/about/')
def about():
    return render_template('datamaneger.html')

@app.route('/data/')
def data():
    return render_template('datamaneger.html')

@app.route('/data/download')
def download():
    path = 'data/test.txt'
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)