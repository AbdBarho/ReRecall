
# DB path
DB_PATH = 'db'
# Time between each screenshot in seconds
SLEEP_TIME = 60
# Prompt for generating descriptions of screenshots
IMAGE_DESCRIPTION_PROMPT = 'This is a screenshot of a desktop, describe what you see, what windows or programs are open, and what is the user doing. If there is a web browser open, describe the contents of the web page. refrain from using the word "screenshot" or "desktop" in your description.'
# The model for generating descriptions of screenshots
IMAGE_DESCRIPTION_MODEL = 'llava-phi3:3.8b-mini-q4_0'
# for vector embeddings of descriptions
EMBEDDING_MODEL = 'mxbai-embed-large'

