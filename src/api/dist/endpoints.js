"use strict";
exports.__esModule = true;
exports.MAX_SIMULTANEOUS_SPARQL_REQUESTS = exports.MAX_ENTITIES_PER_API_REQUEST = exports.MAX_SIMULTANEOUS_API_REQUESTS = exports.customDomain = exports.sqidEndpoint = exports.sparqlEndpoint = exports.wikidataEndpoint = exports.commonsEndpoint = void 0;
exports.commonsEndpoint = 'https://commons.wikimedia.org/w/api.php'; // for image
exports.wikidataEndpoint = 'http://localhost:5556/entity/';
exports.sparqlEndpoint = 'http://localhost:5556/sparql/';
exports.sqidEndpoint = 'http://localhost:5556/data';
exports.customDomain = 'http://sitaware.isi.edu:5556';
exports.MAX_SIMULTANEOUS_API_REQUESTS = 25;
exports.MAX_ENTITIES_PER_API_REQUEST = 50;
exports.MAX_SIMULTANEOUS_SPARQL_REQUESTS = 5;