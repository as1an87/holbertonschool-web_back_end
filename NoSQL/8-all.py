#!/usr/bin/env python3
""" Function """

import pymongo


def list_all(mongo_collection):
    """Return """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
