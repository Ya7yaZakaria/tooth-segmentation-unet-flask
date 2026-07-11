# Weak Mask Decision

## Problem

The original assignment goal is tooth segmentation using U-Net.

However, the selected dataset provides bounding box annotations instead of manually prepared segmentation masks.

## Decision

Bounding boxes will be converted into weak binary masks.

Each generated mask will contain:

```text
0 = background
1 = weak target region from bounding box
```

Visually:

```text
Black background
White rectangular annotation regions
```

## Important Limitation

These generated masks are not true manual tooth segmentation masks.

They are pseudo masks created for educational U-Net training.

## Correct Wording

Use:

```text
weak binary masks
pseudo masks
weak-mask segmentation prototype
bounding-box-derived masks
```

Avoid:

```text
true tooth segmentation masks
manual ground truth tooth masks
clinical tooth boundary segmentation
```

## Final Workflow

```text
Dental radiograph
+
Bounding box CSV
↓
Generate weak binary mask
↓
Train U-Net prototype
↓
Export model
↓
Deploy with Flask
```
