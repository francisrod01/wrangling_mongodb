#!~/envs/python3/udacity_python_mongodb

import json
import codecs
import requests
import os

URL_MAIN = "http://api.nytimes.com/svc/"
URL_POPULAR = URL_MAIN + "mostpopular/v2/"
API_KEY = {
    "popular": "",
    "article": ""
}

DATA_DIR = "datasets"
POPULAR_FILE = "popular-{0}-{1}.json"
MOST_FILE = "most{0}/{1}/{2}.json"

popular_file = os.path.join(DATA_DIR, POPULAR_FILE)
most_file = os.path.join(DATA_DIR, MOST_FILE)


def get_from_file(kind, period):
    filename = popular_file.format(kind, period)
    with open(filename, "r") as f:
        return json.loads(f.read())


def article_overview(kind, period):
    data = get_from_file(kind, period)
    titles = []
    urls = []

    ### @TODO our code here.

    return titles, urls


def query_site(url, target, offset):
    # This will set up the query with the API key and offset
    # Web services often use offset parameter to return data in small chunks
    # NYTimes returns 20 articles per request, if you want the next 20
    # You have to provide the offset parameter.
    if API_KEY["popular"] == "" or API_KEY["article"] == "":
        print("You need to register for NYTimes Developer account to run this program.")
        print("See Instructor notes for more information.")
        return False

    params = {
        "api-key": API_KEY[target],
        "offset": offset
    }

    r = requests.get(url, params=params)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def get_popular(url, kind, days, section="all-sections", offset=0):
    # This function will construct the query according to the requirements of the site
    # and return the data, or print an error message if called incorrectly.
    if days not in [1, 7, 30]:
        print("Time period can be 1, 7, 30 days only.")
        return False
    if kind not in ["viewed", "shared", "emailed"]:
        print("Kind can be only one of viewed/shared/emailed")
        return False

    url += most_file.format(kind, section, days)
    data = query_site(url, "popular", offset)

    return data


def save_file(kind, period):
    # This will process all results, by calling the API repeatedly with supplied offset value,
    # combine the data and then write all results in a file.
    data = get_popular(URL_POPULAR, "viewed", 1)
    num_results = data["num_results"]
    full_data = []
    with codecs.open(popular_file.format(kind, period), encoding='utf-8', mode='w') as v:
        for offset in range(0, num_results, 20):
            data = get_popular(URL_POPULAR, kind, period, offset=offset)
            full_data += data["results"]

        v.write(json.dumps(full_data, indent=2))


def test():
    titles, urls = article_overview("viewed", 1)
    assert len(titles) == 20
    assert len(urls) == 30
    assert titles[2] == {'Opinion': 'Professors, We Need You!'}
    assert urls[20] == 'http://graphics8.nytimes.com/images/2014/02/17/sports/ICEDANCE/ICEDANCE-thumbStandard.jpg'


if __name__ == "__main__":
    test()
