# Tooth Segmentation Using U-Net and Flask — Roadmap

## Project Title

Development of a Dental Tooth Segmentation Prototype Using U-Net and Flask

---

## Project Reality Check

The original assignment goal is tooth segmentation using U-Net.

After exploring the Tufts Radiographs dataset, the dataset was found to contain panoramic dental radiographs and bounding box annotations, not ready-made pixel-level tooth segmentation masks.

Therefore, this project will be implemented as a weak-mask segmentation prototype.

```text
Dental panoramic radiographs
+
Bounding box annotations
↓
Generate weak binary masks
↓
Train U-Net segmentation prototype
↓
Deploy with Flask
```

The generated masks are pseudo masks created from bounding boxes.

They should not be described as true manual tooth segmentation masks.

This limitation must be clearly stated in the notebook, README, project plan, and final report.

---

# Phase 0 — Project Setup and Planning

## Goal

Prepare the project structure, documentation, and GitHub repository before model development.

## Completed

- Project folder created.
- Git repository initialized.
- GitHub repository connected.
- Initial documentation files created.
- Initial folder structure created.

## Output

```text
README.md
project_plan.md
TODO.md
CHANGELOG.md
MEMORY.md
AGENTS.md
docs/
flask_app/
models/
notebooks/
screenshots/
```

---

# Phase 1 — Dataset Exploration on Kaggle

## Goal

Understand the dataset structure before training any model.

## Completed

- Kaggle Notebook created.
- Dataset accessed using Kaggle.
- Dataset folder structure inspected.
- Training images folder identified.
- Testing images folder identified.
- Bounding box CSV files identified.
- CSV files loaded with pandas.
- Sample images displayed.
- Bounding boxes visualized on radiographs.
- Class distribution analyzed.

## Key Findings

