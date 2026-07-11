# Phase 12 Completion — Prediction Visualization

## Status
Completed.

## Goal
Generate prediction masks from the trained U-Net model and visually inspect model behavior.

## What was done
- Predicted segmentation masks on test images.
- Displayed original image, weak mask, predicted mask, and overlay.
- Inspected raw prediction probabilities.
- Tested different thresholds because standard 0.5 threshold produced mostly black masks.

## Key finding
The model output was low confidence:
- Maximum probability was around 0.10 on inspected samples.
- Threshold 0.5 produced empty masks.
- Lower thresholds showed weak activation over dental regions.

## Interpretation
The model learned a weak soft localization pattern rather than precise segmentation boundaries.
This is expected because the labels are weak masks generated from bounding boxes.
