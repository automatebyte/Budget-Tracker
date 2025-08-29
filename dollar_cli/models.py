from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

# This is the base class for all our database tables
Base = declarative_base()

# This enum makes sure we only use valid transaction types
class TransactionType(enum.Enum):
    INCOME = "income"   # Money coming in
    EXPENSE = "expense" # Money going out

# This table stores budget categories like Food, Rent, Entertainment
class Category(Base):
    __tablename__ = 'categories'  # This will be the table name in the database
    
    id = Column(Integer, primary_key=True)        # Unique ID for each category
    name = Column(String, unique=True, nullable=False)  # Category name (must be unique)
    budget_limit = Column(Float, nullable=True)   # Optional spending limit
    
    # This connects categories to their transactions
    transactions = relationship("Transaction", back_populates="category")

# This table stores individual money transactions
class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)          # Unique ID for each transaction
    amount = Column(Float, nullable=False)          # How much money was involved
    description = Column(String)                    # What the transaction was for
    date = Column(DateTime, default=datetime.now)   # When it happened (defaults to now)
    type = Column(Enum(TransactionType), nullable=False)  # Income or expense
    category_id = Column(Integer, ForeignKey('categories.id'))  # Links to category table
    
    # This connects transactions to their category
    category = relationship("Category", back_populates="transactions")

# This table stores financial goals for different categories
class BudgetGoal(Base):
    __tablename__ = 'budget_goals'
    
    id = Column(Integer, primary_key=True)              # Unique ID for each goal
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)  # Links to category
    target_amount = Column(Float, nullable=False)       # How much we want to save/spend
    timeframe = Column(String, default="monthly")       # Monthly or yearly goal
    
    # This connects goals to their category
    category = relationship("Category")