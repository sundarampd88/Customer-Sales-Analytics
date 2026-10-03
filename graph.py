import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("cleaned.csv")

product_sales = data.groupby("Product")["Total_Sales"].sum()

bars = plt.bar(product_sales.index, product_sales.values)

plt.title("Product-wise Total Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales (₹)")

for bar, value in zip(bars, product_sales.values):
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"₹{value}",
        ha="center",
        va="bottom"
    )

plt.show()