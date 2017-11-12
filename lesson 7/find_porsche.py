#!~/envs/udacity_python3_mongodb

"""
Your task is to complete the 'porsche_query' function and in particular the query
to find all autos where the manufacturer field matches "Porsche".
Please modify only 'porsche_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB and download and insert the datasets.
For instructions related to MongoDB setup and datasets please see Course Materials at
the following link:
https://www.udacity.com/wiki/ud032
"""


def porsche_query():
    # Please fill in the query to find all autos manufactured by Porsche.
    query = {}
    return query


def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db


def find_porsche(db, query):
    return db.autos.find(query)


if __name__ == "__main__":
    db = get_db('examples')
    query = porsche_query()
    results = find_porsche(db, query)

    print("Printing first 3 results\n")
    import pprint

    for car in results[:3]:
        pprint.pprint(car)
