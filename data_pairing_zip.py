products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [999.99, 25.50, 75.00, 299.99]
quantities = [5, 20, 15, 8]

print({product:price for product,price in zip(products,prices)})
print("-"*20)

print({f"{product} - {price*quantity}" for product,price,quantity in zip(products,prices,quantities)})
print("-"*20)
print({
    product:{
        'price':price,
        'quantity':quantity
    }
    for product,price,quantity in zip(products,prices,quantities)
})
print("-"*20)
print({f"{product} - {quantity}" for product,quantity in zip(products,quantities) if quantity <10})