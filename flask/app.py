from flask import request, Response, Flask
from flask_cors import CORS
import requests
from urllib.parse import urlparse, parse_qs
import logging
import json
from elasticsearch import Elasticsearch
from config import MOCK_HEADERS, ELASTICSEARCH_HOST, MOCK_CLASSIFICATION, PROPERTY_FILES, SPARQL_ENDPOINT, PORT, HOST
from utility import build_ids_query, build_classifications, build_mediawiki_dicts_es, build_mock_stats_dict, build_entity_dict, build_wbsearch_dicts_es


app = Flask(__name__)
cors = CORS(app, resources=r'/*')
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


print("# Begin Loading Property File Info")
for file in PROPERTY_FILES:
    MOCK_CLASSIFICATION.update(build_classifications(file))
print("# Done Loading Property File Info")
es = Elasticsearch(ELASTICSEARCH_HOST)

@app.route("/", methods=["GET"])
def home_page():
    return "<h1>Homepage</h1>"

@app.route("/data/<path:data_path>", methods=["GET"])
def _data_proxy(*args, **kwargs):
    parsed_url = urlparse(request.url)
    queries = parse_qs(parsed_url.query)
    if parsed_url[2] == '/data/properties/usage.json':
        content = json.dumps(MOCK_CLASSIFICATION)
    elif parsed_url[2] == "/data/properties/classification.json":
        content = json.dumps(MOCK_CLASSIFICATION)
    elif parsed_url[2] == "/data/properties/urlpatterns.json":
        content = json.dumps({})
    elif parsed_url[2].startswith("/data/properties/relate"):
        content = json.dumps({})
    elif parsed_url[2].startswith('/data/classes/hierarchy'):
        content = json.dumps({})
    elif parsed_url[2] == '/data/statistics.json':
        content = json.dumps(build_mock_stats_dict())
    return Response(content.encode('utf-8'), 200, MOCK_HEADERS)

# @app.route("/data/properties/<path>", methods=["GET"])
# def _properties_proxy(*args, **kwargs):
#     parsed_url = urlparse(request.url)
#     queries = parse_qs(parsed_url.query)
#     # print("#DEBUG_usage_", counter, queries, parsed_url)
#     if parsed_url[2] == '/data/properties/usage.json':
#         content = json.dumps(MOCK_CLASSIFICATION)
#     elif parsed_url[2] == "/data/properties/classification.json":
#         content = json.dumps(MOCK_CLASSIFICATION)
#     elif parsed_url[2] == "/data/properties/urlpatterns.json":
#         content = json.dumps({})
#     elif parsed_url[2].startswith("/data/properties/relate"):
#         content = json.dumps({})
#     return Response(content.encode('utf-8'), 200, MOCK_HEADERS)


# @app.route("/data/classes/<path>", methods=["GET"])
# def _hierarchy_proxy(*args, **kwargs):
#     parsed_url = urlparse(request.url)
#     queries = parse_qs(parsed_url.query)
#     # print("#DEBUG_hierarchy_", counter, queries, parsed_url)
#     if parsed_url[2].startswith('/data/classes/hierarchy'):
#         content = json.dumps({})
#     return Response(content.encode('utf-8'), 200, MOCK_HEADERS)


# @app.route("/data/<path>", methods=["GET"])
# def _stats_proxy(*args, **kwargs):
#     parsed_url = urlparse(request.url)
#     queries = parse_qs(parsed_url.query)
#     #print("#DEBUG_data_",queries, parsed_url)
#     if parsed_url[2] == '/data/statistics.json':
#         content = json.dumps(build_mock_stats_dict())
#     return Response(content.encode('utf-8'), 200, MOCK_HEADERS)



@app.route("/entity/", methods=["GET"])
def _wiki_proxy(*args, **kwargs):
    parsed_url = urlparse(request.url)
    queries = parse_qs(parsed_url.query)
    action = queries["action"][0]
    if action == "wbgetentities":
        keys = queries["ids"][0].split("|")
        res_dict = build_mediawiki_dicts_es(es, keys)
        return Response(json.dumps(res_dict).encode('utf-8'), 200, MOCK_HEADERS)
    elif action == "wbsearchentities":
        if "search" in queries:
            res_dict = build_wbsearch_dicts_es(es, queries["search"][0])
        else:
            res_dict = {}
        return Response(json.dumps(res_dict).encode('utf-8'), 200, MOCK_HEADERS)
    else:
        raise NotImplementedError


@app.route("/sparql/", methods=["GET"])
def _sparql_proxy(*args, **kwargs):
    parsed_url = urlparse(request.url)
    queries = parse_qs(parsed_url.query)
    resp = requests.request(
        method=request.method,
        url=request.url.replace("/sparql", "").replace(
            request.host_url, SPARQL_ENDPOINT),
        headers={key: value for (key, value)
                 in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=True)
    return Response(resp.content, resp.status_code, MOCK_HEADERS)


# Run server
if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
