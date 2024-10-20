import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visualize_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses to visualize.")
        return

    df = pd.DataFrame(expenses)

    category_sum = df.groupby('category')['amount'].sum()

    plt.figure(figsize=(6, 6))
    category_sum.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title('Expense Distribution by Category')
    plt.ylabel('')
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.barplot(x=category_sum.index, y=category_sum.values)
    plt.title('Total Spending by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.show()
