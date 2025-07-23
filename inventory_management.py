inventory = {
    "apples": {"price": 1.50, "quantity": 100},
    "bananas": {"price": 0.75, "quantity": 150},
    "oranges": {"price": 2.00, "quantity": 80}
}


def add_product(product:str,price:float,quantity:int):
    inventory[product] = {"price":price,"quantity":quantity}
    print(f"{product} added to inventory")

def update_price(product:str,price:float):
    inventory[product]["price"] = price
    print(f"{product} price updated to {price}")

def update_quantity(product:str,quantity:int):
    inventory[product]["quantity"] = quantity
    print(f"{product} quantity updated to {quantity}")

def calculate_total_value():
    total_value = sum(item["price"] * item["quantity"] for item in inventory.values())
    print("Total inventory value:", total_value)

def display_low_stock():
    low_stock = [product for product, details in inventory.items() if details["quantity"] < 100]
    print("Low stock products:", low_stock)

def sell_product(product:str,quantity:int):
    if product in inventory:
        if inventory[product]["quantity"] >= quantity:
            inventory[product]["quantity"] -= quantity
            print(f"{quantity} {product} sold")
        else:
            print(f"Not enough {product} in stock")
    else:
        print(f"{product} not found in inventory")

def display_inventory():
    print(inventory)

add_product("pears",2.50,60)
update_price("bananas",0.85)
update_quantity("apples",75)
calculate_total_value()
display_low_stock()
sell_product("apples",20)