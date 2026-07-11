# Changelog

All notable changes to this project will be documented in this file.

---

## Phase 0 — Project Planning

### Added

- Created initial project planning file.
- Defined the assignment goal.
- Defined the main deliverables:
  - Kaggle Notebook
  - Trained U-Net Model
  - Flask Source Code
- Defined the project workflow:
  - Dental panoramic X-ray
  - Image preprocessing
  - U-Net segmentation model
  - Predicted tooth mask
  - Flask web application
- Clarified the difference between:
  - Kaggle for model training
  - VS Code for Flask development
  - iHIS for future integration
- Added future iHIS integration direction.
- Defined the initial scope as a simple assignment-focused version.

### Notes

This project will start as a standalone academic assignment, but it will be organized to support future integration into the iHIS Dentistry Module.

---

## Phase 1 — Dataset Exploration and Weak-Mask Workflow Update

### Added

- Added corrected roadmap in `docs/ROADMAP.md`.
- Added project status documentation in `docs/PROJECT_STATUS.md`.
- Added dataset findings documentation in `docs/DATASET_FINDINGS.md`.
- Added weak-mask decision documentation in `docs/WEAK_MASK_DECISION.md`.

### Changed

- Updated README to describe the project as a weak-mask segmentation prototype.
- Updated project plan to reflect bounding-box-derived weak masks.
- Updated TODO to mark Phase 1 dataset exploration as completed.
- Updated MEMORY with the dataset limitation and current project direction.

### Key Decision

The Tufts Radiographs dataset provides bounding box annotations, not ready-made pixel-level tooth segmentation masks.

Therefore, this project will generate weak binary masks from bounding boxes for educational U-Net training.

### Correct Wording

Use `weak mask`, `pseudo mask`, or `bounding-box-derived mask`.

Avoid describing the generated masks as true manual tooth segmentation masks.

---

## Phase 3 — Weak Binary Mask Generation Completed

### Added

- Added `docs/PHASE_3_COMPLETION.md`.
- Documented completed Phase 3 notebook steps.
- Updated project status to show the next phase as image-mask pairing.

### Completed

- Generated one weak binary mask.
- Displayed original radiograph and generated weak mask.
- Displayed weak mask overlay.
- Created reusable weak-mask generation function.
- Tested reusable function successfully.
- Prepared annotated image list.
- Confirmed annotated image availability.
- Generated weak masks for sample images.
- Visualized sample weak masks.
- Completed Phase 3 check.

### Verified Result

```text
Number of annotated training images: 335
Image shape = Mask shape
Mask unique values = [0, 255]
```

### Next

Start `Phase 4 — Image and Weak Mask Pairing`.
