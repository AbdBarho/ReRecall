from chromadb import Collection, PersistentClient
from chromadb.config import Settings
from config import DB_PATH

client = PersistentClient(DB_PATH, Settings(anonymized_telemetry=False))
collection: Collection = client.get_or_create_collection(name="screenshots")
