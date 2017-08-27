#!~/envs/python3/udacity_python_mongodb

import csv
import os

DATADIR = ""
DATAFILE = "datasets/745090.csv"


def parse_file(datafile):
    name = ""
    data = []
    with open(datafile, 'r') as f:
        name = f.readline().split(',')
        name = name[1].strip('"')
        for line in f:
            data = list(csv.reader(f, delimiter=','))
    # Do not change the line below
    return name, data


def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    name, data = parse_file(datafile)

    assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
    assert data[0][1] == "01:00"
    assert data[2][0] == "01/01/2005"
    assert data[2][5] == "2"


if __name__ == "__main__":
    test()
