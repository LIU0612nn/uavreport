from flask import Flask, request, send_file, render_template
import os
from werkzeug.utils import secure_filename
from analyzer.log_parser import parse_csv
from analyzer.report_generator import generate_report

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
REPORT_FOLDER = './reports'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded'
    file = request.files['file']
    if file.filename == '':
        return 'No file selected'
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    if filename.endswith('.csv'):
        data = parse_csv(filepath)
        report_path = os.path.join(REPORT_FOLDER, 'flight_report.png')
        generate_report(data, report_path)
        return send_file(report_path, as_attachment=True, attachment_filename='flight_report.png')
    else:
        return 'Please upload a .csv file'

if __name__ == '__main__':
    app.run(debug=True)