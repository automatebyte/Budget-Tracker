from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# This sets up our connection to the SQLite database
# The database will be stored in a file called 'budget.db'
engine = create_engine('sqlite:///budget.db')

# This creates all the tables in the database based on our models
Base.metadata.create_all(engine)

# This creates a Session class that we'll use to talk to the database
Session = sessionmaker(bind=engine)

# This function gives us a new database session whenever we need it
def get_session():
    return Session()