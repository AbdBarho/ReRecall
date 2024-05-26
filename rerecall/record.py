from time import time_ns
from os import makedirs
from datetime import datetime
from time import sleep
import ollama


from config import IMAGE_DESCRIPTION_MODEL, EMBEDDING_MODEL, IMAGE_DESCRIPTION_PROMPT, SLEEP_TIME
from utils.screenshot import get_screenshots
from utils.ml import generate_description, generate_embedding
from utils.db import collection


def run_iteration():
  timestamp = str(int(time_ns() / 1000))
  now = datetime.now()
  print(now, "Taking screenshots")
  screenshots = get_screenshots(timestamp)
  print(now, "Generating descriptions")
  descriptions = [generate_description(IMAGE_DESCRIPTION_MODEL, IMAGE_DESCRIPTION_PROMPT, screenshot.base64) for screenshot in screenshots]
  print(now, "Generating embeddings")
  embeddings = [generate_embedding(EMBEDDING_MODEL, description) for description in descriptions]
  print(now, "Saving to DB")
  for screenshot, description, embedding in zip(screenshots, descriptions, embeddings):
    collection.add(
      ids=[screenshot.filename],
      embeddings=[embedding],
      documents=[description],
    )
  print(now, "Finished iteration")

def loop():
  while True:
    run_iteration()
    print("Sleeping for", SLEEP_TIME, "seconds")
    sleep(SLEEP_TIME)


if __name__ == "__main__":
  print("Pulling model, might take a while...")
  ollama.pull(IMAGE_DESCRIPTION_MODEL)
  print("Pulling embedding model, might take a while...")
  ollama.pull(EMBEDDING_MODEL)

  makedirs("screenshots", exist_ok=True)
  loop()
