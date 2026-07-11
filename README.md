# Tooth Segmentation Using U-Net and Flask

This project is an academic assignment for developing a dental image segmentation prototype using U-Net and Flask.

## Assignment Title

Development of a Dental Tooth Segmentation System Using U-Net and Flask

## Dataset

Dataset Name: Tufts Radiographs

Dataset Source: Kaggle

Dataset Link:
https://www.kaggle.com/datasets/manarmaged/tufts-radiographs/data

## Important Dataset Limitation

After dataset exploration, the dataset was found to provide bounding box annotations rather than ready-made pixel-level tooth segmentation masks.

Therefore, this project uses weak binary masks generated from bounding boxes for educational U-Net training.

The generated masks are pseudo masks and should not be described as true manual tooth segmentation masks.

## Goal

Build a complete weak-mask dental segmentation prototype:

```text
Dental panoramic radiograph
+
Bounding box annotation
↓
Generated weak binary mask
↓
U-Net segmentation prototype
↓
Export trained model
↓
Flask web app
↓
Upload new image
↓
Display original image, predicted weak mask, and overlay result
```

## Main Deliverables

1. Kaggle Notebook
2. Trained U-Net Model
3. Flask Source Code
4. Documentation
5. Screenshots / final report if required

## Environments

### Kaggle

Used for:

- Dataset access
- Dataset exploration
- Weak mask generation
- U-Net training
- GPU usage
- Model export

### VS Code

Used for:

- Flask app development
- File organization
- Documentation
- GitHub version control
- Future iHIS integration preparation

## Documentation

Main documentation is organized in the `docs/` folder:

```text
docs/ROADMAP.md
docs/PROJECT_STATUS.md
docs/DATASET_FINDINGS.md
docs/WEAK_MASK_DECISION.md
```

## Future Integration

This project starts as a standalone academic assignment, but it should remain suitable for later integration into the iHIS Dentistry Module.

The AI model should not directly modify any database.

In the future iHIS version, the segmentation output should be linked to a dental image record and reviewed by a dentist before clinical use.
