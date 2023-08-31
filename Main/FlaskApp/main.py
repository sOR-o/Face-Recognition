# from flask import Flask, render_template, request, flash
# from werkzeug.utils import secure_filename
# import os



# UPLOAD_FOLDER = 'static/uploads'  # Store uploaded images in a separate folder
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # Image file extensions

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['SECRET_KEY'] ='\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")

# @app.route("/check", methods=["POST"])
# def check():
#     if 'file' not in request.files:
#         flash('No file part')
#         return "Error"
    
#     file = request.files['file']
#     if file.filename == '':
#         flash('No selected file')
#         return "Error"

#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)
        
#         # Perform face recognition and detection on the uploaded image
#         # Modify the following line based on your face_recognition_and_detection_function
#         # result = face_recognition_and_detection_function(file_path)
        
#         return render_template("results.html", result=result)

# if __name__ == '__main__':
#     app.run(debug=True)


# ***********************************************************

from flask import Flask, render_template, request, flash

from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] ='\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'



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
        if 'file' not in request.files:
            flash('No file part')
            return "Error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "Error"

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            takeAttendance()
            return render_template("result.html")
    return render_template("about.html")

app.run(debug=True)



