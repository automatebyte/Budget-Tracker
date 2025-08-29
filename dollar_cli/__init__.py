from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# This sets up our connection to the SQLite database
# The database will be stored in a file called 'budget.db'
engine = create_engine('sqlite:///budget.db')

# NOTE: We use Alembic migrations to create tables instead of Base.metadata.create_all()
# Run 'alembic upgrade head' to create the database tables

# This creates a Session class that we'll use to talk to the database
Session = sessionmaker(bind=engine)

# This function gives us a new database session whenever we need it
def get_session():
    """Returns a new database session for performing operations"""
    return Session()