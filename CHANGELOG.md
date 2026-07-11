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

---

## Phase 4 — Image and Weak Mask Pairing Completed

### Added

- Added `docs/PHASE_4_COMPLETION.md`.
- Documented Phase 4 completion.
- Updated project status to show the next phase as train/validation split.
- Updated project memory with the rule to read GitHub and the latest notebook before every new phase.

### Completed

- Defined image size as 256 x 256.
- Created image and mask loading function.
- Tested image and mask loading function.
- Built X and Y arrays.
- Checked final dataset values.
- Visualized processed image and mask pair.
- Completed Phase 4 check.

### Verified Result

```text
X shape: (335, 256, 256, 1)
Y shape: (335, 256, 256, 1)
X dtype: float32
Y dtype: float32
X min/max: 0.0 1.0
Y min/max: 0.0 1.0
Y unique values: [0. 1.]
```

### Next

Start `Phase 5 — Train / Validation Split`.

---

## Phase 7, Phase 8, and Phase 9 Completed

### Added

- Added docs/PHASE_7_COMPLETION.md.
- Added docs/PHASE_8_COMPLETION.md.
- Added docs/PHASE_9_COMPLETION.md.
- Updated TODO.md to match the current roadmap phases.
- Updated docs/PROJECT_STATUS.md.
- Updated MEMORY.md with the new notebook working rule.

### Completed

- Confirmed U-Net architecture task and components.
- Built a simple U-Net model using TensorFlow/Keras.
- Verified model input and output shapes.
- Defined Dice coefficient.
- Defined IoU metric.
- Defined Dice loss.
- Compiled the U-Net model.

### Verified Result

Model input shape: (None, 256, 256, 1)
Model output shape: (None, 256, 256, 1)
Total params: 481,745
Model compiled successfully.

### Next

Start Phase 10 — Model Training.

## 2026-07-11 — Phase 10 to Phase 14 Completion

### Added
- Phase 10 training completion documentation.
- Phase 11 training curves completion documentation.
- Phase 12 prediction visualization completion documentation.
- Phase 13 final evaluation completion documentation.
- Phase 14 model export completion documentation.
- Kaggle notebook artifact.
- Trained U-Net Keras model artifact.

### Notes
- The model uses bounding-box-derived weak masks.
- The Flask deployment phase can now begin.

## 2026-07-11 — Phase 15 Flask Setup

### Added
- Flask requirements file.
- Flask app entry point.
- Flask configuration file.
- Initial HTML home page.
- Model existence check.
- Phase 15 documentation.

### Next
- Add image upload interface.
- Add prediction service.
- Add visualization of uploaded image, predicted mask, and overlay.

## 2026-07-11 — Phase 16 Upload Interface

### Added
- Image upload form.
- Flask POST upload handling.
- File extension validation.
- Secure filename saving.
- Uploaded image preview.

### Next
- Add model loading.
- Add preprocessing.
- Add prediction mask generation.
