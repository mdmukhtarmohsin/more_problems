type Item = dict[str,str|float]
cart=[]
def add_item(item:Item):
    cart.append(item)
    print(f"{item} added to cart")



def remove_item(item:Item):
    cart.remove(item)
    print(f"{item} removed from cart")

def remove_last_item():
    cart.pop()
    print("last item removed from cart")

def view_cart():
    print(cart)

def display_alphabetical_order():
    print(sorted(cart,key=lambda x:x['name']))

def clear_cart():
    cart.clear()
    print("cart cleared")

def display_cart_with_indices():
    for index,item in enumerate(cart):
        print(f"{index+1}. {item}")

def display_cart_with_indices_and_prices():
    for index,item in enumerate(cart):
        print(f"{index+1}. {item['name']} - ${item['price']}")

add_item({'name':'apple','price':1.99})
add_item({'name':'banana','price':0.99})
add_item({'name':'orange','price':2.99})
add_item({'name':'pear','price':1.49})
add_item({'name':'pineapple','price':3.99})

display_cart_with_indices()
display_cart_with_indices_and_prices()
display_alphabetical_order()
view_cart()
remove_item({'name':'apple','price':1.99})
view_cart()
remove_last_item()
view_cart()
clear_cart()    
view_cart()