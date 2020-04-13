from flask import Flask, jsonify, request, Response, json

app = Flask(__name__)
books = [
    {
        'name':"Padre rico, padre pobre",
        'price': 25.3,
        'isbn': 2132134354,
    },
    {   'name': 'Harry Potter III',
        'price': 30,
        'isbn': 2132132135,
    }
]

def validBookObject(bookObject):
    if("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False

@app.route("/")
def hello_world():
    return 'Hello World'

@app.route("/books")
def get_books():
    return jsonify({'books':books})


@app.route("/books", methods=['POST'])
def add_book():
    request_data = request.get_json()

    if(validBookObject(request_data)):
        new_book = {
            "name": request_data['name'],
            "price": request_data['price'],
            "isbn": request_data['isbn']
        }
        books.insert(0, new_book)
        response = Response("",201,mimetype='application/json')
        response.headers['Location'] = "/books/" + str(new_book['isbn'])
        return response
    else:
        invalidBookObjectMsg = {
            "error": "invalid Book object passed in request",
            "helpString": "Data passed in similar to this  {'name': 'bookname','price': 30,'isbn': 2132132135}"
        }
        response = Response(json.dumps(invalidBookObjectMsg), status=400, mimetype='application/json')
        return response

@app.route("/books/<int:isbn>")
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'name': book['name'],
                'price': book['price']
            }

    return jsonify(return_value)

@app.route("/books/<int:isbn>", methods=['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    new_item = {
            'name': request_data['name'],
            'price': request_data['price'],
            'isbn': isbn
    }
    i = 0
    for book in books:
        currentItem = book['isbn']
        if  currentItem == isbn:
            books[i] = new_item
        i=+1
    response = Response("", status= 204)
    return response


app.run(port=5000, host="0.0.0.0")