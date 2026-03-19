import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Customer': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Amount_Spent': [2500, 3200, 1800, 4000, 2200],
    'Category': ['Electronics', 'Clothing', 'Groceries', 'Electronics', 'Clothing']
})
print(data)

total = data['Amount_Spent'].sum()
print("Total Amount Spent:", total)

avg = data['Amount_Spent'].mean()
print("Average Amount Spent:", avg)

max_spent = data['Amount_Spent'].max()
print("Maximum Amount Spent:", max_spent)

category_spending = data.groupby('Category')['Amount_Spent'].sum()
print("Total Amount Spent by Category:")
print(category_spending)

data.plot(x = 'Customer', y = 'Amount_Spent', kind = 'bar')
plt.title('Amount Spent by Customer')
plt.xlabel('Customer')
plt.ylabel('Amount Spent')
plt.show()