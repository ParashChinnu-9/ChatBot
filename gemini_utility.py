import os
import json
from PIL import Image
import google.generativeai as genai

# Working directory path
working_dir = os.path.dirname(os.path.abspath(__file__))

# Path of config_data file
config_file_path = f"{working_dir}/config.json"
config_data = json.load(open(config_file_path))

# Loading the GOOGLE_API_KEY
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

# Configuring google.generativeai with the API key
genai.configure(api_key=GOOGLE_API_KEY)

# Load the Gemini-1.5-Flash model
def load_gemini_flash_model():
    gemini_flash_model = genai.GenerativeModel("gemini-1.5-flash")
    return gemini_flash_model

# Get response from Gemini-1.5-Flash for image captioning
def gemini_flash_vision_response(prompt, image):
    gemini_flash_model = genai.GenerativeModel("gemini-1.5-flash")
    response = gemini_flash_model.generate_content([prompt, image])
    result = response.text if hasattr(response, 'text') else "No response text found"
    return result

# Get response from embeddings model - text to embeddings
def embeddings_model_response(input_text):
    embedding_model = "models/embedding-001"
    embedding = genai.embed_content(
        model=embedding_model,
        content=input_text,
        task_type="retrieval_document"
    )
    embedding_list = embedding["embedding"]
    return embedding_list

# Get response from Gemini-1.5-Flash - text to text
def gemini_flash_response(user_prompt):
    gemini_flash_model = genai.GenerativeModel("gemini-1.5-flash")
    response = gemini_flash_model.generate_content(user_prompt)
    result = response.text if hasattr(response, 'text') else "No response text found"
    return result

# Test cases for demonstration (commented out)
# Uncomment these lines to test the functionality

# Text response example
# result = gemini_flash_response("What is Machine Learning?")
# print(result)
# print("-" * 50)

# Image captioning example
# image_path = "test_image.png"
# if os.path.exists(image_path):
#     image = Image.open(image_path)
#     result = gemini_flash_vision_response("Write a short caption for this image", image)
#     print(result)
#     print("-" * 50)
# else:
#     print(f"File not found: {image_path}")

# Embeddings example
# result = embeddings_model_response("Machine Learning is a subset of Artificial Intelligence")
# print(result)
