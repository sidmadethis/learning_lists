def make_pizza(*toppings):
    """print the list of topping that have been requested"""
    print(toppings)

make_pizza("pepperoni")
make_pizza("mushrooms","green peppers", "extra cheese")

# in the above version the *toppings in the parameter tells python to make an empty tuple called toppings and pack whatever values it gets into this tuple. even if you only get one value, it is still packed into a tuple


# in this version below, we use a loop to go through the list of toppings and print it out correctly
def make_pizza2(*toppings):
    """summarize the pizza about to make"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)

make_pizza2('pepperoni')
make_pizza2('green onions', 'mushrooms', 'extra cheese')
