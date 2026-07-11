# Project Memory

## Project

Tooth Segmentation Using U-Net and Flask

## Repository

```text
Ya7yaZakaria/tooth-segmentation-unet-flask
```

## Main Decision

The selected Tufts Radiographs dataset provides bounding box annotations, not ready-made pixel-level tooth segmentation masks.

Therefore, the project will generate weak binary masks from bounding boxes and train a U-Net weak-mask segmentation prototype.

## Correct Wording

Use:

```text
weak binary masks
pseudo masks
weak-mask segmentation prototype
bounding-box-derived masks
```

Avoid:

```text
true manual tooth segmentation masks
ground truth tooth masks
clinical tooth boundary segmentation
```

## Dataset Structure

```text
TUFTS/
├── Radiographs/
│   ├── training_images/
│   └── testing_images/
└── bboxes/
    ├── trainBoundryBoxes.csv
    └── testBoundryBoxes.csv
```

## Annotation Columns

```text
imageID
class
x-min
y-min
width
height
```

## Current Status

Phase 0 completed.

Phase 1 dataset exploration completed in Kaggle.

Current next step:

```text
Phase 2 — Generate Weak Binary Masks
```

## Development Direction

Kaggle is used for dataset exploration, weak mask generation, model training, and model export.

VS Code is used for documentation, Flask app development, GitHub control, and future iHIS integration preparation.

## Future iHIS Rule

The AI model should not directly modify any database.

Segmentation output should be stored as AI-generated output linked to a dental image record and reviewed by a dentist before clinical use.