```text
Training images: 980
Testing images: 20
Annotated training images: 335
Train CSV rows: 520
Test CSV rows: 6
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

## Important Decision

No ready-made pixel-level tooth segmentation masks were found.

The available annotations are bounding boxes.

Therefore, bounding boxes will be converted into weak binary masks for educational U-Net training.

---

# Phase 2 — Understanding Dental Imaging and Segmentation

## Goal

Understand the difference between classification, detection, and segmentation.

## Classification

Classification answers:

```text
What is in the image?
```

## Detection

Detection answers:

```text
Where is the finding?
```

Detection commonly uses bounding boxes.

## Segmentation

Segmentation answers:

```text
Which pixels belong to the target region?
```

Segmentation requires pixel-level masks.

## Project-Specific Meaning

This project is not using manual tooth boundary masks.

It will generate weak binary masks from bounding boxes.

So the correct wording is:

```text
weak-mask segmentation prototype
bounding-box-derived masks
pseudo masks
```

Avoid wording like:

```text
true manual tooth segmentation masks
clinical tooth boundary segmentation
ground truth tooth masks
```

---

# Phase 3 — Weak Binary Mask Generation

## Goal

Convert bounding box annotations into binary masks.

## Concept

For each annotated image:

```text
Original dental radiograph
+
CSV bounding boxes
↓
Generated weak binary mask
```

The mask contains:

```text
0 = background
1 = weak target region
```

Visually:

```text
Black background
White rectangular annotation regions
```

## Implementation Tasks

- Generate one weak mask from one sample image.
- Display the original image.
- Display the generated weak mask.
- Display overlay of weak mask over the radiograph.
- Create reusable function for mask generation.

## Notebook Section

```text
3. Weak Binary Mask Generation
```

---

# Phase 4 — Image and Weak Mask Pairing

## Goal

Create matched image-mask pairs for training.

## Rule

```text
Each image must match its correct generated weak mask.
```

## Project Decision

Only images listed in the bounding box CSV should be used in the first training version.

Unannotated images should not be used for supervised training.

---

# Phase 5 — Preprocessing

## Goal

Convert radiographs and masks into model-ready tensors.

## Processing Logic

```text
Image → grayscale → resize → normalize → expand dimensions
Mask → resize → binary → expand dimensions
```

## Initial Settings

```text
Image size: 256 x 256
Image values: 0 to 1
Mask values: 0 or 1
```

---

# Phase 6 — Train / Validation / Test Split

## Goal

Split data honestly.

```text
Training set   → model learns
Validation set → monitor during training
Test set       → final evaluation
```

## Recommended Split

```text
70% training
15% validation
15% testing
```

---

# Phase 7 — U-Net Architecture Understanding

## Goal

Understand the U-Net model.

## Main Components

```text
Encoder
Bottleneck
Decoder
Skip connections
```

## Why U-Net

U-Net is commonly used in medical image segmentation because it combines deep feature extraction with spatial detail preservation using skip connections.

---

# Phase 8 — Build U-Net Model

## Goal

Build a simple U-Net using TensorFlow/Keras.

## Initial Strategy

```text
Input shape: 256 x 256 x 1
Output shape: 256 x 256 x 1
Final activation: sigmoid
Task: binary weak-mask segmentation
```

---

# Phase 9 — Loss Functions and Metrics

## Goal

Use metrics suitable for segmentation.

## Metrics

```text
Dice coefficient
IoU
Binary crossentropy
Dice loss
```

## Important Note

Accuracy alone is not enough because the background may dominate the image.

Dice and IoU are more useful for mask overlap.

---

# Phase 10 — Model Training

## Goal

Train the U-Net model on generated weak masks.

## Training Strategy

```text
Simple U-Net
256 x 256 images
Batch size: 8
Epochs: up to 30
EarlyStopping
ModelCheckpoint
```

---

# Phase 11 — Training Curves

## Goal

Visualize training behavior.

## Outputs

```text
Training loss curve
Validation loss curve
Training Dice curve
Validation Dice curve
```

---

# Phase 12 — Prediction Visualization

## Goal

Inspect model predictions visually.

## Required Views

```text
Original radiograph
Weak mask
Predicted mask
Overlay
```

## Correct Label

Use:

```text
Weak Mask
```

not:

```text
Ground Truth Tooth Mask
```

---

# Phase 13 — Final Evaluation

## Goal

Evaluate the model on the test set.

## Correct Wording

Use:

```text
The model was evaluated against weak masks generated from bounding box annotations.
```

Avoid:

```text
The model achieved true tooth segmentation accuracy.
```

---

# Phase 14 — Export Model

## Goal

Save the trained model for deployment.

## Output

```text
unet_weak_mask_segmentation.keras
```

or:

```text
unet_weak_mask_segmentation.h5
```

---

# Phase 15 — Flask Project Setup

## Goal

Prepare the deployment app.

## Structure

```text
flask_app/
├── app.py
├── model/
├── services/
├── utils/
├── static/
│   ├── uploads/
│   └── predictions/
├── templates/
└── requirements.txt
```

---

# Phase 16 — Flask Upload Page

## Goal

Create a simple page for image upload.

## Output

A page where the user uploads a dental radiograph and runs segmentation.

---

# Phase 17 — Flask Prediction Pipeline

## Goal

Connect the trained model to Flask.

## Important Rule

The preprocessing in Flask must match Kaggle preprocessing exactly:

```text
grayscale
resize to 256 x 256
normalize to 0–1
expand dimensions
```

---

# Phase 18 — Overlay Result in Flask

## Goal

Display useful visual output.

## Flask Output

```text
Uploaded radiograph
Predicted weak mask
Overlay result
```

---

# Phase 19 — Requirements and README

## Goal

Prepare project documentation for review.

## README Must Mention

```text
Dataset
Annotation limitation
Weak mask generation
U-Net model
Flask deployment
How to run
Limitations
Future work
```

---

# Phase 20 — Final Report

## Goal

Convert the project into academic submission.

## Report Sections

```text
1. Introduction
2. Dataset Description
3. Annotation Type and Limitation
4. Weak Mask Generation
5. Preprocessing
6. U-Net Architecture
7. Training Setup
8. Evaluation Metrics
9. Results
10. Flask Deployment
11. Limitations
12. Future Work
13. Conclusion
```

## Critical Limitation Statement

```text
The dataset used in this project provides bounding box annotations rather than manually segmented tooth masks. Therefore, weak binary masks were generated from bounding boxes to train a U-Net segmentation prototype. The resulting predictions should be interpreted as weak region segmentation rather than true anatomical tooth segmentation.
```

---

# Phase 21 — Final Submission Package

## Final Folder

```text
Tooth_Segmentation_Assignment/
├── kaggle_notebook.ipynb
├── unet_weak_mask_segmentation.keras
├── flask_app/
├── report.pdf
└── screenshots/
```

---

# Current Next Step

Continue the Kaggle Notebook from:

```text
Phase 2 — Generate Weak Binary Masks
```

Next tasks:

```text
Generate one weak binary mask
Show original image and weak mask
Show overlay
Create reusable weak-mask function
```
