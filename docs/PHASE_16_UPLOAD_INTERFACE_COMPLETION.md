# Phase 16 Completion — Flask Upload Interface

## Status
Completed.

## Goal
Add image upload support to the Flask dental segmentation application.

## What was done
- Added POST handling to the Flask home route.
- Added allowed file extension validation.
- Added secure filename handling.
- Saved uploaded images into the static uploads folder.
- Updated the HTML page with an upload form.
- Displayed the uploaded image preview after upload.

## Upload folder
flask_app/static/uploads

## Current capability
The user can upload a PNG, JPG, or JPEG dental radiograph and preview it in the Flask web page.

## Next phase
Phase 17 will load the trained U-Net model and generate a predicted weak segmentation mask.
