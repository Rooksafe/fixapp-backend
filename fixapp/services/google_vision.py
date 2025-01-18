from google.cloud import vision

def analyze_id_card(image_path):
    """Analyze an ID card using Google Cloud Vision API."""
    client = vision.ImageAnnotatorClient()
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
        image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(f"Google Vision API error: {response.error.message}")

    return texts[0].description if texts else None
