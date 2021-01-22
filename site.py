#FIRST TIME USING FLASK
#this was a good experience, learning how to use flask with python to manage http requests and create a little web api 
#below is the code used to establish a working flask application and a small api for some book data from a database

#learned a lot about apis, url structure, http methods and how to manage them (mainly get), databases, html tags,
#... flask in general, databases and SQL


from flask import Flask, request, jsonify
import sqlite3


app = Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods = ['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/resources/books/all', methods = ['GET'])
def api_all():
    #here we will connect this page to the sqlite3 database and display the data
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()

    return jsonify(all_books)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

    #note: in HTML responses, the code 200 means "OK", and the code 404 means "Not Found".
    #this page will display when a code 404 is encountered (invalid url at this domain)

@app.route('/api/v1/resources/books', methods = ['GET'])
def api_filter():
    #this method will read the query parameters portion of the url (after the ?) and show a page with a jsonified version of all
    #data entries that contain the requested information
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"
    #note: SQL queries used to find data in a database take the form:
    # 'SELECT <columns> FROM <table> WHERE <column=match> AND <column=match>;'
    #... and you can keep adding more AND <column=match> statements to further filter the search
    #SO, the above definition is just to start building the query 
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)

    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'
    #this line basically just removes the trailing AND at the end of the query we have built, and adds a ;

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)
app.run()