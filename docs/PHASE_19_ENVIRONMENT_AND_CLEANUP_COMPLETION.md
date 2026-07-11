# Phase 19 Completion — Local Environment and Cleanup

## Status
Completed.

## Goal
Clean up the local development environment and confirm that the Flask application can run correctly after Phase 17 and Phase 18.

## What was done
- Created a Python 3.11 virtual environment for the project.
- Installed Flask, TensorFlow, OpenCV, NumPy, Pillow, and Werkzeug.
- Confirmed OpenCV imports successfully.
- Confirmed TensorFlow imports successfully.
- Confirmed the Flask application runs locally.
- Confirmed image upload works.
- Confirmed predicted mask generation works.
- Confirmed overlay visualization works.
- Updated .gitignore to ignore the local .venv/ folder.

## Important environment note
TensorFlow did not work with Python 3.14. The project was tested successfully using Python 3.11.9 inside a virtual environment.

## Local test commands

py -3.11 -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
python -c "import cv2; print('cv2 ok', cv2.__version__)"
python -c "import tensorflow as tf; print('tensorflow ok', tf.__version__)"
cd flask_app
python app.py

## Flask output status
The application successfully displays:
- Uploaded image
- Predicted mask
- Overlay visualization
- Prediction probability details

## Current capability
The Flask application now meets the core assignment demo requirement:
upload a dental radiograph, run the trained U-Net model, generate a weak segmentation mask, and display an overlay visualization.

## Technical limitation
The prediction is based on a weakly supervised U-Net model trained with bounding-box-derived masks, not manually drawn tooth boundary masks.
