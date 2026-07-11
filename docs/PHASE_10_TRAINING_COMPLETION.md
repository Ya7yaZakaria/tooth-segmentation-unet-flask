# Phase 10 Completion — Model Training

## Status
Completed.

## Goal
Train a U-Net segmentation model using the prepared image and bounding-box-derived weak mask pairs.

## What was done
- Used the paired dataset created in previous phases.
- Trained a U-Net model on grayscale dental radiographs.
- Used training, validation, and test splits.
- Saved the best model during training.
- Initial Dice-only training produced very weak predictions because the masks are sparse and background-dominant.
- Improved training was performed using a combined BCE + Dice loss.

## Important note
The model was trained on weak masks generated from bounding boxes, not true manual tooth boundary masks.

## Result
The improved model produced low-confidence soft probability maps but was usable for completing the assignment pipeline and Flask deployment.
