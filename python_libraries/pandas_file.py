
"""
1.What is Pandas?
* Pandas is a powerful library in python used for data analysis and manipulation.

2.What is DataFrame in Python?
* A DataFrame is a core data structure in Pandas, used to store tabular data (like an Excel sheet or SQL table).

"""
# Exercise-1
# Create the simple pandas data frame.
import pandas as pd
"""
data = {
    "Name":["Jerry","Kalvin","Edison","Akash","Alice"],
    "Age" :[24,26,30,19,19],
    "City" : ["Tirunelveli","Bangalore","Italy","Trichy","Madurai"]
}

data_details = pd.DataFrame(data)
print(data_details["Name"])
print(data_details.dtypes)

"""
"""
Exercise-2

data = pd.read_csv("data.csv")
print(data["Place"])

data["Name"].to_csv("sibling.csv",index=False) # Its create and paste the particular details in another csv file.

data.to_csv("details.csv",index=False) # Its create and paste the another csv file.

"""
# Exercise-3
# Step -1 read csv file
"""

sales_data = pd.read_csv("sales.csv")

#print(sales_data)

# Step -2 Add a new column - Total
sales_data["Total"] = sales_data['Price'] * sales_data["Quantity"]

# Step -3 Group by product

grouped = sales_data.groupby("Product")['Total'].sum().reset_index()

# Step -4 Sort by sales

sorted_sales_data = grouped.sort_values(ascending=False,by="Total")

# output
print("Sales Summery:")
print(sorted_sales_data)

"""
"""
output
Sales Summery:
  Product  Total
0    Pant   4500
1   Shirt   3800

"""

"""
Exercise-4

# read the json file.
brother_data = pd.read_json("data.json")

# Display the DataFrame
print(brother_data)

# convert DataFrame to json format
brother_data.to_json("output.json",orient="records",indent=2)
"""
"""

# Exercise-5

# Two tables insert and find the customer id...
# customer Table:-
customers = {
    "Customer_Id":[1,2,3,4,],
    "Name":["Jerry","Akash",'Alice',"Edison"]
}
# order table:-
orders ={
    "Order_Id":[101,102,103,104],
    "Customer_Id":[1,2,1,3],
    "Products":["Shirt","Pant",'Shoes','Bat']

}

customer_df = pd.DataFrame(customers)
order_df = pd.DataFrame(orders)

# merge or join the table

result = pd.merge(customer_df,order_df,how="inner",on="Customer_Id")
print("Inner Join:")
print(result)

#output:-

Inner Join:
   Customer_Id   Name  Order_Id Products
0            1  Jerry       101    Shirt
1            1  Jerry       103    Shoes
2            2  Akash       102     Pant
3            3  Alice       104      Bat
"""
# Exercise-6

# To create the header names of the csv file.
"""
edit_sales = pd.read_csv("sales.csv",header=None,names=["Date","Product","Price","Quantity"])
print(edit_sales)

result = pd.read_csv("details.csv",header=None,names=["Name","Age","Place"])
print(result)
"""
