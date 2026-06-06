from PIL import Image
import numpy as np


def analyze_wine_image(image: Image.Image) -> dict:
    image = image.convert("RGB")

    width, height = image.size

    resized_image = image.resize((224, 224))
    image_array = np.array(resized_image)

    mean_rgb = image_array.mean(axis=(0, 1))
    mean_red = mean_rgb[0]
    mean_green = mean_rgb[1]
    mean_blue = mean_rgb[2]

    brightness = np.mean(image_array)

    if brightness < 85:
        brightness_category = "dark"
    elif brightness < 170:
        brightness_category = "medium"
    else:
        brightness_category = "bright"

    if mean_red > mean_green and mean_red > mean_blue:
        dominant_color = "red/brown"
    elif mean_green > mean_red and mean_green > mean_blue:
        dominant_color = "green"
    elif mean_blue > mean_red and mean_blue > mean_green:
        dominant_color = "blue"
    else:
        dominant_color = "neutral"

    aspect_ratio = height / width

    if aspect_ratio > 1.4:
        shape_hint = "portrait-oriented image, which is common for bottle photos"
    else:
        shape_hint = "non-portrait image"

    dark_pixel_ratio = np.mean(image_array < 80)

    if dark_pixel_ratio > 0.45:
        bottle_hint = "The image contains many dark pixels, which may indicate a dark wine bottle or dark background."
    elif dark_pixel_ratio > 0.25:
        bottle_hint = "The image contains a moderate amount of dark regions."
    else:
        bottle_hint = "The image is mostly bright, so bottle detection may be less clear."

    return {
        "width": width,
        "height": height,
        "brightness": round(float(brightness), 2),
        "brightness_category": brightness_category,
        "dominant_color": dominant_color,
        "shape_hint": shape_hint,
        "dark_pixel_ratio": round(float(dark_pixel_ratio), 2),
        "bottle_hint": bottle_hint
    }


def generate_image_explanation(image_analysis: dict) -> str:
    explanation = (
        f"The uploaded image has a resolution of "
        f"{image_analysis['width']} x {image_analysis['height']} pixels. "
        f"The overall brightness is classified as {image_analysis['brightness_category']}. "
        f"The dominant color impression is {image_analysis['dominant_color']}. "
        f"The shape analysis suggests a {image_analysis['shape_hint']}. "
        f"{image_analysis['bottle_hint']}"
    )

    return explanation