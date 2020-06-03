# reporter.py

import pandas as pd
import numpy as np
import os

csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "sales-201710.csv")

df = pd.read_csv(csv_filepath)

sales = df.to_dict("records")

total_sales = 0

for x in sales:
    total_sales = total_sales + x["sales price"]

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

total_sales = to_usd(total_sales)

print("GENERATING SALES REPORT FOR MONTH OF OCTOBER 2017...")
print(" ")
print("Sales Report (OCTOBER 2017)")
print(" ")
print("Total Sales: " + str(total_sales))
print(" ")

print("Top Selling Products:")

sales = pd.read_csv(csv_filepath)
grouped = sales.groupby("product").sum()
top_products = grouped.nlargest(1000, "sales price")
print(top_products[['sales price']])