# Phase 17 Completion — Flask Prediction Service

## Status
Completed.

## Goal
Connect the Flask application to the trained U-Net model and generate predicted weak segmentation masks from uploaded dental radiographs.

## What was done
- Added a prediction service module.
- Loaded the trained Keras U-Net model with compile disabled for inference.
- Added image preprocessing matching the Kaggle notebook:
  - grayscale image reading
  - resize to 256 x 256
  - normalization to 0–1
  - channel and batch dimension expansion
- Generated model predictions.
- Converted soft probability maps into binary weak masks.
- Saved prediction masks into the static predictions folder.
- Updated the Flask page to show the uploaded image and predicted mask.

## Model path
flask_app/model/unet_weak_mask_segmentation.keras

## Upload folder
flask_app/static/uploads

## Prediction folder
flask_app/static/predictions

## Important technical note
A threshold of 0.03 is used because the trained weak-mask model produces low-confidence probability maps. A standard 0.5 threshold produced mostly empty masks during notebook testing.

## Current capability
The user can upload a dental radiograph and receive a predicted weak segmentation mask.

## Next phase
Phase 18 will add overlay visualization between the uploaded image and predicted mask.
