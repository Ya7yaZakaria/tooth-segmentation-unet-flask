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

## Current Status

Phase 0 completed.

Phase 1 dataset exploration completed.

Phase 2 imaging task understanding completed.

Phase 3 weak binary mask generation completed.

Phase 4 image and weak mask pairing completed.

## Current Next Step

```text
Phase 5 — Train / Validation Split
```

## Verified Phase 4 Result

```text
X shape: (335, 256, 256, 1)
Y shape: (335, 256, 256, 1)
X dtype: float32
Y dtype: float32
X min/max: 0.0 1.0
Y min/max: 0.0 1.0
Y unique values: [0. 1.]
```

## Working Rule

Before starting each new phase:

1. Read the current GitHub documentation.
2. Read the latest Kaggle notebook file if uploaded.
3. Update documentation after the phase is completed.
4. Commit and push before moving to the next phase.

## Future iHIS Rule

The AI model should not directly modify any database.

Segmentation output should be stored as AI-generated output linked to a dental image record and reviewed by a dentist before clinical use.
