
from config import ES_INDEX, DOMAIN

def build_mediawiki_dicts_es(es, keys: list) -> dict:
    # from a list of dict, build a returned dict
    temp_dict = {"entities": {}, "success": 1}
    result = es.search(index=ES_INDEX, body=build_ids_query(keys))
    hits = result["hits"]["hits"]
    for hit in hits:
        js = hit["_source"]
        key = js["id"]
        temp_dict["entities"][key] = js
    if temp_dict["entities"] == {}:
        temp_dict = {"entities": {}, "missing": 1}
    return temp_dict


def build_ids_query(_ids: list):
    return {
        "size": 10000,
        "query": {
            "terms": {
                "id": _ids
            }
        }
    }


def build_classifications(property_file_path: str):
    mutable_mapping = {}
    with open(property_file_path, "r") as fp:
        for line_number, line in enumerate(fp.readlines()):
            if line.split("\t")[1] == "data_type" or line.split("\t")[1] == "property_type":
                p_id = line.split("\t")[0][1:]
                data_type = line.split("\t")[2].strip()
                if data_type == "external-identifier":
                    mutable_mapping[p_id] = "i"
                else:
                    mutable_mapping[p_id] = "o"
    return mutable_mapping

def build_mock_stats_dict():
    stats_dict = {
        "itemStatistics": {
            "cAliases": 0,
            "cDesc": 0,
            "cStmts": 0,
            "c": 0,
            "cLabels": 0
        },
        "entityCount": 0,
        "sites": {},
        "classUpdate": "2020-05-20T15:13:10+0000",
        "dumpDate": "20200511",
        "siteLinkCount": "73531601",
        "propertyUpdate": "2020-05-20T16:12:11+0000",
        "propertyStatistics": {
            "cAliases": 0,
            "cDesc": 0,
            "cStmts": 0,
            "c": 0,
            "cLabels": 0
        }
    }
    return stats_dict

def build_entity_dict(hit: dict, search_string: str, source:str):
    entity_dict = {
        "id": hit["id"],
        "title": hit["id"],
        "pageid": hit["pageid"],
        "repository": "local",
        "url": "{}/entity/{}".format(DOMAIN, hit["id"]),
        "concepturi": "{}/entity/{}".format(DOMAIN,hit["id"]),
        "label": hit["labels"]["en"]["value"],
        "description": hit["descriptions"]["en"]["value"] if "en" in hit["descriptions"] else "",
        "match": {
            "type": source, "language": "en", "text": search_string
        }
    }
    return entity_dict

def build_wbsearch_dicts_es(es, search_string: str):
    # original
    temp_dict = {"searchinfo": {"search": search_string}, "search": []}
    # local es version
    es_query = {
        "query": {
            "match_phrase": {
                "labels.en.value": search_string
            }
        }
    }
    result_label = es.search(index=ES_INDEX, body=es_query)
    es_query = {
        "query":
            {"match_phrase": {
                "descriptions.en.value": search_string
            }
            }
    }
    result_desc = es.search(index=ES_INDEX, body=es_query)

    hits_label = result_label["hits"]["hits"]
    for hit in hits_label:
        obj = hit["_source"]
        if obj["id"].startswith("Q"):
            entity_dict = build_entity_dict(obj, search_string, "label")
            temp_dict["search"].append(entity_dict)

    hits_desc = result_desc["hits"]["hits"]
    for hit in hits_desc:
        obj = hit["_source"]
        if obj["id"].startswith("Q"):
            entity_dict = build_entity_dict(obj, search_string, "description")
            temp_dict["search"].append()
    return temp_dict