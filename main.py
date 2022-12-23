import time

import schedule

import setting
from crawl.Crawl import Crawl
from storage.mongo.WithMongo import WithMongo


def run():
    data = Crawl().crawl(url=setting.url, headers=setting.headers)
    mongo_client = WithMongo().get_mongo(mongo_host=setting.mongo_host, mongo_port=setting.mongo_port)
    database = mongo_client[setting.database]
    for metadata in data:
        WithMongo().save_mongo(database=database, collection=setting.collection, metadata=metadata)


if __name__ == '__main__':

    schedule.every(60).seconds.do(run)
    while True:
        schedule.run_pending()
        time.sleep(1)
