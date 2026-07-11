# Dataset Findings

## Dataset

Tufts Radiographs dataset from Kaggle.

## Observed Structure

```text
TUFTS/
├── Radiographs/
│   ├── training_images/
│   └── testing_images/
└── bboxes/
    ├── trainBoundryBoxes.csv
    └── testBoundryBoxes.csv
```

## Image Counts

```text
Training images: 980
Testing images: 20
Annotated training images: 335
```

## Annotation Files

```text
trainBoundryBoxes.csv
testBoundryBoxes.csv
```

## Annotation Columns

```text
imageID
class
x-min
y-min
width
height
```

## Important Finding

No ready-made pixel-level tooth segmentation masks were found.

The available annotations are bounding boxes.

## Consequence

Bounding boxes will be converted into weak binary masks for educational U-Net training.
