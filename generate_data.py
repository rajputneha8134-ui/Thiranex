import pandas as pd
import numpy as np

np.random.seed(42)

products = [
    "Laptop",
    "Smartphone",
    "Tablet",
    "Headphones",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Printer",
    "Smartwatch",
    "Webcam"
]

categories = {
    "Laptop": "Electronics",
    "Smartphone": "Electronics",
    "Tablet": "Electronics",
    "Headphones": "Accessories",
    "Keyboard": "Accessories",
    "Mouse": "Accessories",
    "Monitor": "Electronics",
    "Printer": "Office",
    "Smartwatch": "Wearables",
    "Webcam": "Accessories"
}

regions = ["North", "South", "East", "West"]

start_date = "2025-01-01"
end_date = "2025-12-31"

dates = pd.date_range(start=start_date, end=end_date, periods=500)

data = []

for i in range(500):

    product = np.random.choice(products)
    category = categories[product]
    region = np.random.choice(regions)

    quantity = np.random.randint(1, 10)

    price_range = {
        "Laptop": (50000, 90000),
        "Smartphone": (15000, 60000),
        "Tablet": (10000, 40000),
        "Headphones": (1000, 8000),
        "Keyboard": (800, 5000),
        "Mouse": (400, 3000),
        "Monitor": (8000, 30000),
        "Printer": (5000, 25000),
        "Smartwatch": (3000, 20000),
        "Webcam": (1500, 10000)
    }

    min_price, max_price = price_range[product]

    unit_price = np.random.randint(min_price, max_price)

    sales = quantity * unit_price

    discount = np.random.choice([0, 5, 10, 15])

    revenue = sales - (sales * discount / 100)

    data.append([
        i + 1,
        dates[i],
        product,
        category,
        region,
        quantity,
        unit_price,
        discount,
        sales,
        revenue
    ])

columns = [
    "Order_ID",
    "Date",
    "Product",
    "Category",
    "Region",
    "Quantity",
    "Unit_Price",
    "Discount",
    "Sales",
    "Revenue"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("sales_data.csv", index=False)

print("Sales dataset created successfully!")
print(f"Total records: {len(df)}")
print("File saved as sales_data.csv")