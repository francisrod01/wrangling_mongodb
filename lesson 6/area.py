#!~/envs/udacity_python3_mongodb
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the
"areaLand" field, you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it
has to return a float representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you
like, but changes to process_file will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""

import codecs
import csv
import json
import pprint

import re

DIR_DATA = 'datasets/'
CITIES_DATA = DIR_DATA + 'cities.csv'


def test_if_int(text):
    try:
        a = int(text)
        return True
    except ValueError:
        return False


def test_if_float(text):
    try:
        a = float(text)
        if test_if_int(text):
            return False
        else:
            return True
    except ValueError:
        return False


def fix_area(area):
    if test_if_float(area):
        return float(area)
    elif re.match(r'^{', area):
        values = area.strip('{,}').split('|')
        return float(max(values, key=len))
    else:
        return None


def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        # Skipping the extra metadata
        for i in range(3):
            l = reader.__next__()

        # Processing file
        for line in reader:
            # Calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES_DATA)

    print("Printing three example results:")
    for n in range(5, 8):
        pprint.pprint(data[n]["areaLand"])

    assert data[3]["areaLand"] is None
    assert data[8]["areaLand"] == 55166700.0
    assert data[20]["areaLand"] == 14581600.0
    assert data[33]["areaLand"] == 20564500.0


if __name__ == "__main__":
    test()
