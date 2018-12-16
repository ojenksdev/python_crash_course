def make_pizza(size, *toppings):
    """Summarize an order of Pizza"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
