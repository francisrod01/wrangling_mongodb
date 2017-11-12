#!~/envs/udacity_python3_mongodb

"""
Add a single line of code to the insert_autos function that will insert the
automobile data into the 'autos' collection. The data variable that is
returned from the process_file function is a list of dictionaries, as in the
example in the previous video.
"""

from autos import process_file

DIR_DATA = "datasets/"
AUTOS_DATA = DIR_DATA + "autos-small.csv"


def insert_autos(infile, db):
    data = process_file(infile)
    # Add your here. Insert the data in one command.


if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    insert_autos(AUTOS_DATA, db)
    print(db.autos.find_one())
