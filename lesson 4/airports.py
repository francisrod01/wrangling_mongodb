#!~/envs/udacity_python3_mongodb

# -*- coding: utf-8 -*-
"""
Complete the 'extract_airports()' function so that it returns a list of airport
codes, excluding any combinations like "All".

Refer to the 'options.html' file in the tab above for a stripped down version
of what is actually on the website. The test() assertions are based on the
given file.
"""

from bs4 import BeautifulSoup

html_page = "datasets/options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # Find the necessary values
        soup = BeautifulSoup(html, "lxml")

        airport_list = soup.select("select#AirportList option")

        for airport in airport_list:
            if airport["value"].startswith("All"):
                del airport["value"]
            else:
                data.append(airport["value"])

    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data


if __name__ == "__main__":
    test()
