# Project Plan

## Project Title

Development of a Dental Tooth Segmentation Prototype Using U-Net and Flask

---

## Dataset

Dataset Name: Tufts Radiographs

Dataset Source: Kaggle

Dataset Link:
https://www.kaggle.com/datasets/manarmaged/tufts-radiographs/data

---

## Dataset Finding

The dataset contains panoramic dental radiographs and bounding box annotations.

The available annotation files contain:

```text
imageID
class
x-min
y-min
width
height
```

No ready-made pixel-level tooth segmentation masks were found.

---

## Project Goal

The goal is to build a complete weak-mask dental segmentation pipeline.

The system will:

1. Load panoramic dental radiographs.
2. Read bounding box annotations.
3. Generate weak binary masks from bounding boxes.
4. Prepare images and weak masks for deep learning.
5. Train a U-Net model for weak-mask segmentation.
6. Evaluate segmentation performance against weak masks.
7. Export the trained model.
8. Deploy the trained model using Flask.
9. Allow the user to upload a new dental radiograph.
10. Display the predicted weak mask and overlay result.

---

## Problem Type

This is a medical image segmentation prototype using weak annotations.

The model performs binary weak-mask segmentation:

```text
Weak target region = 1
Background = 0
```

Important: the weak target region is generated from bounding boxes and is not a manual tooth boundary mask.

---

## Expected Workflow

```text
Dental panoramic X-ray
+
Bounding box CSV
↓
Generate weak binary mask
↓
Image and mask preprocessing
↓
U-Net segmentation model
↓
Predicted weak mask
↓
Model export
↓
Flask web application
↓
Upload new radiograph
↓
Display original image, predicted weak mask, and overlay result
```

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
- Pandas
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

- Weak binary mask generation from bounding boxes
- Annotated images only
- Image size 256 x 256
- Simple U-Net architecture
- Dice coefficient and IoU evaluation
- Flask upload page
- Original image, predicted weak mask, and overlay display

---

## Success Criteria

The project is successful if:

1. The Kaggle Notebook runs without errors.
2. The dataset is loaded correctly.
3. Bounding box annotations are read correctly.
4. Weak binary masks are generated correctly.
5. Images and weak masks are preprocessed correctly.
6. The U-Net model trains successfully.
7. The model produces visible predicted weak masks.
8. The trained model is exported.
9. The Flask app loads the trained model.
10. The user can upload a radiograph.
11. The app displays the predicted weak mask and overlay result.
12. The structure remains suitable for future iHIS integration.
