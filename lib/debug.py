# Import necessary modules from SQLAlchemy and your custom models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Review, Customer

if __name__ == '__main__':
    # Create an SQLAlchemy engine to connect to the SQLite database 'restaurbase.db'
    engine = create_engine('sqlite:///restaurbase.db')

    # Create a session factory using the engine
    Session = sessionmaker(bind=engine)

    # Create a session to interact with the database
    session = Session()

    # Set a breakpoint using 'ipdb' for debugging
    import ipdb; ipdb.set_trace()
