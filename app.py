from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Load CSV data
def load_csv():
    df = pd.read_csv('data.csv')
    return df

@app.route('/')
def index():
    df = load_csv()
    return render_template('index.html', data=df.to_dict(orient='records'))

@app.route('/tag', methods=['POST'])
def tag():
    row_id = request.form.get('row_id')
    author = request.form.get('author')
    sql_path = request.form.get('sql_path')
    # Process the data as needed
    print(f"Row ID: {row_id}, Author: {author}, SQL Path: {sql_path}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
