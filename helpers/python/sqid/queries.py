QUERY_CLASSES = """
prefix wikibase: <http://wikiba.se/ontology#>
prefix wd: <http://www.wikidata.org/entity/>
prefix wdt: <http://www.wikidata.org/prop/direct/>
SELECT ?cl ?clLabel ?c
WITH { SELECT ?cl (COUNT(*) AS ?c) WHERE {
   ?i wdt:P31 ?cl
  } GROUP BY ?cl
} AS %classes
WHERE {
  INCLUDE %classes
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
    ?cl rdfs:label ?clLabel .
  }
}"""
QUERY_CLASSSES_FALLBACK = """
prefix wikibase: <http://wikiba.se/ontology#>
prefix wd: <http://www.wikidata.org/entity/>
prefix wdt: <http://www.wikidata.org/prop/direct/>
SELECT ?cl ?clLabel
WITH { SELECT DISTINCT ?cl WHERE {
    ?i wdt:P31 ?cl
  }
} AS %classes
WHERE {
  INCLUDE %classes
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
    ?cl rdfs:label ?clLabel .
  }
}"""
QUERY_PROPERTIES = """
prefix wikibase: <http://wikiba.se/ontology#>
prefix wd: <http://www.wikidata.org/entity/>
prefix wdt: <http://www.wikidata.org/prop/direct/>
SELECT ?id ?idLabel ?type
WITH { SELECT ?id ?type WHERE {
    ?id a wikibase:Property ;
          wikibase:propertyType ?type .
  }
} AS %properties
WHERE {
  INCLUDE %properties .
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
    ?id rdfs:label ?idLabel .
  }
}"""
QUERY_PROPERTY_USAGE = """
prefix wikibase: <http://wikiba.se/ontology#>
prefix wd: <http://www.wikidata.org/entity/>
prefix wdt: <http://www.wikidata.org/prop/direct/>
SELECT ?p (count(*) as ?c) WHERE {
  ?s ?p ?o .
} GROUP BY ?p ORDER BY DESC(?c)"""
