import click
from .helpers import *
from .models import TransactionType

# This creates a group of commands that all start with 'dollar'
@click.group()
def cli():
    """Dollar-CLI - A simple budget tracker for your command line"""
    pass

@cli.command()
@click.option('--amount', type=float, required=True, help='How much money? (e.g., 50.00)')
@click.option('--description', prompt='Description', help='What was this for? (e.g., "Groceries")')
@click.option('--category', prompt='Category', help='Budget category (e.g., "Food", "Rent")')
@click.option('--type', type=click.Choice(['income', 'expense']), prompt='Type (income/expense)', help='Income or expense?')
def add(amount, description, category, type):
    """Add a new income or expense transaction"""
    try:
        # Input validation - amount must be positive
        if amount <= 0:
            click.echo("Error: Amount must be greater than 0")
            return
            
        transaction = add_transaction(amount, description, category, type)
        click.echo(f"Added {type}: ${amount:.2f} for {description}")
    except Exception as e:
        click.echo(f" Error: {str(e)}")

@cli.command()
def summary():
    """Show your monthly income, expenses, and balance"""
    try:
        # Get the monthly summary (returns a tuple)
        income, expenses, balance = get_monthly_summary()
        
        click.echo("\n=== Your Monthly Summary ===")
        click.echo(f"Income:   ${income:.2f}")
        click.echo(f" Expenses: ${expenses:.2f}")
        click.echo(f"  Balance:  ${balance:.2f}")
        
        # Helpful message based on balance
        if balance < 0:
            click.echo(" You're spending more than you're earning this month!")
        elif balance == 0:
            click.echo("You're breaking even this month.")
        else:
            click.echo(" You're saving money this month!")
            
    except Exception as e:
        click.echo(f"Error: {str(e)}")

@cli.command()
@click.option('--limit', default=10, help='How many transactions to show? (default: 10)')
@click.option('--category', help='Filter by category (e.g., "Food")')
@click.option('--type', type=click.Choice(['income', 'expense']), help='Filter by type (income/expense)')
def list_trans(limit, category, type):
    """Show your recent transactions"""
    try:
        # Get transactions (returns a list)
        transactions = list_transactions(limit, category, type)
        
        if not transactions:
            click.echo("No transactions found. Add some with 'dollar add'!")
            return
            
        click.echo(f"\n=== Your Recent Transactions ===")
        
        # Show each transaction with clear formatting
        for transaction in transactions:
            emoji = "💰" if transaction.type == TransactionType.INCOME else "💸"
            click.echo(f"{emoji} {transaction.date.strftime('%Y-%m-%d')} | "
                      f"${transaction.amount:8.2f} | "
                      f"{transaction.description:20.20} | "
                      f"{transaction.category.name}")
                      
    except Exception as e:
        click.echo(f" Error: {str(e)}")

@cli.command()
@click.option('--category', required=True, help='Category name (e.g., "Food")')
@click.option('--limit', type=float, required=True, help='Monthly limit (e.g., 300.00)')
def budget(category, limit):
    """Set a monthly spending limit for a category"""
    try:
        # Input validation - limit must be positive
        if limit <= 0:
            click.echo(" Error: Budget limit must be greater than 0")
            return
            
        set_budget_limit(category, limit)
        click.echo(f" Set monthly budget for '{category}' to ${limit:.2f}")
    except Exception as e:
        click.echo(f" Error: {str(e)}")

@cli.command()
def budget_status():
    """Show budget status for all categories with limits"""
    try:
        # Import the new function
        from .helpers import get_budget_status
        
        # Get budget status (returns a dictionary)
        status_dict = get_budget_status()
        
        if not status_dict:
            click.echo("No budget limits set. Use 'dollar budget' to set limits!")
            return
            
        click.echo("\n=== Budget Status ===")
        
        # Iterate through the dictionary to show each category's status
        for category_name, budget_info in status_dict.items():
            emoji = "🚨" if budget_info['over_budget'] else "✅"
            
            click.echo(f"\n{emoji} {category_name}:")
            click.echo(f"   Budget: ${budget_info['budget_limit']:.2f}")
            click.echo(f"   Spent:  ${budget_info['amount_spent']:.2f}")
            click.echo(f"   Left:   ${budget_info['remaining']:.2f}")
            click.echo(f"   Used:   {budget_info['percentage_used']:.1f}%")
            
            if budget_info['over_budget']:
                click.echo("   ⚠️  Over budget!")
                
    except Exception as e:
        click.echo(f" Error: {str(e)}")

# This makes the CLI work when run directly
if __name__ == '__main__':
    cli()