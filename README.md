# Dollar-CLI - Personal Budget Tracker

A command-line interface (CLI) application for tracking personal finances, built with Python, SQLAlchemy ORM, and Click.

## Features

- **Add Transactions**: Record income and expenses with categories
- **Monthly Summary**: View your income, expenses, and balance
- **Transaction History**: List recent transactions with filtering options
- **Budget Limits**: Set spending limits for different categories
- **Category Management**: Automatically creates and manages expense categories

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd dollar-cli
   ```

2. **Install dependencies using Pipenv**:
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Initialize the database**:
   ```bash
   alembic upgrade head
   ```

## Usage

### Basic Commands

#### Add a Transaction
```bash
dollar add --amount 50.00 --description "Groceries" --category "Food" --type expense
```

#### View Monthly Summary
```bash
dollar summary
```
Shows your total income, expenses, and balance for the current month.

#### List Recent Transactions
```bash
# Show last 10 transactions
dollar list-trans

# Show last 20 transactions
dollar list-trans --limit 20

# Filter by category
dollar list-trans --category "Food"

# Filter by type
dollar list-trans --type expense
```

#### Set Budget Limits
```bash
dollar budget --category "Food" --limit 300.00
```

## Function Workflow

### Core Functions

1. **add_transaction(amount, description, category_name, transaction_type)**
   - Creates a new transaction record in the database
   - Automatically creates categories if they don't exist
   - Validates input data and handles database operations

2. **get_monthly_summary()**
   - Calculates total income and expenses for the current month
   - Returns a tuple: (income, expenses, balance)
   - Uses SQLAlchemy aggregation functions for efficient queries

3. **list_transactions(limit, category, transaction_type)**
   - Retrieves filtered transaction history
   - Returns a list of transaction objects
   - Supports filtering by category and transaction type

4. **set_budget_limit(category_name, limit)**
   - Sets or updates spending limits for categories
   - Creates categories automatically if needed
   - Stores budget information for future reference

5. **get_category_spending()**
   - Analyzes spending patterns by category
   - Returns a list of tuples: [(category_name, total_amount), ...]
   - Provides data for budget analysis and reporting

### Database Schema

The application uses three related tables:

- **Categories**: Stores expense/income categories with optional budget limits
- **Transactions**: Records individual financial transactions
- **BudgetGoals**: Stores financial goals and targets for categories

### Data Structures Used

- **Lists**: Transaction history, category spending reports
- **Tuples**: Monthly summary data, category spending pairs
- **Dictionaries**: Configuration settings, transaction filtering

## Project Structure

```
dollar-cli/
├── dollar_cli/           # Main application package
│   ├── __init__.py      # Database setup and session management
│   ├── cli.py           # Click CLI commands and user interface
│   ├── models.py        # SQLAlchemy ORM models and database schema
│   └── helpers.py       # Business logic and database operations
├── alembic/             # Database migration management
│   ├── versions/        # Migration files
│   └── env.py          # Alembic configuration
├── Pipfile              # Dependency management
├── alembic.ini          # Alembic settings
└── README.md           # This documentation
```

## Dependencies

- **SQLAlchemy**: ORM for database operations
- **Alembic**: Database migration management
- **Click**: Command-line interface framework
- **Python-dateutil**: Date/time utilities

## Development

This project follows Python best practices:
- Separation of concerns (CLI, models, business logic)
- Input validation and error handling
- Clear user prompts and feedback
- Modular package structure
- Virtual environment management with Pipenv