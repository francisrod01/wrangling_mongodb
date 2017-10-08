#!~/envs/udacity_python3_mongodb

# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

import xml.etree.ElementTree as ET

PATENTS = "datasets/patent.data"


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def split_file(filename):
    """
    Split the input file into separate files, each containing a single patent.
    As a hint - each patent declaration starts with the same line that was
    causing the error found in the previous exercises.

    The new files should be saved with filename in the following format:
    "{}-{}".format(filename, n) where n is a counter, starting from 0.
    """

    with open(filename, "r") as f:
        splitxml = f.read().split("</us-patent-grant>")
        n = 0

        for xml_content in splitxml:
            with open("{}-{}".format(filename, n), "w") as xml_file:
                if len(xml_content) > 1:
                    xml_file.write(xml_content.strip())
                    n = n + 1
                else:
                    pass


def test():
    split_file(PATENTS)
    for n in range(4):
        fname = "{}-{}".format(PATENTS, n)
        try:
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print("You have not split the file {} in the correct boundary!".format(fname))
            f.close()
        except:
            print("Could not find file {}. Check if the filename is correct!".format(fname))


test()
