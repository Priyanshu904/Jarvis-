# modules/ocr_tools.py
import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    """
    This function takes the path to an image and uses Tesseract to extract text.
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error: {str(e)}"
