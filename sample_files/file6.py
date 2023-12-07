# import base64
# import fitz
#
# with open("sample2.pdf", "rb") as pdf_file:
#     encoded_string = base64.b64encode(pdf_file.read()).decode("utf-8")
#
# import openai
# import os
#
# openai.api_key = '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'
#
#
# def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=temperature
#     )
#     return response.choices[0].message.content
#
#
#
# def extract_text_from_base64_pdf(base64_content):
#     try:
#         # Decode base64 content
#         pdf_content = base64.b64decode(base64_content)
#
#
#         # Create a PDF document object
#         doc = fitz.open(stream=pdf_content)
#
#         text = ""
#
#         # Iterate through pages and extract text
#         for page_number in range(doc.page_count):
#             page = doc[page_number]
#             text += page.get_text()
#
#         return text
#     except Exception as e:
#         print(f"Error extracting text: {e}")
#         return None
#
#
#
# text = extract_text_from_base64_pdf(encoded_string)
#
# if text:
#     print("Extracted Text:")
#     # print(text)
# else:
#     print("Text extraction failed.")
#
# prompt = f"""
#               print the name used in pdf that has given this certificate from given data with the " \
#          ```{text}```text delimited by triple backticks """
#
# response = get_completion(prompt)
# print(response)
#
# import base64
# import fitz
# import io
# import pytesseract
# import openai
# from PIL import Image
# # Set your OpenAI API key
# openai.api_key = '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'
#
#
# def extract_text_from_base64_pdf(base64_content):
#     try:
#         # Decode base64 content
#         pdf_content = base64.b64decode(base64_content)
#
#         # Create a PDF document object
#         doc = fitz.open(stream=pdf_content)
#
#         text = ""
#
#         # Iterate through pages and extract text
#         for page_number in range(doc.page_count):
#             page = doc[page_number]
#             text += page.get_text()
#
#         return text
#     except Exception as e:
#         print(f"Error extracting text: {e}")
#         return None
#
#
# def extract_text_from_base64_pdf(base64_content):
#     try:
#         pdf_content = base64.b64decode(base64_content)
#         pdf_document = fitz.open(stream = pdf_content)
#         # Iterate through each page in the document
#         text = ""
#         for page_number in range(pdf_document.page_count):
#             page = pdf_document[page_number]
#
#             # Get the images on the page
#             images = page.get_images(full=True)
#
#             # Iterate through each image on the page
#             for img_index, img_info in enumerate(images):
#                 img_index += 1  # Image index starts from 1
#                 image_index = img_info[0]
#                 base_image = pdf_document.extract_image(image_index)
#
#                 # Convert image bytes to a format that Tesseract can process
#                 image_bytes = base_image["image"]
#                 image_pil = Image.open(io.BytesIO(image_bytes))
#
#                 # Use pytesseract to extract text from the image
#                 image_text = pytesseract.image_to_string(image_pil)
#                 text+=image_text
#         return text
#     except Exception as e:
#         print(f"Error extracting text: {e}")
#         return None
#
#
#
#
# def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=temperature
#     )
#     return response.choices[0].message.content
#
#
# def process_pdf_and_query(pdf_file_path):
#     # Read the PDF file and encode it to base64
#     with open(pdf_file_path, "rb") as pdf_file:
#         encoded_string = base64.b64encode(pdf_file.read()).decode("utf-8")
#
#     # Extract text from the base64-encoded PDF
#     extracted_text = extract_text_from_base64_pdf(encoded_string)
#
#
#
#     # Create a prompt using the extracted text
#     prompt = f"""
#     print the name of the competition with json format 'name' as key and competition name as value from given
#     data with the text delimited by triple backticks" \
#     ```{extracted_text}```
#     """
#
#     # Query OpenAI with the prompt
#     response = get_completion(prompt)
#     return response
#
#
# # Example usage:
# pdf_file_path = "sample2.pdf"
# result = process_pdf_and_query(pdf_file_path)
# print(result)

import base64
import fitz
import io
import pytesseract
import openai
from PIL import Image

# Set your OpenAI API key
openai.api_key = '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'

def extract_text_from_base64_pdf(base64_content):
    try:
        pdf_content = base64.b64decode(base64_content)
        pdf_document = fitz.open(stream=pdf_content)
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
                text += image_text
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

def process_pdfs_and_query(pdf_file_paths):
    responses = []
    for pdf_file_path in pdf_file_paths:
        # Read the PDF file and encode it to base64
        with open(pdf_file_path, "rb") as pdf_file:
            encoded_string = base64.b64encode(pdf_file.read()).decode("utf-8")

        # Extract text from the base64-encoded PDF
        extracted_text = extract_text_from_base64_pdf(encoded_string)

        # Create a prompt using the extracted text
        prompt = f"""
        print the name of the competition with json format 'name' as key and competition name as value from given 
        data with the text delimited by triple backticks" \
        ```{extracted_text}```
        """

        # Query OpenAI with the prompt
        response = get_completion(prompt)
        responses.append(response)

    return responses

# Example usage with multiple PDFs:
pdf_file_paths = ["image_pdf.pdf", "image_pdf1.pdf", "sample2.pdf"]
results = process_pdfs_and_query(pdf_file_paths)
print(results)

for result in results:
    print(result)
