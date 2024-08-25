#!/usr/bin/env python3
"""Function"""


def schools_by_topic(mongo_collection, topic):
    """ Return """
    return [i for i in mongo_collection.find({"topics": topic})]
