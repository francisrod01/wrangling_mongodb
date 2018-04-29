#!~/envs/udacity_python3_mongodb

"""
Your task is to wrangle the data and transform the shape of the data
into the model we mentioned earlier. The output should be a list of dictionaries
that look like this:

{
    "id": "2406124091",
    "type: "node",
    "visible":"true",
    "created": {
      "version":"2",
      "changeset":"17206049",
      "timestamp":"2013-08-03T16:43:42Z",
      "user":"linuxUser16",
      "uid":"1219059"
    },
    "pos": [41.9757030, -87.6921867],
    "address": {
      "housenumber": "5157",
      "postcode": "60625",
      "street": "North Lincoln Ave"
    },
    "amenity": "restaurant",
    "cuisine": "mexican",
    "name": "La Cabana De Don Luis",
    "phone": "1 (773)-271-5176"
}

You have to complete the function 'shape_element'.
We have provided a function that will parse the map file, and call the function with the element
as an argument. You should return a dictionary, containing the shaped data for that element.
We have also provided a way to save the data in a file, so that you could use
mongoimport later on to import the shaped data into MongoDB.

Note that in this exercise we do not use the 'update street name' procedures
you worked on in the previous exercise. If you are using this code in your final
project, you are strongly encouraged to use the code from previous exercise to
update the street names before you save them to JSON.

In particular the following things should be done:
- you should process only 2 types of top level tags: "node" and "way"
- all attributes of "node" and "way" should be turned into regular key/value pairs, except:
    - attributes in the CREATED array should be added under a key "created"
    - attributes for latitude and longitude should be added to a "pos" array,
      for use in geospacial indexing. Make sure the values inside "pos" array are floats
      and not strings.
- if the second level tag "k" value contains problematic characters, it should be ignored
- if the second level tag "k" value starts with "addr:", it should be added to a dictionary "address"
- if the second level tag "k" value does not start with "addr:", but contains ":", you can
  process it in a way that you feel is best. For example, you might split it into a two-level
  dictionary like with "addr:", or otherwise convert the ":" to create a valid key.
- if there is a second ":" that separates the type/direction of a street,
  the tag should be ignored, for example:

<tag k="addr:housenumber" v="5158" />
<tag k="addr:street" v="North Lincoln Avenue"/>
<tag k="addr:street:name" v="Lincoln"/>
<tag k="addr:street:prefix" v="North"/>
<tag k="addr:street:type" v="Avenue"/>
<tag k="amenity" v="pharmacy"/>

  should be turned into:

{...
    "address": {
        "housenumber": 5158,
        "street": "North Lincoln Avenue"
    }
    "amenity": "pharmacy",
    ...
}

- for "way" specifically:

  <nd ref="305896090"/>
  <nd ref="1719825889"/>

  should be turned into:

  "node_refs": ["305896090", "1719825889"]
"""

import xml.etree.cElementTree as et
import pprint
import re
import codecs
import json

dataset_dir = 'datasets/'
dataset_file = dataset_dir + 'example2.osm'
lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problem_chars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = ["version", "changeset", "timestamp", "user", "uid"]


