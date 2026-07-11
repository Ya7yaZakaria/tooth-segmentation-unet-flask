# Phase 13 Completion — Final Evaluation

## Status
Completed.

## Goal
Evaluate the final trained U-Net model on the held-out test set.

## What was done
- Loaded the best improved U-Net model.
- Evaluated the model on the test split.
- Reported loss, Dice coefficient, IoU, and accuracy.
- Interpreted the results in the context of weak mask supervision.

## Final test results
- Test loss: approximately 1.0744
- Test Dice coefficient: approximately 0.0515
- Test IoU: approximately 0.0265
- Test accuracy: approximately 0.9717

## Interpretation
The high accuracy is misleading because the images are dominated by background pixels.
Dice and IoU are more meaningful for segmentation and show that the model performance is weak.
The result is still acceptable as a complete educational pipeline using weak supervision from bounding-box annotations.
