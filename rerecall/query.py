import argparse

from utils.db import collection
from utils.ml import generate_embedding
from config import EMBEDDING_MODEL

def query(n_results: int, query: str):
  results = collection.query(
    n_results=n_results,
    query_embeddings=[generate_embedding(EMBEDDING_MODEL, query)],
  )
  documents = results['documents'][0]
  ids = results['ids'][0]
  for (_id, doc) in zip(ids, documents):
    print(doc)
    print(_id)
    print("----")

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Query for screenshots in the database')
  parser.add_argument('query', type=str, nargs=argparse.REMAINDER, help='The query to search for')
  parser.add_argument('-n', '--num-results', type=int, help='How many results to return', default=2)
  args = parser.parse_args()
  query(args.num_results, ' '.join(args.query))
