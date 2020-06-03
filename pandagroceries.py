# groceries.py

#TODO Assemble a new products variable by pulling from CSV file
import pandas
import os

#csv_filepath = "data/products.csv"
csv_filepath = os.path.join(os.path.dirname(__file__), "data", "products.csv")
df = pandas.read_csv(csv_filepath)
print(type(df)) #> <class 'pandas.core.frame.DataFrame'>
print(df.head()) #> prints first few rows
products = df.to_dict("records")

#os.path.dirname(__file__) #references current file / where we are right now
#".." #in current directory
#"data" #goes into the data directory


#csv_filepath = "data/products.csv"
# df = pandas.read_csv(csv_filepath)
# print(df.head())

#todo: assemble a list of dictionaries

#Approach A
# products = []
# for row in _____: #how to loop through each row in a dataframe
#     products.append({}) #how to convert each row to a dictionary

#Approach B
# products = df.to_dict("records")

exit()

# products = [
#     {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
#     {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
#     {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
#     {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
#     {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
#     {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
#     {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
#     {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
#     {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
#     {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
#     {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
#     {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
#     {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
#     {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
#     {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
#     {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
#     {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
#     {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
#     {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
#     {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
# ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
#>list
# pprint(products)

# TODO: write some Python code here to produce the desired output

#Products

print("-------------------")
print("There Are", len(products), "Products")
print("-------------------")

def sort_by_name(any_product):
    return any_product["name"]
    #sorts products by name
sorted_products = sorted(products, key=sort_by_name)


for p in sorted_products:
    #print("_____")
    #print(p)
    #concatenate string 
    # #use str to make int into str w/i dict
    #price_usd = p["price"] #price attribute
    price_usd = "${0:.2f}".format(p["price"])
    print("+" + p["name"] + " (" + str(price_usd) + ")")
    #concatenate string 
    # #use str to make int into str w/i dict 
    
#Departments
departments = []
for p in products:
    #print(p["department"])
    #departments.append(p["department"])
    if p["department"] not in departments:
        departments.append(p["department"])

department_count = len(departments)    

print("-------------------")
print("There Are " + str(department_count) + " Departments")
print("-------------------")

departments.sort()

for d in departments:
    matching_products = [p for p in products if p["department"] == d]
    matching_products_count = len(matching_products)
    if matching_products_count > 1:
        label = "products"
    else:
        label = "product"
    print(d.title() + " (" + str(matching_products_count) + " "  + label + ")")
