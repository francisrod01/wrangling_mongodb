#!~/envs/udacity_python3_mongodb

"""
Your task in this exercise has two steps:

- audit the OSM file and change the variable 'mapping' to reflect the changes needed to fix
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problem you find in this OSM file,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the 'update_name' function, to actually fix the 'street_name'.
    The function takes a string with street name as an argument and should return the fixed name
    we have provided a simple test so that you see what exactly is expected.
"""

import xml.etree.cElementTree as et
from collections import defaultdict
import re
import pprint

# Global variables
dataset_dir = 'datasets/'
dataset_file = dataset_dir + 'example2.osm'
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected = [
    "Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
    "Trail", "Parkway", "Commons"
]

mapping = {
    "AVE": "Avenue",
    "Ave": "Avenue",
    "Ave.": "Avenue",
    "Av.": "Avenue",
    "ave": "Avenue",
    "Blvd": "Boulevard",
    "Blvd.": "Boulevard",
    "boulevard": "Boulevard",
    "CT": "Court",
    "Ct": "Court",
    "Dr": "Drive",
    "Dr.": "Drive",
    "E": "East",
    "E.Division": "East Division",
    "FI": "Fox Drive",
    "Hwy": "Highway",
    "K10": "NE 8th Street",
    "MainStreet": "N Main Street",
    "N": "North",
    "NE": "Northeast",
    "NW": "Northwest",
    "nw": "Northwest",
    "PL": "Place",
    "Pl": "Place",
    "Rd": "Road",
    "RD": "Road",
    "Rd.": "Road",
    "S": "South",
    "S.": "South",
    "S.E.": "Southeast",
    "SE": "Southeast",
    "ST": "Street",
    "SW": "Southwest",
    "SW,": "Southwest",
    "Se": "Southeast",
    "southeast": "Southeast",
    "St": "Street",
    "st": "Street",
    "street": "Street",
    "St.": "Street",
    "Ter": "Terrace",
    "W": "West",
    "west": "West",
    "WA": "17625 140th Avenue Southeast",
    "WA)": "US 101",
    "WY": "Way"
}


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return elem.attrib['k'] == "addr:street"


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in et.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(name, _mapping):
    n = street_type_re.search(name)
    n = n.group()
    for m in _mapping:
        if n == m:
            name = name[:-len(n)] + _mapping[m]
    return name


def test():
    st_types = audit(dataset_file)
    assert len(st_types) == 3
    pprint.pprint(dict(st_types))

    for st_type, ways in st_types.items():
        for name in ways:
            better_name = update_name(name, mapping)
            print(name, "=>", better_name)
            if name == "West Lexington St.":
                assert better_name == "West Lexington Street"
            if name == "Baldwin Rd.":
                assert better_name == "Baldwin Road"


if __name__ == '__main__':
    test()
