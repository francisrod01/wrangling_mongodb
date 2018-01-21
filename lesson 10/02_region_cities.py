#!~/envs/udacity_python3_mongodb

"""
Which Region in India has the largest number of cities with longitude between
75 and 80?

Please modify only the 'make_pipeline' function so that it creates and returns
an aggregation pipeline that can be passed to the MongoDB aggregate function.
As in our examples in this lesson, the aggregation pipeline should be a list of
one or more dictionary objects. Please review the lesson examples if you are
unsure of the syntax.

Your code will be run against a MongoDB instance that we have provided. If you
want to run this code locally on your machine, you have to install MongoDB,
download and insert the dataset. For instructions related to MongoDB setup and
datasets please see Course Materials.

Please note that the dataset you are using here is a different version of the
cities collection provided in the course materials, if you attempt some of the
same queries that we look at in the problem set, your results may be different.

NOTE - If you have to match multiple criteria on a single field, you will need
to put both conditions in the same dictionary, e.g.

{"$match": {'field': {'$cond1': val1, '$cond2': val2}...}}

NOTE - See the example document in lesson9/datasets/example_india_city.txt
"""


def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db


def make_pipeline():
    pipeline = [
        {
            "$unwind": "$isPartOf",
        },
        {
            "$match": {
                "lon": {"$gt": 75, "$lt": 80},
                "name": {"$ne": None},
                "country": "India",
            },
        },
        {
            "$group": {
                "_id": "$isPartOf",
                "count": {"$sum": 1},
            },
        },
        {
            "$sort": {"count": -1},
        },
        {
            "$limit": 1
        }
    ]
    return pipeline


def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]


if __name__ == '__main__':
    # The following statements will be used to test your code by the grader.
    # Any modifications to the code past this point will not be reflected by
    # the Test Run.
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)

    import pprint

    pprint.pprint(result[0])

    assert len(result) == 1
    assert result[0]["_id"] == 'Tamil Nadu'
    assert result[0]["count"] == 424
