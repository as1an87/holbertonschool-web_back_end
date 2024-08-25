#!/usr/bin/env python3
""" Function """


def update_topics(mongo_collection, name, topics):
    """Return"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
