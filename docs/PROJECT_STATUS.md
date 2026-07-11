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

## Dataset Finding

The dataset provides bounding box annotations, not ready-made pixel-level tooth segmentation masks.

## Current Project Direction

This project will generate weak binary masks from bounding boxes and train a U-Net weak-mask segmentation prototype.

## Current Notebook Position

```text
Phase 2 — Generate Weak Binary Masks
```

## Next Tasks

- Generate one weak binary mask.
- Display original radiograph and generated weak mask.
- Display overlay.
- Create reusable weak-mask generation function.
- Continue preprocessing.
