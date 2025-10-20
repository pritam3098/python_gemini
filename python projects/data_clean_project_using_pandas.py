import pandas as pd

# Raw food order data for a simple cleaning project
raw_order_data = [
    {'order_id': 101, 'order_date': '2025-10-11', 'item_name': 'Pizza Slice', 'price': '$150.00', 'quantity': 2},
    {'order_id': 102, 'order_date': '2025-10-11', 'item_name': ' Chiken Burger', 'price': '250', 'quantity': 1},
    {'order_id': 103, 'order_date': '2025-10-11', 'item_name': 'Soft Drink', 'price': '$50.00', 'quantity': 2},
    {'order_id': 104, 'order_date': '2025-10-12', 'item_name': 'Pizza slice', 'price': '150', 'quantity': 1},
    {'order_id': 105, 'order_date': '2025-10-12', 'item_name': 'French Fries', 'price': None, 'quantity': 1},
    {'order_id': 106, 'order_date': '2025-10-12', 'item_name': 'Chicken Burger', 'price': '$250.00', 'quantity': 2},
    {'order_id': 102, 'order_date': '2025-10-11', 'item_name': 'Chiken Burger', 'price': '250', 'quantity': 1},
    {'order_id': 107, 'order_date': '2025-10-13', 'item_name': 'soft drink', 'price': '50', 'quantity': None}
]

df=pd.DataFrame(raw_order_data)
print(f"orginal shape{df}")

remove_duplicates=df.drop_duplicates(subset=['order_id'],keep='first',inplace=True)

print(f"after removing the duplicates:{remove_duplicates}")

df['price']=pd.to_numeric(df['price'].str.replace('$','',regex=False),errors='coerce')

median_price=df['price'].median()

df['item_name']=df['item_name'].str.strip().str.lower()
df['item_name']=df['item_name'].str.replace('chiken','chicken',regex=False)
#df['item_name']=df['item_name'].unique()
print(df)