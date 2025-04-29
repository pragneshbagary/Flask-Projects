from book import db, app
from book import AuthorModel, BookModel

def populate_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        authors = [
            AuthorModel(name="J.K. Rowling"),
            AuthorModel(name="George R.R. Martin"),
            AuthorModel(name="J.R.R. Tolkien"),
            AuthorModel(name="Agatha Christie")
        ]

        db.session.add_all(authors)
        db.session.commit()

        books = [
            BookModel(title="Harry Potter and the Sorcerer's Stone", author_id=authors[0].id),
            BookModel(title="Harry Potter and the Chamber of Secrets", author_id=authors[0].id),
            BookModel(title="A Game of Thrones", author_id=authors[1].id),
            BookModel(title="The Hobbit", author_id=authors[2].id),
            BookModel(title="Murder on the Orient Express", author_id=authors[3].id),
        ]

        db.session.add_all(books)
        db.session.commit()

        print("✅ Sample authors and books added successfully.")

if __name__ == "__main__":
    populate_data()
