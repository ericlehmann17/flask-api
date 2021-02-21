# flask-api
A small web application created using the Flask web framework in Python. Mainly for practice and learning purposes. The application allows a user to pull data from a web api by making queries in the url. Many of the ideas in this project came from an online tutorial: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

Both the database file and the python file are included in this repo. You have to download all the files to your local machine in order for this to work - the web application runs on your local IP, and the application pulls from the database locally. 

The database is a small database containing info on a few notable science fiction novels. 

Once the application is running on your local machine, open http://127.0.0.1:5000/ to view the application home page. 

There are two primary functions that this application can perform:
  - Add the following text to the url to pull all of the data from the database and display it, jsonified: api/v1/resources/books/all
  - Instead of /all, type a '?' followed by one of the following: author=[type a name], id=[type an integer], published=[type a year]. This will return all the books that have the specified id number, or specified author, or specified publication year (jsonified).

While making this application, I learned a lot about apis, url structure, http methods and how to manage them (mainly get), databases, html tags, flask in general, databases and SQL.

