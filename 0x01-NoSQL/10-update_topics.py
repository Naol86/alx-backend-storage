#!/usr/bin/env python3
'''
    update a document in a collection
'''


def update_topics(mongo_collection, name, topics):
    mongo_collection.updata_many({"name": name}, {"$set": {"topics": topics}})