# Helping for a solution:
# https://discussions.udacity.com/t/preparing-for-database-mongodb-example/197866
def shape_element(element):
    node = {}
    my_temp_dictionary = {}
    my_temp_address_dictionary = {}
    node_refs_list = []
    # pos_list = []
    # initialize two element list
    pos_list = [None for i in range(2)]

    if element.tag == "node" or element.tag == "way":
        # used for development, testing
        # if element.tag == "way" and element.attrib['id'] == '209809850' :
        # used for development, testing
        # if element.tag == "node" and element.attrib['id'] == '2406124091' :
        # if element.tag == "way": # used for development, testing
        node['type'] = element.tag
        # print("element is {}".format(element))
        # type(element) is <type 'Element'>
        # print("type(element) is {}\n".format(type(element)))

        # element.tag is way
        # print("element.tag is {}".format(element.tag))
        # print("type(element.tag) is {}\n".format(type(element.tag))) #str

        # print("element.attrib is {}\n".format(element.attrib)) #
        # print("type(element.attrib) is {}\n".format(type(element.attrib))) # Dictionary

        # access the top level element.attrib dictionary
        # print ("element.attrib[key] - {}\n".format(element.attrib[key]))
        for key in element.attrib:

            if key in CREATED:
                # populate my_temp_dictionary with the key value pair from
                # the element.attrib dictionary
                # when the key is in the hard coded CREATED list
                my_temp_dictionary[key] = element.attrib[key]
                # populate the created dictionary nested within
                # the node dictionary
                node['created'] = my_temp_dictionary

            elif key == 'lat':
                pos_list[0] = float(element.attrib[key])
                # print("lat type(element.attrib[key]) is {}".format(type(element.attrib[key])))
                # print("lat type(pos_list[0]) is {}\n".format(type(pos_list[0])))
                node['pos'] = pos_list

            elif key == 'lon':
                pos_list[1] = float(element.attrib[key])
                # print("lon type(element.attrib[key]) is {}".format(type(element.attrib[key])))
                # print("lon type(pos_list[1]) is {}\n".format(type(pos_list[1])))

                node['pos'] = pos_list

            else:
                # populate the node dictionary
                node[key] = element.attrib[key]

        # access the nested elements
        for secondLevelTag in element:
            # print("secondLevelTag is {}".format(secondLevelTag))
            # <type 'Element'>
            # print("type(secondLevelTag) is {}".format(type(secondLevelTag)))

            # print("secondLevelTag.attrib is {}".format(secondLevelTag.attrib))

            for key in secondLevelTag.attrib:
                # print("\tkey - {}, value - {}".format(key, secondLevelTag.attrib[key]))
                if 'ref' in secondLevelTag.attrib:
                    node_refs_list.append(secondLevelTag.attrib['ref'])
                    node['node_refs'] = node_refs_list

                elif 'k' in secondLevelTag.attrib:
                    if 'addr:housenumber' == secondLevelTag.attrib['k']:
                        my_temp_address_dictionary['housenumber'] = secondLevelTag.attrib['v'].strip()
                        # print("secondLevelTag.attrib['v'] is {}".format(secondLevelTag.attrib['v']))
                        # print("type(secondLevelTag.attrib['v']) is {}".format(type(secondLevelTag.attrib['v']))) # str
                        node['address'] = my_temp_address_dictionary

                    elif "addr:street" == secondLevelTag.attrib['k']:
                        node['address']['street'] = secondLevelTag.attrib['v']

                    elif "addr:postcode" == secondLevelTag.attrib['k']:
                        node['address']['postcode'] = secondLevelTag.attrib['v']

                    elif "amenity" == secondLevelTag.attrib['k']:
                        node['amenity'] = secondLevelTag.attrib['v']

                    elif "cuisine" == secondLevelTag.attrib['k']:
                        node['cuisine'] = secondLevelTag.attrib['v']

                    elif "name" == secondLevelTag.attrib['k']:
                        node['name'] = secondLevelTag.attrib['v']

                    elif "phone" == secondLevelTag.attrib['k']:
                        node['phone'] = secondLevelTag.attrib['v']

        # print("END THAT ELEMENT\n")

        return node
    else:
        return None


def process_map(file_in, pretty=False):
    # You do not need to change this file
    file_out = "{0}-output.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in et.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2) + "\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data


def test():
    # NOTE: if you are running this code on your computer, with a larger dataset,
    # call the 'process_map' procedure with pretty=false. The pretty=true option adds
    # additional spaces to the output, making it significantly larger.
    data = process_map(dataset_file)
    # pprint.pprint(data)
    # pprint.pprint(data[-1])

    correct_first_element = {
        "id": "261114295",
        "visible": "true",
        "type": "node",
        "pos": [41.9730791, -87.6866303],
        "created": {
            "changeset": "11129782",
            "user": "bbmiller",
            "version": "7",
            "uid": "451048",
            "timestamp": "2012-03-28T18:31:23Z"
        }
    }
    assert data[0] == correct_first_element
    assert data[-1]["address"] == {
        "street": "West Lexington St.",
        "housenumber": "1412"
    }
    assert data[-1]["node_refs"] == [
        "2199822281", "2199822390", "2199822392", "2199822369",
        "2199822370", "2199822284", "2199822281"
    ]


if __name__ == "__main__":
    test()
