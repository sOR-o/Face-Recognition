from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def takeAttendance():
    pass


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/check", methods=["GET", "POST"])
def check():
    if request.method == "POST":
        # return "POST request is here"
        if 'file' not in request.files:
            flash('No file part')
            # return redirect(request.url)
            return "Error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)      # Handle this by importing redirect
            return "Error"

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # takeAttendance()
            return render_template("index.html")
    return render_template("about.html")

app.run(debug=True)
