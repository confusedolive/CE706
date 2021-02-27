import csv
from elasticsearch import helpers, Elasticsearch
from constants import INDEX_NAME , DOCU_TYPE

es = Elasticsearch()
#no need to specify host as we are doing it locally
data_path = r'local path for data to be indexed'

def index_data():
    with open(data_path, encoding='utf8', mode='r') as f:
        reader = csv.DictReader(f)
        helpers.bulk(es, reader,index=INDEX_NAME, doc_type=DOCU_TYPE)
    
if __name__ == '__main__':
    es.indices.create(index=INDEX_NAME, ignore=400)
    index_data()

