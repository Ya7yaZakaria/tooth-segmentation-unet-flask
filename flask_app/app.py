import os
from flask import Flask, render_template
from config import UPLOAD_FOLDER, PREDICTION_FOLDER, MAX_CONTENT_LENGTH, MODEL_PATH

def create_app():
    app = Flask(__name__)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config["PREDICTION_FOLDER"] = PREDICTION_FOLDER
    app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(PREDICTION_FOLDER, exist_ok=True)

    @app.route("/")
    def index():
        model_exists = os.path.exists(MODEL_PATH)
        return render_template("index.html", model_exists=model_exists)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
