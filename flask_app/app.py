import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash

from config import (
    UPLOAD_FOLDER,
    PREDICTION_FOLDER,
    MAX_CONTENT_LENGTH,
    MODEL_PATH,
    ALLOWED_EXTENSIONS,
)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def create_app():
    app = Flask(__name__)
    app.secret_key = "development-secret-key"
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config["PREDICTION_FOLDER"] = PREDICTION_FOLDER
    app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(PREDICTION_FOLDER, exist_ok=True)

    @app.route("/", methods=["GET", "POST"])
    def index():
        model_exists = os.path.exists(MODEL_PATH)
        uploaded_image = None

        if request.method == "POST":
            if "image" not in request.files:
                flash("No image file was uploaded.")
                return redirect(url_for("index"))

            file = request.files["image"]

            if file.filename == "":
                flash("Please choose an image file.")
                return redirect(url_for("index"))

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(save_path)

                uploaded_image = url_for("static", filename=f"uploads/{filename}")

                return render_template(
                    "index.html",
                    model_exists=model_exists,
                    uploaded_image=uploaded_image,
                    uploaded_filename=filename,
                )

            flash("Invalid file type. Please upload PNG, JPG, or JPEG.")

        return render_template(
            "index.html",
            model_exists=model_exists,
            uploaded_image=uploaded_image,
        )

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
