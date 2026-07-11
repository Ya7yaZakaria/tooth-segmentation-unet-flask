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

- [x] Open Kaggle.
- [x] Create new Kaggle Notebook.
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
- [x] Confirm bounding-box-to-weak-mask strategy.

---

## Phase 2 — Understanding Dental Imaging and Segmentation

- [x] Clarify classification, detection, and segmentation.
- [x] Confirm that bounding boxes are detection-style annotations.
- [x] Confirm that U-Net requires image-mask pairs.
- [x] Document that this project uses weak binary masks.
- [x] Avoid describing generated masks as true manual tooth masks.

---

## Phase 3 — Weak Binary Mask Generation

- [x] Step 1 — Generate one weak binary mask.
- [x] Step 2 — Display original image and generated weak mask.
- [x] Step 3 — Display weak mask overlay.
- [x] Step 4 — Create reusable weak-mask generation function.
- [x] Step 5 — Test reusable weak-mask generation function.
- [x] Step 6 — Prepare annotated image list.
- [x] Step 7 — Check annotated images exist.
- [x] Step 8 — Generate weak masks for sample images.
- [x] Step 9 — Visualize weak masks for sample images.
- [x] Step 10 — Phase 3 completion check.

---

## Phase 4 — Image and Weak Mask Pairing

- [x] Step 1 — Define image size.
- [x] Step 2 — Create image and mask loading function.
- [x] Step 3 — Test image and mask loading function.
- [x] Step 4 — Build image and mask arrays.
- [x] Step 5 — Check final dataset values.
- [x] Step 6 — Visualize processed image and mask pair.
- [x] Step 7 — Phase 4 completion check.

---

## Phase 5 — Train / Validation Split

- [ ] Step 1 — Import train test split.
- [ ] Step 2 — Split dataset into training and validation sets.
- [ ] Step 3 — Phase 5 completion check.

---

## Phase 6 — U-Net Training

- [ ] Build U-Net model.
- [ ] Add Dice coefficient.
- [ ] Add IoU metric if needed.
- [ ] Compile model.
- [ ] Train model.
- [ ] Save best checkpoint.

---

## Phase 7 — Evaluation and Visualization

- [ ] Evaluate on validation/test samples.
- [ ] Show original image.
- [ ] Show weak mask.
- [ ] Show predicted mask.
- [ ] Show overlay.
- [ ] Save result screenshots.

---

## Phase 8 — Model Export

- [ ] Export model as .keras or .h5.
- [ ] Download trained model.
- [ ] Place model inside VS Code project.

---

## Phase 9 — Flask App

- [ ] Create Flask app.
- [ ] Create upload page.
- [ ] Load trained model.
- [ ] Preprocess uploaded image.
- [ ] Predict weak mask.
- [ ] Save prediction.
- [ ] Display original, predicted mask, and overlay.

---

## Phase 10 — Final Submission

- [ ] Finalize Kaggle notebook.
- [ ] Finalize Flask source code.
- [ ] Finalize README.
- [ ] Prepare screenshots.
- [ ] Prepare report if required.
