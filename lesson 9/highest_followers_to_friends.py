#!~/envs/udacity_python3_mongodb

"""
It is important to note that there is no "$group" stage in this pipeline.

If a user tweeted more than once in this data set a ratio will be computed
for that user each time one of their tweets if found, leading to duplicates.

If the user's friend count or followers count changed during the time
this data set was taken, the ratio will change too!
"""

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.examples


def highest_ratio():
    result = db.tweets.aggregate([
        {
            "$match": {
                "user.friends_count": {"$gt": 0},
                "user.followers_count": {"$gt": 0},
            },
        },
        {
            "$project": {
                "ratio": {
                    "$divide": [
                        "$user.followers_count",
                        "$user.friends_count",
                    ]
                },
                "screen_name": "$user.screen_name",
            },
        },
        {
            "$sort": {"ratio": -1},
        },
        {
            "$limit": 1,
        },
    ])

    return result


if __name__ == '__main__':
    result = highest_ratio()
    print(result)
