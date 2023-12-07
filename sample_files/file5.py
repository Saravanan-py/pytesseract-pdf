# import openai
# import os
#
# openai.api_key = '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'
#
# def get_completion(prompt, model="gpt-3.5-turbo"):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0, # this is the degree of randomness of the model's output
#     )
#     return response.choices[0].message["content"]
#
# def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=temperature, # this is the degree of randomness of the model's output
#     )
#     #     print(str(response.choices[0].message))
#     return response.choices[0].message["content"]

import faiss
import numpy as np

# Generate some random data
data = np.random.rand(1000, 128).astype('float32')

# Create an index
index = faiss.IndexFlatL2(128)

# Add data to the index
index.add(data)

# Query for the nearest neighbors
query_vector = np.random.rand(1, 128).astype('float32')
k = 5  # Number of neighbors to retrieve
distances, indices = index.search(query_vector, k)

print("Nearest neighbors:")
print(indices)
print("Distances:")
print(distances)
