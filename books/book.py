from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, fields, marshal_with, reqparse, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)

class AuthorModel(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False, unique = True)

    books = db.relationship('BookModel',  backref='author', lazy = True)

    def __repr__(self):
        return super().__repr__()

class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False, unique = True)

    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable = False)

    def __repr__(self):
        return super().__repr__()

author_args = reqparse.RequestParser()
book_args = reqparse.RequestParser()

author_args.add_argument('name', type=str, required = True, help = "Name cannot be empty")

book_args.add_argument('title', type = str, required = True, help = "Name cannot be empty")
book_args.add_argument('author_id', type = int, required = True, help = "Author cannot be empty")

authorFields = {
    "name" : fields.String,
}

bookFields = {
    "title" : fields.String,
    "author_id" : fields.Integer,
    "author" : fields.Nested(authorFields)
}


class Authors(Resource):
    @marshal_with(authorFields)
    def get(self):
        authors = AuthorModel.query.all()
        return authors
    
    @marshal_with(authorFields)
    def post(self):
        args = author_args.parse_args()
        new_author = AuthorModel(name =  args['name'])
        db.session.add(new_author)
        db.session.commit()
        return AuthorModel.query.all(), 201
    
class Author(Resource):
    @marshal_with(authorFields)
    def get(self, id):
        author = AuthorModel.query.filter_by(id=id).first()
        return author
    
    @marshal_with(authorFields)
    def put(self, id):
        args = author_args.parse_args()
        author = AuthorModel.query.filter_by(id=id).first()
        if not author:
            abort(404, message="Author not found")
        author.name = args['name']
        db.session.commit()
        return author
    
    @marshal_with(authorFields)
    def delete(self, id):
        # args = author_args.parse_args()
        author = AuthorModel.query.filter_by(id=id).first()
        if not author:
            abort(404, message="Author not found")
        db.session.delete(author)
        db.session.commit()
        return AuthorModel.query.all()
    

class Books(Resource):
    @marshal_with(bookFields)
    def get(self):
        books = BookModel.query.all()
        return books
    
    @marshal_with(bookFields)
    def post(self):
        args = book_args.parse_args()
        new_book = BookModel(title =  args['title'], author_id = args['author_id'])
        db.session.add(new_book)
        db.session.commit()
        return BookModel.query.all(), 201
    
class Book(Resource):
    @marshal_with(bookFields)
    def get(self, id):
        book = BookModel.query.filter_by(id=id).first()
        return book
    
    @marshal_with(bookFields)
    def put(self, id):
        args = book_args.parse_args()
        book = BookModel.query.filter_by(id=id).first()
        if not book:
            abort(404, message="Book not found")
        book.title = args['title']
        book.author_id = args['author_id']
        db.session.commit()
        return book
    
    @marshal_with(bookFields)
    def delete(self, id):
        # args = book_args.parse_args()
        book = BookModel.query.filter_by(id=id).first()
        if not book:
            abort(404, message="Book not found")
        db.session.delete(book)
        db.session.commit()
        return BookModel.query.all()
    
class BooksByAuthor(Resource):
    def get(self, author_id):
        books = BookModel.query.filter_by(author_id=author_id).all()
        return [{"id":book.id, "title": book.title}
                for book in books], 200
    
    

api.add_resource(Authors, '/api/authors/')
api.add_resource(Author, '/api/author/<int:id>/')
api.add_resource(Books, '/api/books/')
api.add_resource(Book, '/api/book/<int:id>/')
api.add_resource(BooksByAuthor, '/api/author/<int:author_id>/books')


@app.route('/')
def home():
    return '<h1>This is a book app</h1>'

if __name__ == '__main__':
    app.run(debug=True)
