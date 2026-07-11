# Project Memory

## Project

Tooth Segmentation Using U-Net and Flask

## Repository

Ya7yaZakaria/tooth-segmentation-unet-flask

## Main Decision

The selected Tufts Radiographs dataset provides bounding box annotations, not ready-made pixel-level tooth segmentation masks.

Therefore, the project generates weak binary masks from bounding boxes and trains a U-Net weak-mask segmentation prototype.

## Correct Wording

Use:
- weak binary masks
- pseudo masks
- weak-mask segmentation prototype
- bounding-box-derived masks

Avoid:
- true manual tooth segmentation masks
- ground truth tooth masks
- clinical tooth boundary segmentation

## Current Status

Phase 0 completed.
Phase 1 completed.
Phase 2 completed.
Phase 3 completed.
Phase 4 completed.
Phase 5 completed.
Phase 6 completed.
Phase 7 completed.
Phase 8 completed.
Phase 9 completed.

## Current Next Step

Phase 10 — Model Training

## Verified Phase 8 Result

Model input shape: (None, 256, 256, 1)
Model output shape: (None, 256, 256, 1)
Total params: 481,745

## Verified Phase 9 Result

Dice coefficient defined.
IoU metric defined.
Dice loss defined.
Model compiled successfully.

## Working Notebook Rule

For each new phase:
1. Use one Markdown cell with phase title and steps.
2. Use one Code cell containing the full phase code.
3. Put step comments inside the code.
4. Use organized print outputs.
5. Keep explanation in ChatGPT, not inside long notebook markdown.

## Future iHIS Rule

The AI model should not directly modify any database.

Segmentation output should be stored as AI-generated output linked to a dental image record and reviewed by a dentist before clinical use.

## Memory Update — Phase 10 to Phase 14

The Kaggle part of the assignment is now complete.

The project now contains:
- Kaggle notebook: notebooks/tooth_segmentation_unet_kaggle.ipynb
- Trained model: flask_app/model/unet_weak_mask_segmentation.keras

The U-Net model was trained using bounding-box-derived weak masks because the dataset provides bounding boxes rather than true pixel-level segmentation masks.

Final evaluation showed weak Dice and IoU but high background-driven accuracy. The limitation should be explained clearly in the report and Flask demo.

## Memory Update — Phase 15

The Flask application setup has started.

Current Flask files:
- flask_app/app.py
- flask_app/config.py
- flask_app/templates/index.html
- requirements.txt

The app checks for the trained model at:
flask_app/model/unet_weak_mask_segmentation.keras
