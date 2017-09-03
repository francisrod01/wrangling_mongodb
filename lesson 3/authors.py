#!~/envs/python3/udacity_python_mongodb

import xml.etree.ElementTree as ET

article_file = "datasets/exampleResearchArticle.xml"


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
            "fnm": None,
            "snm": None,
            "email": None
        }

        # YOUR CODE HERE

        authors.append(data)

    return authors


def test():
    solution = [
        {'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'},
        {'fnm': 'Mike', 'snm': 'Carmont', 'email': 'mcarmont@hotmail.com'},
        {'fnm': 'Lior', 'snm': 'Laver', 'email': 'laver17@gmail.com'},
        {'fnm': 'Meir', 'snm': 'Nyska', 'email': 'nyska@internet-zahav.net'},
        {'fnm': 'Hagay', 'snm': 'Kammar', 'email': 'kammarh@gmail.com'},
        {'fnm': 'Gideon', 'snm': 'Mann', 'email': 'gideon.mann.md@gmail.com'},
        {'fnm': 'Barnaby', 'snm': 'Clarck', 'email': 'barns.nz@gmail.com'},
        {'fnm': 'Eugene', 'snm': 'Kots', 'email': 'eukots@gmail.com'}
    ]

    root = get_root(article_file)
    data = get_authors(root)

    assert data[0] == solution[0]
    assert data[1]["fnm"] == solution[1]["fnm"]


test()
