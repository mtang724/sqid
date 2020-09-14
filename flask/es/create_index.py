from elasticsearch import Elasticsearch
from config import MAPPING_FILE, ELASTICSEARCH_HOST, INDEX
client = Elasticsearch(ELASTICSEARCH_HOST)
try:
    client.indices.delete(index=INDEX)
except:
    pass
client.indices.create(index=INDEX, body=MAPPING_FILE)
