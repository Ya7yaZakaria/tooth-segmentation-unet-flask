# Phase 11 Completion — Training Curves

## Status
Completed.

## Goal
Visualize and review the training behavior of the U-Net model.

## What was done
- Plotted training loss and validation loss.
- Plotted Dice coefficient behavior.
- Plotted IoU behavior.
- Reviewed the best validation results.

## Key result
- Best validation loss: approximately 1.0523
- Best validation Dice: approximately 0.0339
- Best validation IoU: approximately 0.0173

## Interpretation
The weak numerical performance reflects the limitation of bounding-box-derived masks and the strong background imbalance.
Accuracy is not reliable for this task because most pixels are background.
