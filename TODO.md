# TODO

## Phase 0 — Project Planning

- [x] Create project folder.
- [x] Create project_plan.md.
- [x] Create README.md.
- [x] Create CHANGELOG.md.
- [x] Create MEMORY.md.
- [x] Create TODO.md.
- [x] Create .gitignore.
- [x] Create initial folders.

---

## Phase 1 — Kaggle Dataset Exploration

- [x] Access Tufts Radiographs dataset.
- [x] Inspect dataset folders.
- [x] Identify image folders.
- [x] Identify annotation folders.
- [x] Read train bounding box CSV.
- [x] Read test bounding box CSV.
- [x] Display sample images.
- [x] Visualize bounding boxes.
- [x] Analyze class distribution.
- [x] Confirm no ready-made pixel-level masks were found.

---

## Phase 2 — Understanding Dental Imaging and Segmentation

- [x] Clarify classification, detection, and segmentation.
- [x] Confirm that bounding boxes are detection-style annotations.
- [x] Confirm that U-Net requires image-mask pairs.
- [x] Document that this project uses weak binary masks.

---

## Phase 3 — Weak Binary Mask Generation

- [x] Generate weak binary masks from bounding boxes.
- [x] Create reusable weak-mask function.
- [x] Test weak-mask function.
- [x] Visualize generated weak masks.
- [x] Complete Phase 3 check.

---

## Phase 4 — Image and Weak Mask Pairing

- [x] Create matched image-mask pairs.
- [x] Use annotated images only.
- [x] Build X and Y arrays.
- [x] Confirm final X and Y shapes.
- [x] Complete Phase 4 check.

---

## Phase 5 — Preprocessing

- [x] Confirm preprocessing settings.
- [x] Verify preprocessed dataset tensors.
- [x] Complete Phase 5 check.

---

## Phase 6 — Train / Validation / Test Split

- [x] Import train_test_split.
- [x] Create train / validation / test split.
- [x] Verify split shapes.
- [x] Complete Phase 6 check.

---

## Phase 7 — U-Net Architecture Understanding

- [x] Confirm U-Net task.
- [x] Confirm U-Net components.
- [x] Complete Phase 7 check.

---

## Phase 8 — Build U-Net Model

- [x] Import TensorFlow and Keras layers.
- [x] Define convolution block.
- [x] Build U-Net architecture.
- [x] Create U-Net model.
- [x] Display model summary.
- [x] Complete Phase 8 check.

---

## Phase 9 — Loss Functions and Metrics

- [x] Define Dice coefficient.
- [x] Define IoU metric.
- [x] Define Dice loss.
- [x] Compile U-Net model.
- [x] Complete Phase 9 check.

---

## Phase 10 — Model Training

- [ ] Add EarlyStopping.
- [ ] Add ModelCheckpoint.
- [ ] Train U-Net model.
- [ ] Monitor validation loss and metrics.
- [ ] Save best model checkpoint.
- [ ] Complete Phase 10 check.

---

## Phase 11 — Training Curves

- [ ] Plot training loss curve.
- [ ] Plot validation loss curve.
- [ ] Plot training Dice curve.
- [ ] Plot validation Dice curve.

---

## Phase 12 — Prediction Visualization

- [ ] Generate predictions.
- [ ] Show original radiograph.
- [ ] Show weak mask.
- [ ] Show predicted mask.
- [ ] Show overlay.

---

## Phase 13 — Final Evaluation

- [ ] Evaluate model on test set.
- [ ] Report Dice score.
- [ ] Report IoU score.
- [ ] Use correct weak-mask wording.

---

## Phase 14 — Export Model

- [ ] Export trained model as .keras or .h5.
- [ ] Download trained model.
- [ ] Place model inside VS Code project.

---

## Phase 15 — Flask Project Setup

- [ ] Prepare Flask deployment app.

---

## Phase 16 — Flask Upload Page

- [ ] Create image upload page.

---

## Phase 17 — Flask Prediction Pipeline

- [ ] Connect trained model to Flask.

---

## Phase 18 — Overlay Result in Flask

- [ ] Display uploaded radiograph, predicted weak mask, and overlay.

---

## Phase 19 — Requirements and README

- [ ] Finalize README and requirements.

---

## Phase 20 — Final Report

- [ ] Prepare academic report.

---

## Phase 21 — Final Submission Package

- [ ] Prepare final submission folder.

## Completed — Kaggle Training and Export

- [x] Phase 10 — Train U-Net model
- [x] Phase 11 — Review training curves
- [x] Phase 12 — Visualize predictions
- [x] Phase 13 — Final evaluation
- [x] Phase 14 — Export trained model
- [x] Add Kaggle notebook to repository
- [x] Add trained Keras model to repository

## Next
- [ ] Phase 15 — Flask project setup
- [ ] Phase 16 — Flask upload interface
- [ ] Phase 17 — Flask prediction service
- [ ] Phase 18 — Result visualization

## Completed — Flask Setup

- [x] Phase 15 — Flask project setup

## Next
- [ ] Phase 16 — Flask upload interface
- [ ] Phase 17 — Flask prediction service
- [ ] Phase 18 — Result visualization

## Completed — Upload Interface

- [x] Phase 16 — Flask upload interface

## Next
- [ ] Phase 17 — Flask prediction service
- [ ] Phase 18 — Result visualization

## Completed — Prediction Service

- [x] Phase 17 — Flask prediction service

## Next
- [ ] Phase 18 — Result visualization and overlay

## Completed — Result Visualization

- [x] Phase 18 — Result visualization and overlay

## Next
- [ ] Phase 19 — Final cleanup and testing
- [ ] Phase 20 — Final submission packaging

## Completed — Final Submission Packaging

- [x] Phase 20 — Final submission packaging
- [x] Final README polish
- [x] Final submission checklist
- [x] Final deliverables list
- [x] Run instructions
- [x] Limitation statement

## Final Status
- [x] Project ready for final review
- [x] Project ready for academic submission
