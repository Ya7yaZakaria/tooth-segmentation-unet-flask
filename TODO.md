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

## Phase 2 — Weak Binary Mask Generation

- [ ] Generate one weak mask from one sample image.
- [ ] Display original image and generated weak mask.
- [ ] Display weak mask overlay.
- [ ] Create reusable weak-mask generation function.
- [ ] Validate mask shape matches original image shape.

---

## Phase 3 — Image and Weak Mask Pairing

- [ ] Use annotated images only.
- [ ] Generate image-mask pairs.
- [ ] Check missing images.
- [ ] Confirm number of usable pairs.

---

## Phase 4 — Preprocessing

- [ ] Resize images.
- [ ] Normalize images.
- [ ] Resize weak masks using nearest-neighbor interpolation.
- [ ] Convert masks to binary.
- [ ] Expand dimensions.
- [ ] Build NumPy arrays.

---

## Phase 5 — Train / Validation / Test Split

- [ ] Split into train, validation, and test sets.
- [ ] Print shapes.
- [ ] Confirm no leakage.

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

- [ ] Evaluate on test set.
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
- [ ] Display original, mask, and overlay.

---

## Phase 10 — Final Submission

- [ ] Finalize Kaggle notebook.
- [ ] Finalize Flask source code.
- [ ] Finalize README.
- [ ] Prepare screenshots.
- [ ] Prepare report if required.
