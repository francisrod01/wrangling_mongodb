#!~/envs/python3/udacity_python_mongodb

from bs4 import BeautifulSoup
import requests

SOURCE_URL = "https://www.transtats.bts.gov/Data_Elements.aspx?Data=2"
HTML_PAGE = "datasets/virgin_and_logan_airport.html"


def make_html():
    data = {"eventvalidation": "",
            "viewstate": ""}

    s = requests.Session()

    req = s.get(SOURCE_URL)
    soup = BeautifulSoup(req.text, "lxml")

    viewstate_element = soup.find('input', id="__VIEWSTATE")
    eventvalidation_element = soup.find('input', id="__EVENTVALIDATION")

    data["viewstate"] = viewstate_element["value"]
    data["eventvalidation"] = eventvalidation_element["value"]

    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post(SOURCE_URL,
                      data={"__EVENTTARGET": "",
                            "__EVENTARGUMENT": "",
                            "__VIEWSTATE": viewstate,
                            "__EVENTVALIDATION": eventvalidation,
                            'CarrierList': "VX",
                            'AirportList': "BOS",
                            'Submit': 'Submit'
                            })

    f = open(HTML_PAGE, "w")
    f.write(r.text)


def run():
    html_page = make_html()
    make_request(html_page)


if __name__ == '__main__':
    run()
