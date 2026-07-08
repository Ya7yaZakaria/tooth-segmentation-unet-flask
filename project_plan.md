# Project Plan

## Project Title

Development of a Dental Tooth Segmentation System Using U-Net and Flask

---

## Dataset

Dataset Name: Tufts Radiographs

Dataset Source: Kaggle

Dataset Link:
https://www.kaggle.com/datasets/manarmaged/tufts-radiographs/data

The dataset contains panoramic dental radiographs and associated annotations for dental AI research.

---

## Project Goal

The goal is to build a complete dental tooth segmentation pipeline.

The system will:

1. Load panoramic dental radiographs.
2. Prepare images and masks for deep learning.
3. Train a U-Net model for tooth segmentation.
4. Evaluate segmentation performance.
5. Export the trained model.
6. Deploy the trained model using a Flask web application.
7. Allow the user to upload a new dental radiograph.
8. Display the predicted tooth segmentation result.

---

## Problem Type

This is a medical image segmentation task.

The model performs binary semantic segmentation:

- Tooth pixels = 1
- Background pixels = 0

---

## Expected Workflow

Dental panoramic X-ray  
↓  
Image preprocessing  
↓  
U-Net segmentation model  
↓  
Predicted tooth mask  
↓  
Model export  
↓  
Flask web application  
↓  
Upload new radiograph  
↓  
Display original image, predicted mask, and overlay result  

---

## Main Deliverables

1. Kaggle Notebook
2. Trained U-Net Model
3. Flask Source Code

Recommended additional deliverables:

1. README.md
2. CHANGELOG.md
3. Screenshots
4. Short report
5. Demo video if required

---

## Tools Used

### Training

- Kaggle Notebook
- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Matplotlib
- Scikit-learn

### Deployment

- VS Code
- Flask
- HTML
- Bootstrap 5 optional
- TensorFlow / Keras
- OpenCV
- NumPy

---

## Architecture Mindset

The project should remain simple for assignment delivery, but should not be disposable.

The Flask app should separate:

1. Web route logic
2. AI prediction service
3. Image preprocessing utilities
4. Model storage
5. Prediction output storage

---

## Future iHIS Integration Plan

This module should later be integrable into:

- iHIS Dentistry Module
- Dental Imaging workflow
- AI Dental Assistant
- Patient Dental Record
- Dentist Dashboard

The model should not directly modify the database.

Future iHIS integration should save segmentation results as AI-generated outputs linked to dental image records and reviewed by a dentist before clinical use.

---

## Initial Scope

The first version will include:

- Binary tooth segmentation
- Image size 256 x 256
- Simple U-Net architecture
- Dice coefficient and IoU evaluation
- Flask upload page
- Original image, predicted mask, and overlay display

---

## Success Criteria

The project is successful if:

1. The Kaggle Notebook runs without errors.
2. The dataset is loaded correctly.
3. Images and masks are preprocessed correctly.
4. The U-Net model trains successfully.
5. The model produces visible tooth segmentation masks.
6. The trained model is exported.
7. The Flask app loads the trained model.
8. The user can upload a radiograph.
9. The app displays the predicted segmentation result.
10. The structure remains suitable for future iHIS integration.
