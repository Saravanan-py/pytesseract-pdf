# import PdfDocument as PdfDocument
# from PIL import Image
# from pytesseract import pytesseract
# import os

# path_to_tessaract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
# path_to_image = r'images/image4.jpg'
#
# pytesseract.tesseract_cmd = path_to_tessaract
#
#
#
# for root, dirs, file_names in os.walk(path_to_image):
#     for file_name in file_names:
#         image = Image.open(path_to_image + file_name)
#         text = pytesseract.image_to_string(image)
#         print(text)
#
# print(pytesseract.image_to_string(path_to_image, lang = 'eng'))
a = (1,2,3,4)
print(a[0])