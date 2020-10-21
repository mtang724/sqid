import argparse

parser = argparse.ArgumentParser(description='Enter congiguration parameters')
parser.add_argument('--is_generate', type=bool, help='is_generate', default=False)
args = parser.parse_args()

HOST = "localhost"
SQID_PORT = 8052
SPARQL_PORT = 11102
FLASK_PORT = 5556
ES_INDEX = "kgtk_files"
ELASTICSEARCH_PORT = 9200
is_generate = args.is_generate

# Flask application config
PROPERTY_FILES = [
	"flask_data/wikidata_properties.tsv"
]
ES_INDEX = ES_INDEX
ELASTICSEARCH_HOST = "http://{}:{}".format(HOST, str(ELASTICSEARCH_PORT))
SPARQL_ENDPOINT = "http://{}:{}/proxy/wdqs/bigdata/namespace/wdq/sparql".format(HOST, str(SPARQL_PORT))
FLASK_PORT = FLASK_PORT
SQID_DOMAIN = "http://{}:{}/".format(HOST, SQID_PORT)

# ES config
ES_DATA_FOLDER_PATH = "/home/mingyuet/sqid/flask/es/es_data"


# Generate Endpoints for SQID
commonsEndpoint = 'https://commons.wikimedia.org/w/api.php'
wikidataEndpoint = 'http://{}:{}/entity/'.format(HOST, str(FLASK_PORT))
sparqlEndpoint = 'http://{}:{}/sparql/'.format(HOST, str(FLASK_PORT))
sqidEndpoint = 'http://{}:{}/data'.format(HOST, str(FLASK_PORT))
customDomain = 'http://{}:{}'.format(HOST, str(SQID_PORT))
MAX_SIMULTANEOUS_API_REQUESTS = 25
MAX_ENTITIES_PER_API_REQUEST = 50
MAX_SIMULTANEOUS_SPARQL_REQUESTS = 5

endpoints_text = "export const commonsEndpoint = '{}'\nexport const wikidataEndpoint = '{}'\nexport const sparqlEndpoint = '{}'\nexport const sqidEndpoint = '{}'\nexport const customDomain = '{}'\n"\
.format(commonsEndpoint, wikidataEndpoint, sparqlEndpoint, sqidEndpoint, customDomain)
endpoints_constrain = "export const MAX_SIMULTANEOUS_API_REQUESTS = {}\nexport const MAX_ENTITIES_PER_API_REQUEST = {}\nexport const MAX_SIMULTANEOUS_SPARQL_REQUESTS = {}\n"\
.format(str(MAX_SIMULTANEOUS_API_REQUESTS), str(MAX_ENTITIES_PER_API_REQUEST), str(MAX_SIMULTANEOUS_SPARQL_REQUESTS))

def write_sqid_endpoints(file_name, text):
	with open(file_name, "w") as f:
		f.write(text)
if is_generate == True:
    write_sqid_endpoints("src/api/endpoints.ts", endpoints_text + endpoints_constrain)

endpoints_js_prefix = """
"use strict";\n
exports.__esModule = true;\n
exports.MAX_SIMULTANEOUS_SPARQL_REQUESTS = exports.MAX_ENTITIES_PER_API_REQUEST = exports.MAX_SIMULTANEOUS_API_REQUESTS = exports.customDomain = exports.sqidEndpoint = exports.sparqlEndpoint = exports.wikidataEndpoint = exports.commonsEndpoint = void 0;\n
"""
endpoints_js_text = "exports.commonsEndpoint = '{}';\nexports.wikidataEndpoint = '{}';\nexports.sparqlEndpoint = '{}';\nexports.sqidEndpoint = '{}';\nexports.customDomain = '{}';\n"\
.format(commonsEndpoint, wikidataEndpoint, sparqlEndpoint, sqidEndpoint, customDomain)
endpoints_js_constrain = "exports.MAX_SIMULTANEOUS_API_REQUESTS = {};\nexports.MAX_ENTITIES_PER_API_REQUEST = {};\nexports.MAX_SIMULTANEOUS_SPARQL_REQUESTS = {};\n"\
.format(str(MAX_SIMULTANEOUS_API_REQUESTS), str(MAX_ENTITIES_PER_API_REQUEST), str(MAX_SIMULTANEOUS_SPARQL_REQUESTS))
if is_generate == True:
    write_sqid_endpoints("src/api/dist/endpoints.js", endpoints_js_prefix + endpoints_js_text + endpoints_js_constrain)

