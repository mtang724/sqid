import utility
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
print(utility.build_wbsearch_dicts_es(es, "product"))
