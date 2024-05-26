import ollama
from typing import List

def generate_description(model: str, prompt: str, image: bytes) -> str:
  result = ollama.generate(model=model, prompt=prompt, images=[image])
  description = result['response'].strip()
  return description

def generate_embedding(model: str, prompt: str) -> List[float]:
  response = ollama.embeddings(model=model, prompt=prompt)
  return response['embedding']
