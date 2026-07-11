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

from services.prediction_service import create_prediction_mask


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
        uploaded_filename = None
        prediction_image = None
        prediction_filename = None
        overlay_image = None
        overlay_filename = None
        prediction_info = None

        if request.method == "POST":
            if "image" not in request.files:
                flash("No image file was uploaded.")
                return redirect(url_for("index"))

            file = request.files["image"]

            if file.filename == "":
                flash("Please choose an image file.")
                return redirect(url_for("index"))

            if not allowed_file(file.filename):
                flash("Invalid file type. Please upload PNG, JPG, or JPEG.")
                return redirect(url_for("index"))

            if not model_exists:
                flash("Model file was not found. Please add the trained Keras model first.")
                return redirect(url_for("index"))

            filename = secure_filename(file.filename)
            upload_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(upload_path)

            prediction_filename = f"prediction_{os.path.splitext(filename)[0]}.png"

            try:
                _, _, prediction_info = create_prediction_mask(
                    image_path=upload_path,
                    output_filename=prediction_filename,
                    threshold=0.03,
                )
            except Exception as error:
                flash(f"Prediction failed: {error}")
                return redirect(url_for("index"))

            uploaded_image = url_for("static", filename=f"uploads/{filename}")
            prediction_image = url_for("static", filename=f"predictions/{prediction_filename}")
            overlay_filename = prediction_info["overlay_filename"]
            overlay_image = url_for("static", filename=f"predictions/{overlay_filename}")
            uploaded_filename = filename

            return render_template(
                "index.html",
                model_exists=model_exists,
                uploaded_image=uploaded_image,
                uploaded_filename=uploaded_filename,
                prediction_image=prediction_image,
                prediction_filename=prediction_filename,
                overlay_image=overlay_image,
                overlay_filename=overlay_filename,
                prediction_info=prediction_info,
            )

        return render_template(
            "index.html",
            model_exists=model_exists,
            uploaded_image=uploaded_image,
            prediction_image=prediction_image,
            overlay_image=overlay_image,
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
