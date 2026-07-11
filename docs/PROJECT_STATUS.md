# Project Status

## Repository

```text
Ya7yaZakaria/tooth-segmentation-unet-flask
```

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

- One weak binary mask was generated successfully.
- Original radiograph and generated weak mask were displayed.
- Weak mask overlay was displayed.
- A reusable weak-mask generation function was created.
- The function was tested successfully.
- Annotated image list was prepared.
- Annotated image existence was checked.
- Weak masks were generated for sample images.
- Weak masks were visually reviewed for sample images.
- Phase 3 completion check was performed.

### Phase 4 — Image and Weak Mask Pairing

- Image size was defined as 256 x 256.
- Image-mask loading function was created.
- The loading function was tested successfully.
- X and Y arrays were built.
- Final dataset values were checked.
- Processed image and mask pair were visualized.
- Phase 4 completion check was performed.

## Dataset Finding

The dataset provides bounding box annotations, not ready-made pixel-level tooth segmentation masks.

## Current Project Direction

This project generates weak binary masks from bounding boxes and will train a U-Net weak-mask segmentation prototype.

## Current Notebook Position

```text
Phase 5 — Train / Validation Split
```

## Next Tasks

- Import train_test_split.
- Split X and Y into training and validation sets.
- Confirm train and validation shapes.
- Confirm Phase 5 completion.
