# Phase 20 Completion — Final Submission Packaging

## Status
Completed.

## Goal
Prepare the project for final assignment submission.

## Official Project Title
Development of a Dental Tooth Segmentation System Using U-Net and Flask

## Assignment Deliverables
The project contains the required submission components:

1. Kaggle Notebook
   - notebooks/tooth_segmentation_unet_kaggle.ipynb

2. Trained U-Net Model
   - flask_app/model/unet_weak_mask_segmentation.keras

3. Flask Source Code
   - flask_app/app.py
   - flask_app/config.py
   - flask_app/services/prediction_service.py
   - flask_app/templates/index.html

## Final Application Capability
The Flask application can:
- Load the trained U-Net Keras model.
- Accept uploaded dental radiograph images.
- Preprocess images for model inference.
- Generate predicted weak segmentation masks.
- Generate overlay visualizations.
- Display uploaded image, predicted mask, overlay, and prediction details.

## Dataset Note
The Kaggle Tufts Radiographs dataset provides bounding-box annotations, not manually drawn pixel-level tooth segmentation masks.

Therefore, this project generated bounding-box-derived weak masks and used them to train a U-Net segmentation model.

## Important Limitation
The predicted segmentation does not represent precise anatomical tooth boundaries.

It represents weak segmentation regions learned from bounding-box-derived masks.

## Local Environment
The project was tested locally using:
- Python 3.11.9
- Flask 3.0.3
- TensorFlow 2.16.1
- OpenCV 4.10.0
- NumPy 1.26.4

## Run Instructions
From the project root:

py -3.11 -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
cd flask_app
python app.py

Then open:

http://127.0.0.1:5000

## Final Status
The project is ready for final review and submission packaging.
