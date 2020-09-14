
from elasticsearch import Elasticsearch, helpers
import json
from tqdm import tqdm
from glob import glob
from config import MAPPING_FILE, ELASTICSEARCH_HOST, INDEX, DATA_FOLDER_PATH
client = Elasticsearch(ELASTICSEARCH_HOST)

json_files = glob(DATA_FOLDER_PATH + "/*.jsonl")

for json_file in tqdm(json_files):
    with open(json_file,"r") as fp:
        docs = []
        for idx, js in tqdm(enumerate(fp)):
            doc = list(json.loads(js).values())[0]
            docs.append(doc)
            if idx != 0 and idx%10000 == 0:
                res = helpers.bulk(client,actions=docs,index=INDEX)
                print("loaded {}".format(idx))
                docs = []
