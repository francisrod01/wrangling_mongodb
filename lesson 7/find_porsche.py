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


def add_car(db):
    db.autos.insert([
        {
            "layout": "NULL",
            "name": "Ford GT40",
            "productionYears": [],
            "modelYears": [],
            "bodyStyle": [
                "coupé",
                "roadster"
            ],
            "assembly": "NULL",
            "class": [
                "group 4 (racing)",
                "group 6 (racing)"
            ],
            "manufacturer": [
                "Carrol Shelby International",
                "Ford _Advanced_Vehicles",
                "John Wyer",
                "Kar_Kraft"
            ]
        },
        {
            "layout": "rear mid-engine rear-wheel-drive layout",
            "name": "Porsche Boxster",
            "productionYears": [],
            "modelYears": [],
            "bodyStyle": "roadster",
            "assembly": [
                "Finland",
                "Germany",
                "Stuttgart",
                "Uusikaupunki"
            ],
            "class": "sports car",
            "manufacturer": "Porsche"
        }
    ])


def porsche_query():
    # Please fill in the query to find all autos manufactured by Porsche.
    query = {"manufacturer": "Porsche"}
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
    # add_car(db)
    query = porsche_query()
    results = find_porsche(db, query)

    print("Printing first 3 results\n")
    import pprint

    for car in results[:3]:
        pprint.pprint(car)
