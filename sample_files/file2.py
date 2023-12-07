# import fitz
# from PIL import Image
# import os
#
# file_path = 'image_pdf.pdf'
# pdf_file = fitz.open(file_path)
# pages_nums = len(pdf_file)
# image_list = []
#
# for page_num in range(pages_nums):
#     page_content = pdf_file[page_num]
#     image_list.append(page_content.get_images())
#
# # print(image_list)
#
#
#
# if len(image_list) == 0:
#     raise ValueError("No images found....")
#
# # Save all the extracted images
# for i, image in enumerate(image_list, start=1):
#     # Extract the image object number
#     xref = image[0]
#     # Extract image
#     base_image = pdf_file.extract_image(xref)
#     # Store image bytes
#     image_bytes = base_image['image']
#     # Store image extension
#     image_ext = base_image['ext']
#     # Generate image file name
#     image_name = str(i) + '.' + image_ext
#     # Save image
#     with open(os.path.join('/images', image_name), 'wb') as image_file:
#         image_file.write(image_bytes)
#         image_file.close()
# print(pdf_file[0].get_text())
# print(pdf_file[0].get_images())


import io
from PIL import Image
import pytesseract
import fitz  # PyMuPDF

count = 1


def extract_text(pdf_document):
    pdf_document = fitz.open(pdf_document)
    # Iterate through each page in the document
    text = ""
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]

        # Get the images on the page
        images = page.get_images(full=True)

        # Iterate through each image on the page
        for img_index, img_info in enumerate(images):
            img_index += 1  # Image index starts from 1
            image_index = img_info[0]
            base_image = pdf_document.extract_image(image_index)

            # Convert image bytes to a format that Tesseract can process
            image_bytes = base_image["image"]
            image_pil = Image.open(io.BytesIO(image_bytes))

            # Use pytesseract to extract text from the image
            image_text = pytesseract.image_to_string(image_pil)
            text+=image_text

    return text


text = extract_text("image_pdf.pdf")
print(text)

