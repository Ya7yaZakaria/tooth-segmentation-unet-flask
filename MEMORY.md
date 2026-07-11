# Project Memory

## Project

Tooth Segmentation Using U-Net and Flask

## Repository

```text
Ya7yaZakaria/tooth-segmentation-unet-flask
```

## Main Decision

The selected Tufts Radiographs dataset provides bounding box annotations, not ready-made pixel-level tooth segmentation masks.

Therefore, the project generates weak binary masks from bounding boxes and will train a U-Net weak-mask segmentation prototype.

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

Phase 1 dataset exploration completed.

Phase 2 imaging task understanding completed.

Phase 3 weak binary mask generation completed.

## Current Next Step

```text
Phase 4 — Image and Weak Mask Pairing
```

## Verified Phase 3 Result

```text
Annotated training images: 335
Image shape = Mask shape
Mask unique values = [0, 255]
```

## Development Direction

Kaggle is used for dataset exploration, weak mask generation, model training, and model export.

VS Code is used for documentation, Flask app development, GitHub control, and future iHIS integration preparation.

## Future iHIS Rule

The AI model should not directly modify any database.

Segmentation output should be stored as AI-generated output linked to a dental image record and reviewed by a dentist before clinical use.
