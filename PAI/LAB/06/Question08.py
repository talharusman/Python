import pandas as pd

products_df = pd.read_csv('products.csv')
orders_df = pd.read_csv('orders.csv')

print("Products DataFrame:")
print(products_df.head())
print(products_df.tail(10))

print("\nOrders DataFrame:")
print(orders_df.head())
print(orders_df.tail(10))

orders_df['Total Revenue'] = orders_df['Quantity'] * products_df.set_index('ProductID').loc[orders_df['ProductID'], 'Price'].values
total_revenue = orders_df['Total Revenue'].sum()
print(f"\nTotal Revenue Generated: ${total_revenue:.2f}")

best_selling = orders_df.groupby('ProductID')['Quantity'].sum().nlargest(5)
low_selling = orders_df.groupby('ProductID')['Quantity'].sum().nsmallest(5)

print("\nTop 5 Best-Selling Products:")
print(best_selling)

print("\nTop 5 Low Selling Products:")
print(low_selling)

top_products_ids = best_selling.index
top_categories = products_df[products_df['ProductID'].isin(top_products_ids)]['Category']
most_common_category = top_categories.mode()[0]
print(f"\nMost Common Product Category Among Top 5 Best-Selling Products: {most_common_category}")

average_price_per_category = products_df.groupby('Category')['Price'].mean()
print("\nAverage Price of Products in Each Category:")
print(average_price_per_category)

orders_df['Order Date'] = pd.to_datetime(orders_df['Order Date'])
revenue_by_date = orders_df.groupby(orders_df['Order Date'].dt.date)['Total Revenue'].sum()
highest_revenue_date = revenue_by_date.idxmax()
highest_revenue = revenue_by_date.max()
highest_revenue_day = highest_revenue_date.day
highest_revenue_month = highest_revenue_date.month
highest_revenue_year = highest_revenue_date.year
print(f"\nDay with Highest Revenue: {highest_revenue_day}, Month: {highest_revenue_month}, Year: {highest_revenue_year}")

monthly_revenue = orders_df.groupby(orders_df['Order Date'].dt.to_period('M'))['Total Revenue'].sum()
monthly_revenue_df = monthly_revenue.reset_index(name='Total Revenue')
monthly_revenue_df['Order Date'] = monthly_revenue_df['Order Date'].dt.to_timestamp()
print("\nTotal Revenue for Each Month:")
print(monthly_revenue_df)

null_values_products = products_df.isnull().sum()
null_values_orders = orders_df.isnull().sum()

print("\nNull Values in Products DataFrame:")
print(null_values_products)

print("\nNull Values in Orders DataFrame:")
print(null_values_orders)

products_df.dropna(inplace=True)
orders_df.dropna(inplace=True)
