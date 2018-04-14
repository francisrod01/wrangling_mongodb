#!~/envs/udacity_python3_mongodb

"""
Your task is to explore the data a bit more.
Before you process the data and add it into your database, you should check the
"k" value for each "<tag>" and see if there are any potential problems.

We have provided you with 3 regular expressions to check for certain patterns
in the tags. As we saw in the quiz earlier, we would like to change the data
model and expand the "add:street" type of keys to a dictionary like this:
{"address": {"street": "Some value"}}
So, we have to see if we have such tags, and if we have any tags with
problematic characters.
"""

import xml.etree.cElementTree as et
import pprint
import re

# Global variables
dataset_dir = 'datasets/'
dataset_file = dataset_dir + 'example.osm'

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*S')
problem_chars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    if element.tag == "tag":
        my_k = element.get('k')

        if problem_chars.search(my_k):
            if 'problem_chars' in keys:
                keys['problem_chars'] += 1
            else:
                keys['problem_chars'] = 1

        elif lower_colon.search(my_k):
            if 'lower_colon' in keys:
                keys['lower_colon'] += 1
            else:
                keys['lower_colon'] = 1

        elif lower.search(my_k):
            if 'lower' in keys:
                keys['lower'] += 1
            else:
                keys['lower'] = 1

        else:
            keys['other'] += 1

    return keys


def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problem_chars": 0, "other": 0}
    for _, element in et.iterparse(filename):
        keys = key_type(element, keys)

    return keys


def test():
    # You can use another testfile "map.osm" to look at your solution.
    # Note that the assertion below will be incorrect then.
    # Note as well that the test function here is only used in the Test Run;
    # when you submit, your code will be checked against a different dataset.
    keys = process_map(dataset_file)
    pprint.pprint(keys)
    assert keys == {'lower': 5, 'lower_colon': 0, 'other': 1, 'problem_chars': 1}


if __name__ == '__main__':
    test()
