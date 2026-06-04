import pandas as pd
import matplotlib.pyplot as plt


data= {
  'order_id': [1,2,3,4,5,6,7,8,9,10],
  'customer': ['Ahmed','Mona','Sara','Khaled','Ahmed','Sara','Ali','Mona','Khaled','Ali'],
  'category':['Electronics','Clothes','Electronics','Clothes','Books','Electronics','Clothes','Books','Electronics','Clothes'],
  'amount': [15000,3000,12000,2500,500,8000,1500,800,6000,2000],
  'month': ['Jan','Jan','Feb','Feb','Mar','Mar','Apr','Apr','May','May']
}

df= pd.DataFrame(data)
# 1. Sales by Category
print('Sales by Category:')
df.groupby('category')['amount'].sum().sort_values(ascending=False)

# 2. Top Customer
print("\nTop Customers:")
df.groupby('customer')['amount'].sum().sort_values(ascending=False)

# 3. Best Performing Month
print('\nSales by Month:')
df.groupby('month')['amount'].sum().sort_values(ascending=False)

# 4. Sales by category Chart
category_sales=df.groupby('category')['amount'].sum()
plt.bar(category_sales.index, category_sales.values)
plt.title('Category Sales')
plt.xlabel('category')
plt.ylabel('amount')
plt.savefig('sales_by_category.png')
plt.show()

# 5. Monthly sales chart

month_order= ['Jan','Feb','Mar','Apr','May']
month_sales= df.groupby('month')['amount'].sum().reindex(month_order)

plt.plot(month_sales.index, month_sales.values)
plt.title('Sales Over Time')
plt.xlabel('month')
plt.ylabel('amount')
plt.savefig('Sales_over_time.png')
plt.show()
