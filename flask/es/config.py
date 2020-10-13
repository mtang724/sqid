ELASTICSEARCH_HOST = "localhost"
INDEX = "kgtk"
DATA_FOLDER_PATH = "/instancestore/sqid/flask/es/es_data"
MAPPING_FILE = {
    "mappings": {
        # mapping type has been removed in elasticsearch7
        "dynamic": False,
        "properties": {
            "labels": {
                "dynamic": True,
                "properties": {
                    "en": {
                        "properties": {
                            "language": {"type": "text",
                                         "index": False},
                            "value": {"type": "text",
                                      "analyzer": "english"}
                        }
                    }
                }
            },
            "descriptions": {
                "dynamic": True,
                "properties": {
                    "en": {
                        "properties": {
                            "language": {"type": "text",
                                         "index": False},
                            "value": {"type": "text",
                                      "analyzer": "english"}
                        }
                    }
                }},
            "aliases": {
                "type": "object",
                "enabled": False},
            "claims": {
                "type": "object",
                "enabled": False
            },
            "sitelinks": {
                "type": "object",
                "enabled": False
            },
            "pageid": {
                "type": "integer",
                "index": False
            },
            "ns": {
                "type": "integer",
                "index": False
            },
            "title": {
                "type": "text",
                "index": False
            },
            "lastrevid": {
                "type": "text",
                "index": False
            },
            "type": {
                "type": "text",
                "index": False
            },
            "datatype": {
                "type": "text",
                "index": False
            },
            "id": {
                "type": "keyword"
            }
        }

    }
}