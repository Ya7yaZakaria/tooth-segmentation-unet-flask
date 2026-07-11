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
