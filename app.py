from flask import Flask, request,render_template,jsonify
import os
import subprocess

app = Flask(__name__)


UPLOAD_FOLDER1 = '/home/murali/Documents/db_automate/1.0.0/users'

UPLOAD_FOLDER2 = '/home/murali/Documents/db_automate/1.0.0/services'

UPLOAD_FOLDER3 = '/home/murali/Documents/db_automate/1.0.0/transactions'

UPLOAD_FOLDER4 = '/home/murali/Documents/db_automate/1.0.0/user_plans'


@app.route('/run_liquibase_update', methods=['POST'])
def run_liquibase_update():
    try:
        result = subprocess.run(['liquibase', 'update'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return jsonify({"status": "success", "output": result.stdout.decode('utf-8')})
    
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "error", "output": e.stderr.decode('utf-8')}), 500


@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload1', methods=['POST'])
def upload_file1():
    files = request.files.getlist('files')   
    for file in files:
        if file:
            filename = file.filename
            file_path = os.path.join(UPLOAD_FOLDER1, filename)
            file.save(file_path)
    return render_template('upload.html',data1 = "success")

@app.route('/upload2', methods=['POST'])
def upload_file2():
    files = request.files.getlist('files')   
    for file in files:
        if file:
            filename = file.filename
            file_path = os.path.join(UPLOAD_FOLDER2, filename)
            file.save(file_path)
    return render_template('upload.html',data2 = "success")

@app.route('/upload3', methods=['POST'])
def upload_file3():
    files = request.files.getlist('files')   
    for file in files:
        if file:
            filename = file.filename
            file_path = os.path.join(UPLOAD_FOLDER3, filename)
            file.save(file_path)
    return render_template('upload.html',data3 = "success")

@app.route('/upload4', methods=['POST'])
def upload_file4():
    files = request.files.getlist('files')   
    for file in files:
        if file:
            filename = file.filename
            file_path = os.path.join(UPLOAD_FOLDER4, filename)
            file.save(file_path)
    return render_template('run_update.html',data4 = "success")

if __name__ == "__main__":
    app.run(debug=True)
