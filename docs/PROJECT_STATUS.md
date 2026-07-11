# Project Status

## Repository

Ya7yaZakaria/tooth-segmentation-unet-flask

## Completed

### Phase 0 — Project Setup

- Project folder created.
- Git repository initialized.
- GitHub repository connected.
- Initial documentation files created.
- Initial folder structure created.

### Phase 1 — Dataset Exploration

- Kaggle Notebook created.
- Tufts Radiographs dataset accessed.
- Dataset folder structure inspected.
- Training and testing image folders identified.
- Bounding box CSV annotation files identified.
- CSV files loaded.
- Sample dental radiographs displayed.
- Bounding boxes visualized.
- Class distribution analyzed.
- Confirmed that no ready-made pixel-level tooth masks were found.

### Phase 2 — Understanding Dental Imaging and Segmentation

- Classification, detection, and segmentation were clarified.
- Bounding boxes were identified as detection-style annotations.
- U-Net was confirmed to require image-mask pairs.
- The project direction was defined as a weak-mask segmentation prototype.

### Phase 3 — Weak Binary Mask Generation

- Weak binary masks were generated from bounding boxes.
- A reusable weak-mask generation function was created.
- Weak masks were visually reviewed.
- Phase 3 completion check was performed.

### Phase 4 — Image and Weak Mask Pairing

- Image size was defined as 256 x 256.
- Image-mask loading function was created.
- X and Y arrays were built.
- Final image-mask pair values were checked.
- Phase 4 completion check was performed.

### Phase 5 — Preprocessing

- Radiographs and masks were converted into model-ready tensors.
- Images were normalized to 0 to 1.
- Masks were confirmed as binary values.
- Final tensor shapes were verified.

### Phase 6 — Train / Validation / Test Split

- Dataset was split into training, validation, and test sets.
- Split strategy was approximately 70 / 15 / 15.
- Final split shapes were verified.

### Phase 7 — U-Net Architecture Understanding

- U-Net task was confirmed.
- Main U-Net components were confirmed.
- Phase 7 completion check was performed.

### Phase 8 — Build U-Net Model

- TensorFlow and Keras layers were imported.
- Convolution block was defined.
- U-Net architecture was built.
- Model summary was displayed.
- Model input and output shapes were verified.

### Phase 9 — Loss Functions and Metrics

- Dice coefficient was defined.
- IoU metric was defined.
- Dice loss was defined.
- U-Net model was compiled successfully.

## Dataset Finding

The dataset provides bounding box annotations, not ready-made pixel-level tooth segmentation masks.

## Current Project Direction

This project generates weak binary masks from bounding boxes and trains a U-Net weak-mask segmentation prototype.

## Current Notebook Position

Phase 10 — Model Training

## Next Tasks

- Train the compiled U-Net model.
- Use training data for learning.
- Use validation data for monitoring.
- Add EarlyStopping.
- Add ModelCheckpoint.
- Save the best model checkpoint.

## Phase 10–14 Documentation Update

The Kaggle training and model export workflow has been completed.

Completed items:
- Phase 10 — U-Net model training
- Phase 11 — Training curves review
- Phase 12 — Prediction visualization
- Phase 13 — Final evaluation
- Phase 14 — Model export

Artifacts added:
- notebooks/tooth_segmentation_unet_kaggle.ipynb
- flask_app/model/unet_weak_mask_segmentation.keras

Important technical note:
The model was trained using bounding-box-derived weak masks because the dataset does not provide true pixel-level segmentation masks.
