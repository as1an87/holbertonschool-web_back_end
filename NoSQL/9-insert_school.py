#!/usr/bin/env python3
""" Function """


def insert_school(mongo_collection, **kwargs):
    """Return"""
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
