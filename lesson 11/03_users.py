#!~/envs/udacity_python3_mongodb

"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

import xml.etree.cElementTree as et
import pprint
import re

# Global variables
dataset_dir = 'datasets/'
dataset_file = dataset_dir + 'example.osm'


def get_user(element):
    return


def process_map(filename):
    users = set()
    for _, element in et.iterparse(filename):
        pass

    return users


def test():
    users = process_map(dataset_file)
    pprint.pprint(users)
    assert len(users) == 6


if __name__ == '__main__':
    test()
