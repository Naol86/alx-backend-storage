#!/usr/bin/env python3
'''
    using python list mongo collection
'''


def list_all(mongo_collection):
    '''
        return the list of all documents in a collection
    '''

    return [doc for doc in mongo_collection.find()]
