# writers_books
Fast API backend for small service returns writer and his books

For communication with database needed to start postgresql server at 
localhost:5432 with database named postgres. Use user name == postgres, password == password.
Or correct pg server information(user, password, host, db_name) in sql_app/database.py like:
SQLALCHEMY_DATABASE_URL ="postgresql+psycopg2://user:password@host/db_name"

To start applicaton run: python main.py
To initialize application database example needed run python main.py init