#!~/envs/udacity_python3_mongodb
# -*- coding: utf-8 -*-
"""
In this problem set you work with another type of infobox data, audit it,
clean it, come up with a data model, insert it into MongoDB and then run some
queries against your database. The set contains data about Arachnid lass
animals.

Your task in this exercise is to parse the file, process only the fields that
are listed in the FIELDS dictionary as keys, and return a list of dictionaries
of cleaned values.

The following things should be done:
- keys of the dictionary changed according to the mapping in FIELDS dictionary
- trim out redundant description in parenthesis from the 'rdf-schema#label'
  field, like "(spider)"
- if 'name' is "NULL" or contains non-alphanumeric characters, set it to the
  same value as 'label'
- if there is a value in 'synonym', it should be converted to an array (list)
  by stripping the "{}" characters and splitting the string on "|". Rest of the
  cleanup is up to you, e.g. removing "*" prefixes etc. If there is a singular
  strip leading and ending whitespace from all fields, if there is any
  the output structure should be as follows:

[ { 'label': 'Argiope',
    'uri: 'http://dbpedia.org/resource/Argiope_(spider)',
    'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
    'name': 'Argiope',
    'synonym': ["One", "Two"],
    'classification': {
      'family': 'Orb-weaver spider',
      'class': 'Arachnid',
      'phylum': 'Arthropod',
      'order': 'Spider',
      'kingdom': 'Animal',
      'genus': None
    }
  },
  { 'label': ..., }, ...
]

* None that the value associated with the classification key is a dictionary
  with taxonomic labels.
"""

import codecs
import csv
import json
import pprint
import re

DIR_DATA = 'datasets/'
DATAFILE = DIR_DATA + 'arachnid.csv'
FIELDS = {
    'rdf-schema#label': 'label',
    'URI': 'uri',
    'rdf-schema#comment': 'description',
    'synonym': 'synonym',
    'name': 'name',
    'family_label': 'family',
    'class_label': 'class',
    'phylum_label': 'phylum',
    'order_label': 'order',
    'kingdom_label': 'kingdom',
    'genus_label': 'genus'
}


def process_file(filename, fields):
    process_fields = fields.keys()
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = next(reader)

        for line in reader:
            # YOUR CODE HERE.
            pass

    return data


def parse_array(v):
    if (v[0] == "{") and (v[-1] == "}"):
        v = v.lstrip("{")
        v = v.rstrip("}")
        v_array = v.split("|")
        v_array = [i.strip() for i in v_array]
        return v_array
    return [v]


def test():
    data = process_file(DATAFILE, FIELDS)
    print("Your first entry:")
    pprint.pprint(data[0])
    first_entry = {
        "synonym": None,
        "name": "Argiope",
        "classification": {
            "kingdom": "Animal",
            "family": "Orb-weaver spider",
            "order": "Spider",
            "phylum": "Arthropod",
            "genus": None,
            "class": "Arachnid"
        },
        "uri": "http://dbpedia.org/resource/Argiope_(spider)",
        "label": "Argiope",
        "description": "The genus Argiope includes rather large and spectacular spiders that often... ",
    }

    assert len(data) == 76
    assert data[0] == first_entry
    assert data[17]["name"] == "Ogdenia"
    assert data[48]["label"] == "Hydrachnidiae"
    assert data[14]["synonym"] == ["Cyrene Peckham & Peckham"]


if __name__ == "__main__":
    test()
