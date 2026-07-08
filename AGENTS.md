# AGENTS.md

This file defines how AI coding assistants should work on this project.

The goal is to make ChatGPT, Codex, Cursor, or any coding agent understand the project context before writing code.

---

## Project Identity

Project name:

Tooth Segmentation Using U-Net and Flask

Assignment title:

Development of a Dental Tooth Segmentation System Using U-Net and Flask

This is an academic medical AI project.

The project trains a U-Net model on the Tufts Radiographs dataset using Kaggle, then deploys the trained model using Flask.

---

## Main Rule

Do not jump directly into coding.

Always follow the current project phase.

For each phase:

1. Read README.md.
2. Read project_plan.md.
3. Read MEMORY.md.
4. Read TODO.md.
5. Check CHANGELOG.md.
6. Understand the current phase before changing files.
7. Propose a short plan before implementing.
8. Keep the implementation simple and assignment-focused.

---

## Current Development Strategy

This project has two environments.

### Kaggle Environment

Use Kaggle for:

- Dataset exploration
- Image and mask loading
- Preprocessing
- U-Net model training
- Evaluation
- Prediction visualization
- Model export

Do not build Flask inside Kaggle.

The expected Kaggle output is:

- Kaggle Notebook
- Trained model file:
  - unet_tooth_segmentation.h5
  - or unet_tooth_segmentation.keras

### VS Code Environment

Use VS Code for:

- Flask application
- Documentation
- File structure
- Local testing
- Future iHIS integration preparation

Do not train the model inside VS Code unless explicitly requested.

---

## Future iHIS Integration

This project is standalone now, but must remain suitable for future integration into iHIS.

The future target is:

- iHIS Dentistry Module
- Dental Imaging workflow
- AI Dental Assistant
- Patient Dental Record
- Dentist Dashboard

Important rule:

The AI model must not directly modify the database.

In future iHIS integration, segmentation output should be saved as an AI-generated result linked to a dental image record and reviewed by a dentist.

---

## Coding Principles

Keep the code:

- Simple
- Readable
- Educational
- Modular
- Easy to explain
- Suitable for academic submission
- Easy to migrate later into iHIS

Avoid:

- Overengineering
- Complex authentication
- Database features in the first version
- RBAC
- Large frontend frameworks
- Unnecessary APIs
- Complex deployment setup
- Direct database writes from AI code

---

## Expected Final Structure

The project may evolve toward this structure:

tooth-segmentation-unet-flask/
├── README.md
├── project_plan.md
├── CHANGELOG.md
├── MEMORY.md
├── TODO.md
├── AGENTS.md
├── .gitignore
│
├── notebooks/
│   └── kaggle_tooth_segmentation_unet.ipynb
│
├── models/
│   └── unet_tooth_segmentation.h5
│
├── flask_app/
│   ├── app.py
│   ├── config.py
│   ├── services/
│   │   └── tooth_segmentation_service.py
│   ├── utils/
│   │   └── image_preprocessing.py
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   ├── uploads/
│   │   └── predictions/
│   └── requirements.txt
│
├── docs/
└── screenshots/

---

## Phase Guide

### Phase 0 — Planning

Allowed work:

- Create planning files.
- Create README.
- Create CHANGELOG.
- Create MEMORY.
- Create TODO.
- Create AGENTS.md.
- Create initial folders.

Do not write model training code yet.

---

### Phase 1 — Kaggle Dataset Exploration

Allowed work:

- Create Kaggle notebook.
- Add Tufts Radiographs dataset.
- Inspect folders.
- Identify images.
- Identify masks or annotations.
- Display sample radiographs.
- Document image-mask pairing strategy.

Output:

- Dataset exploration section in notebook.
- Updated MEMORY.md with dataset structure.
- Updated CHANGELOG.md.

---

### Phase 2 — Preprocessing

Allowed work:

- Load images.
- Load masks.
- Resize to 256 x 256.
- Normalize images.
- Convert masks to binary.
- Visualize image-mask pairs.

Output:

- Preprocessing functions.
- Sample visualizations.

---

### Phase 3 — U-Net Training

Allowed work:

- Build simple U-Net.
- Add Dice coefficient.
- Add IoU metric.
- Compile model.
- Train on Kaggle GPU.
- Save checkpoint.

Output:

- Training history.
- Best model checkpoint.

---

### Phase 4 — Evaluation

Allowed work:

- Evaluate on validation/test set.
- Show original images.
- Show ground truth masks.
- Show predicted masks.
- Show overlays.
- Save screenshots.

Output:

- Evaluation metrics.
- Prediction examples.

---

### Phase 5 — Model Export

Allowed work:

- Export trained model as .h5 or .keras.
- Download model from Kaggle.
- Place model in models/.

Output:

- unet_tooth_segmentation.h5
- or unet_tooth_segmentation.keras

---

### Phase 6 — Flask App

Allowed work:

- Build simple Flask app.
- Create upload page.
- Load trained model.
- Preprocess uploaded image.
- Predict mask.
- Save prediction.
- Display original, mask, and overlay.

Output:

- Running Flask app.

---

### Phase 7 — Final Submission

Allowed work:

- Finalize notebook.
- Finalize Flask source code.
- Finalize README.
- Prepare screenshots.
- Prepare report if required.
- Prepare submission folder.

---

## How the Agent Should Respond

When asked to work on a phase, respond with:

1. Phase name.
2. Objective.
3. Files to create or modify.
4. Terminal commands if needed.
5. Code or content to paste.
6. Validation command.
7. What to send back for review.

Do not provide too many unrelated options.

Do not skip validation.

---

## Validation Rules

After each phase, run relevant checks.

For Phase 0:

- Check file tree.
- Confirm files are not empty.
- Confirm README.md and project_plan.md exist.
- Confirm AGENTS.md exists.

For Flask phases:

- Run app locally.
- Confirm upload works.
- Confirm prediction image is saved.
- Confirm result page displays output.

For Git phases:

- Run git status.
- Commit only phase-related files.

---

## Documentation Rules

Update CHANGELOG.md after every phase.

Update MEMORY.md whenever an important decision is made.

Update TODO.md when tasks are completed.

Keep README.md user-facing and concise.

Keep project_plan.md more detailed than README.md.

---

## Safety and Medical AI Rules

This is a research and educational prototype.

Do not present the model as clinically validated.

Do not claim diagnostic accuracy unless measured.

Do not allow the AI prediction to replace dentist review.

Always describe output as AI-generated segmentation support.
