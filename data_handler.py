import pandas as pd

def load_expenses_from_csv(filename='expenses.csv'):
    try:
        return pd.read_csv(filename).to_dict(orient='records')
    except FileNotFoundError:
        return []

def save_expenses_to_csv(expenses, filename='expenses.csv'):
    df = pd.DataFrame(expenses)
    df.to_csv(filename, index=False)

def add_expense(expenses, amount, date, category, description=None):
    new_expense = {
        'amount': amount,
        'date': date,
        'category': category,
        'description': description
    }
    expenses.append(new_expense)

def get_monthly_summary(expenses, month, year):
    expenses_df = pd.DataFrame(expenses)
    expenses_df['date'] = pd.to_datetime(expenses_df['date'])
    monthly_expenses = expenses_df[(expenses_df['date'].dt.month == month) & (expenses_df['date'].dt.year == year)]
    summary = monthly_expenses.groupby('category')['amount'].sum()
    return summary
