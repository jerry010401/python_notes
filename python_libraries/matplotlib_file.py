# MATPLOTLIB is a python library used to create static,animated and interactive plots.

# The main module:
# 1. pyplot - provides functions to make plots just like MATLAB.

# 1. create simple line plot:-

import matplotlib.pyplot as plt
"""
x = [1,2,3,4]
y = [10,20,30,40]

plt.title("Simple line plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot(x,y)
plt.savefig("simpleline_plot.png")
plt.show()

"""

# create simple bar plot
"""
x = ["Apple","Banana","Mango","Orange"]
y = [20,50,30,40]

plt.bar(x,y ,color = "Blue")
plt.title("Fruits count")
plt.ylabel("Count")
plt.savefig("simplebar_plot.png")
plt.show()
"""

# create a scatter plot
"""
x = [1,2,3,4,5,6]
y = [20,17,36,45,30,25]

plt.scatter(x,y,color="Red")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple scatter plot")
plt.savefig("scatter_plot.png")

plt.show()
"""

# read the csv file and create the simple line plot.
"""
import csv

months = []
expense = []

with open("data.csv","r")as file:
    reader = csv.DictReader(file)
    for row in reader:
        months.append(row["Months"])
        expense.append(int(row["Expense"]))

# plot the data.

plt.title(" Monthly Expense Details")
plt.plot(months,expense,color = "Red",marker="o")
plt.xlabel("Months")
plt.ylabel("Expense")
plt.grid(True)
plt.tight_layout()
plt.savefig("expense_details_plotline.png")
plt.show()

"""

