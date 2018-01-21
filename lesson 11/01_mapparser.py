#!~/envs/udacity_python3_mongodb

"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the
tag name as the key and number of times this tag can be encountered in
the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""

import xml.etree.cElementTree as ET
from collections import defaultdict
import pprint

# Global variables
dataset_dir = 'datasets/'
dataset_file = dataset_dir + 'example.osm'


def count_tags(filename):
    tags = defaultdict(int)
    for (event, element) in ET.iterparse(filename):
        tags[element.tag] += 1
    return tags


def test():
    tags = count_tags(dataset_file)
    pprint.pprint(tags)
    assert tags == {
        'bounds': 1,
        'member': 3,
        'nd': 4,
        'node': 20,
        'osm': 1,
        'relation': 1,
        'tag': 7,
        'way': 1,
    }


if __name__ == '__main__':
    test()
