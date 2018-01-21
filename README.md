# wrangling_mongodb #

Udacity Data Wrangling with MongoDB course lessons

Author: [Francis Rodrigues](https://github.com/francisrod01)


### Questions ###

* Can I import a file to my MongoDB instance?

```commandline
mongoimport -d mydb -c things --type csv --file locations.csv --headerline
```


Course's material:

* [Course Resources](https://www.udacity.com/wiki/ud032#course-resources)
* [Discussion Forum](https://discussions.udacity.com/c/standalone-courses/data-wrangling-with-mongodb)

Course discussions:

* [Using $push](https://discussions.udacity.com/t/using-push/121851)

Font's material:

* [Built-in Types](https://docs.python.org/3/library/stdtypes.html)
* [CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
* [Time access and conversions](https://docs.python.org/3/library/time.html)
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [Installation of Requests](http://requests.readthedocs.io/en/latest/user/install/#install)
* [W3C - Extensible Markup Language (XML)](https://www.w3.org/TR/xml/#sec-origin-goals)
* [W3C - Introduction to XML](https://www.w3schools.com/xml/xml_whatis.asp)
* [XML - Example research article](https://d17h27t6h515a5.cloudfront.net/topher/2017/March/58be1c65_exampleresearcharticle/exampleresearcharticle.xml)
* [XML - XPath Syntax](https://www.w3schools.com/xml/xpath_syntax.asp)
* [The Element Tree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree)
* [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Installing additional Modules in Python](https://www.udacity.com/wiki/ud032#installing-additional-modules-in-python)
* Live RegEx tester at [regexpal.com](http://regexpal.com)
* OpenStreetMap [OSM XML](https://wiki.openstreetmap.org/wiki/OSM_XML)


Python dictionaries:
* [Python dictionaries](https://docs.python.org/2/tutorial/datastructures.html#dictionaries)
* [PyMongo installation instructions](http://api.mongodb.org/python/current/installation.html)
    + [cursor - Tools for iterating over MongoDB query results](http://api.mongodb.com/python/current/api/pymongo/cursor.html)
* Official Python [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
* Another good [Python Regular Expressions][1] page

[1]: https://developers.google.com/edu/python/regular-expressions?csw=1


Database's fonts:
* [National Solar Radiation Data Base](http://rredc.nrel.gov/solar/old_data/nsrdb/1991-2005/tmy3/by_USAFN.html)
* [NYTimes Developer Documentation for the Most Popular API](http://developer.nytimes.com/)
* [Air Trans website](https://www.transtats.bts.gov/Data_Elements.aspx?Data=2)
* [Metro extracts](https://mapzen.com/data/metro-extracts/)
* [MongoDB installation instructions](http://docs.mongodb.org/manual/installation/)
    + [Drivers and client libraries](http://docs.mongodb.org/manual/applications/drivers/)
    + [Using Mongoimport](http://docs.mongodb.org/manual/reference/program/mongoimport/)
    + [Query and Projection Operators](https://docs.mongodb.com/manual/reference/operator/query/)
    + [$regex manual](http://docs.mongodb.org/manual/reference/operator/query/regex/)
    + [Aggregation Framework Operator doc](http://docs.mongodb.org/manual/reference/operator/aggregation/)
        * [$match aggregation](https://docs.mongodb.com/manual/reference/operator/aggregation/match/)
        * [$elementMatch (query)](https://docs.mongodb.com/manual/reference/operator/query/elemMatch/)
        * [$group aggregation](https://docs.mongodb.com/manual/reference/operator/aggregation/group/)
        * [$project aggregation](https://docs.mongodb.com/manual/reference/operator/aggregation/project/#pipe._S_project)
        * [$unwind aggregation](https://docs.mongodb.com/manual/reference/operator/aggregation/unwind/#pipe._S_unwind)
    