import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
PREDICTION_FOLDER = os.path.join(BASE_DIR, "static", "predictions")
MODEL_PATH = os.path.join(BASE_DIR, "model", "unet_weak_mask_segmentation.keras")

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
MAX_CONTENT_LENGTH = 10 * 1024 * 1024
IMG_SIZE = 256
