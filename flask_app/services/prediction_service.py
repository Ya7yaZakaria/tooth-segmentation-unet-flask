import os
import cv2
import numpy as np
import tensorflow as tf

from config import MODEL_PATH, IMG_SIZE, PREDICTION_FOLDER


_model = None


def load_segmentation_model():
    global _model

    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

        _model = tf.keras.models.load_model(MODEL_PATH, compile=False)

    return _model


def read_image_grayscale_windows_safe(image_path):
    image_bytes = np.fromfile(image_path, dtype=np.uint8)
    image = cv2.imdecode(image_bytes, cv2.IMREAD_GRAYSCALE)

    if image is None:
        raise ValueError(f"Could not read image: {image_path}")

    return image


def save_image_windows_safe(output_path, image_array):
    extension = os.path.splitext(output_path)[1]
    success, encoded_image = cv2.imencode(extension, image_array)

    if not success:
        raise ValueError(f"Could not encode image for saving: {output_path}")

    encoded_image.tofile(output_path)


def preprocess_image_for_prediction(image_path):
    image = read_image_grayscale_windows_safe(image_path)
    original_height, original_width = image.shape

    resized_image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    normalized_image = resized_image.astype("float32") / 255.0

    model_input = np.expand_dims(normalized_image, axis=-1)
    model_input = np.expand_dims(model_input, axis=0)

    return model_input, image, (original_width, original_height)


def create_overlay_image(original_grayscale_image, binary_mask):
    original_bgr = cv2.cvtColor(original_grayscale_image, cv2.COLOR_GRAY2BGR)

    overlay = original_bgr.copy()
    overlay[binary_mask > 0] = [0, 255, 0]

    blended = cv2.addWeighted(original_bgr, 0.75, overlay, 0.25, 0)

    return blended


def create_prediction_mask(image_path, output_filename, threshold=0.03):
    model = load_segmentation_model()

    model_input, original_image, original_size = preprocess_image_for_prediction(image_path)

    prediction = model.predict(model_input, verbose=0)
    prediction_mask = prediction[0, :, :, 0]

    binary_mask = (prediction_mask >= threshold).astype("uint8") * 255

    resized_mask = cv2.resize(
        binary_mask,
        original_size,
        interpolation=cv2.INTER_NEAREST
    )

    overlay_image = create_overlay_image(original_image, resized_mask)

    os.makedirs(PREDICTION_FOLDER, exist_ok=True)

    mask_output_path = os.path.join(PREDICTION_FOLDER, output_filename)
    overlay_filename = f"overlay_{output_filename}"
    overlay_output_path = os.path.join(PREDICTION_FOLDER, overlay_filename)

    save_image_windows_safe(mask_output_path, resized_mask)
    save_image_windows_safe(overlay_output_path, overlay_image)

    prediction_info = {
        "prediction_min": float(np.min(prediction_mask)),
        "prediction_max": float(np.max(prediction_mask)),
        "prediction_mean": float(np.mean(prediction_mask)),
        "threshold": threshold,
        "mask_output_path": mask_output_path,
        "overlay_output_path": overlay_output_path,
        "overlay_filename": overlay_filename,
    }

    return mask_output_path, overlay_output_path, prediction_info
