import sys

usernameslist = [
   ["Legend27", "a1s2d3f4"],
   ["james123", "c5bt43f4"],
   ["DaveIsGreat", "wlervtb3r"]
]
products = [
    ['google pixel 7', 1000],
    ['Chevy volt 2019', 15000],
    ['Macbook pro M2', 3499],
    ['Microsoft Surface Pro', 3649]
]
username = input("Username ")
password = input("password ")

found = False

for user in usernameslist:    
    if username == user[0] and password == user[1]:
        print("welcome")
        found = True
        break

if not found:
    sys.exit()
for i, product in enumerate(products):
    print(f"[{i}] {product[0]} - {product[1]}")
chosen_product = input("Choose product: ")
product_to_purchase = None
if chosen_product.isdigit():
    chosen_product = int(chosen_product)
    if chosen_product < len(products):
        product_to_purchase = products[chosen_product]
if product_to_purchase is None:
    print('selected prduct does not exist')
else:
    print(f"you have chosen {product_to_purchase[0]}, price: {product_to_purchase[1]} USD")