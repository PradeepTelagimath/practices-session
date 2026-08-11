# Read inputs
product_id = input()
product_name = input()
category = input()
unit_price = float(input())
quantity = int(input())
reorder_level = int(input())

# Store product details in a tuple (excluding reorder_level)
product_tuple = (product_id, product_name, category, unit_price, quantity)

# Access product ID and product name using tuple indexes
indexed_product_id = product_tuple[0]
indexed_product_name = product_tuple[1]

# Unpack the complete tuple into separate variables
p_id, p_name, p_category, p_price, p_quantity = product_tuple

# Calculate the stock value
stock_value = p_price * p_quantity

# Determine the stock status
if p_quantity == 0:
    stock_status = "Out of Stock"
elif 0 < p_quantity <= reorder_level:
    stock_status = "Reorder Required"
else:
    stock_status = "Sufficient Stock"

# Display the processed product record
print(f"Product ID: {indexed_product_id}")
print(f"Product Name: {indexed_product_name}")
print(f"Category: {p_category}")
print(f"Unit Price: {p_price:.2f}")
print(f"Available Quantity: {p_quantity}")
print(f"Stock Value: {stock_value:.2f}")
print(f"Stock Status: {stock_status}")