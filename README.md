# Tooth Segmentation Using U-Net and Flask

This project is an academic assignment for developing a dental tooth segmentation system using U-Net and Flask.

## Assignment Title

Development of a Dental Tooth Segmentation System Using U-Net and Flask

## Dataset

Dataset Name: Tufts Radiographs

Dataset Source: Kaggle

Dataset Link:
https://www.kaggle.com/datasets/manarmaged/tufts-radiographs/data

## Goal

Train a U-Net model to segment teeth from panoramic dental radiographs and deploy the trained model using a Flask web application.

## Main Deliverables

1. Kaggle Notebook
2. Trained U-Net Model
3. Flask Source Code

## Workflow

Dental panoramic X-ray  
→ Image preprocessing  
→ U-Net segmentation model  
→ Predicted tooth mask  
→ Export trained model  
→ Flask web app  
→ Upload new image  
→ Display original image, predicted mask, and overlay result  

## Environments

### Kaggle

Used for:

- Dataset access
- U-Net training
- GPU usage
- Model export

### VS Code

Used for:

- Flask app development
- File organization
- Documentation
- Future iHIS integration preparation

## Future Integration

This project starts as a standalone academic assignment, but it should remain suitable for later integration into the iHIS Dentistry Module.

The AI model should not directly modify any database.

In the future iHIS version, the segmentation output should be linked to a dental image record and reviewed by a dentist before clinical use.
