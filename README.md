# Development of a Dental Tooth Segmentation System Using U-Net and Flask

This project implements a dental radiograph segmentation workflow using a U-Net deep learning model and a Flask web application.

## Project Overview

The system allows a user to upload a dental radiograph image and receive:

- A predicted weak segmentation mask
- An overlay visualization
- Prediction probability details

The project was developed as an academic assignment for tooth segmentation using U-Net and Flask.

## Dataset

Dataset used:

Kaggle Tufts Radiographs dataset

The dataset contains dental radiograph images and bounding-box annotations.

Important note:

The dataset does not provide manually drawn pixel-level tooth boundary masks. Therefore, bounding-box-derived weak masks were generated and used as training masks for the U-Net model.

## Methodology

The workflow followed these steps:

1. Dataset exploration
2. Annotation analysis
3. Weak mask generation from bounding boxes
4. Image and mask preprocessing
5. Train, validation, and test split
6. U-Net model construction
7. Model training
8. Training curve review
9. Prediction visualization
10. Final model evaluation
11. Model export
12. Flask deployment
13. Upload interface
14. Prediction service
15. Overlay visualization

## Project Structure

tooth-segmentation-unet-flask/
docs/
flask_app/
flask_app/app.py
flask_app/config.py
flask_app/model/unet_weak_mask_segmentation.keras
flask_app/services/prediction_service.py
flask_app/static/uploads/
flask_app/static/predictions/
flask_app/templates/index.html
notebooks/tooth_segmentation_unet_kaggle.ipynb
requirements.txt
README.md

## Main Deliverables

Kaggle Notebook:
notebooks/tooth_segmentation_unet_kaggle.ipynb

Trained Model:
flask_app/model/unet_weak_mask_segmentation.keras

Flask Source Code:
flask_app/app.py
flask_app/config.py
flask_app/services/prediction_service.py
flask_app/templates/index.html

## Local Setup

Use Python 3.11.

Commands:

py -3.11 -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
cd flask_app
python app.py

Open the app at:

http://127.0.0.1:5000

## Application Features

- Upload dental radiograph image
- Run U-Net prediction
- Generate weak segmentation mask
- Generate overlay visualization
- Display prediction details

## Technical Limitation

The model was trained using bounding-box-derived weak masks.

Therefore, the prediction is not a precise anatomical tooth boundary segmentation. It should be interpreted as a weak segmentation/localization output.

## Final Status

The project is ready for final academic submission.
