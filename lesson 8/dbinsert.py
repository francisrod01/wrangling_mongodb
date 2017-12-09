#!~/envs/udacity_python3_mongodb

"""
Complete the insert_data function to insert the data into MongoDB.
"""

import json

DATA_DIR = 'datasets/'
DATAFILE = DATA_DIR + 'arachnid.json'


def insert_data(data, db):
    db.arachnid.insert(data)


if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    with open(DATAFILE) as f:
        data = json.loads(f.read())
        insert_data(data, db)
        print(db.arachnid.find_one())
