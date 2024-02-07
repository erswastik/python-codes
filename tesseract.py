from PyPDF2 import PdfReader
import pytesseract
from wand.image import Image as WandImage
import io

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_pdf_with_images(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]

            # Convert the page content to an image using Wand
            image_blob = page.extract_text().encode('utf-8')
            with WandImage(blob=image_blob, format='png') as img:
                # Extract text from the image
                text += extract_text_from_image(img)

    return text

# Replace 'your_pdf_file.pdf' with the actual path to your PDF file
pdf_text_from_images = extract_text_from_pdf_with_images('c:/Users/Admin/Desktop/QP-CDS2-20-GENERAL_KNOWLEDGE.pdf')

# Now 'pdf_text_from_images' contains the extracted text from the images in the PDF file
print(pdf_text_from_images)
