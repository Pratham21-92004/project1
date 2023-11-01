# import all libraries
from io import BytesIO
from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy

# initialize flask and create sqlite database
app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY _TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create datatable
class upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.column(db.String(50))
    data = db.column(db.LargeBinary)

# create index function for upload and return file
@app.route('/', methods=['GET', 'POST'])
def index():
        if request.methode=='POST':
            file = request.files['file']
            upload = upload(filename=file.filename, data=file.read())
            db.session.add(upload)
            db.session.commit()
            return f'Uploaded: {file.filename}'
            return render_template('index.html')
#create download function for dounload files
@app.route('/download/<upload_id>')
def download(upload_id):
        upload = upload.query.filter_by(id=upload_id).first()
        return send_file(BytesIO(upload.data),
                         download_name=upload.filename, as_attachment=True)

if _name== "main_":
        app.run()