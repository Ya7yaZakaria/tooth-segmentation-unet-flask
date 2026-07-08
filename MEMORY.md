# Project Memory

This file stores important project decisions and context so the work remains organized across phases.

---

## Project Identity

Project name:

Dental Tooth Segmentation System Using U-Net and Flask

Assignment title:

Development of a Dental Tooth Segmentation System Using U-Net and Flask

---

## Main Goal

Build a standalone academic assignment that trains a U-Net model on Kaggle and deploys it using Flask.

The project should also remain suitable for future integration into the iHIS Dentistry Module.

---

## Environment Decision

Kaggle will be used for:

- Dataset access
- Model training
- GPU usage
- Notebook submission

VS Code will be used for:

- Flask app development
- File organization
- README and documentation
- Future iHIS integration preparation

---

## Future iHIS Integration Decision

The module should be designed as a standalone prototype now, but later it may be integrated into:

- iHIS Dentistry Module
- Dental Imaging workflow
- AI Dental Assistant
- Patient Dental Record
- Dentist Dashboard

The model should not directly modify the database.

Future iHIS integration should save segmentation results as AI-generated outputs linked to dental image records and reviewed by a dentist.

---

## Architecture Decision

Keep the assignment simple, but not disposable.

The Flask app should separate:

- Web route logic
- AI prediction service
- Image preprocessing utilities
- Model storage
- Prediction output storage

---

## Training Decision

Initial model version:

- Simple U-Net
- Binary segmentation
- Image size: 256 x 256
- Output: tooth mask
- Metrics: Dice coefficient and IoU

---

## Scope Decision

Initial scope is academic and simple.

Do not add:

- Database
- Login
- RBAC
- Complex dashboard
- Full iHIS integration now

These will be considered later after the standalone assignment works.

---

## Current Phase

Phase 0:

Project understanding, file setup, planning, and architecture mindset.
