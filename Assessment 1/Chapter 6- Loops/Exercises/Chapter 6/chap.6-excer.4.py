# not gonna lie, i had to search the internet for this (x-x)
sandwich_orders = ["tuna", "chicken", "ham and cheese", "veggie", "egg salad"]

# empty list 
finished_sandwiches = []

# Loop
for order in sandwich_orders:
    print('I made your', order, 'sandwich.')

    # move the sandwich!
    finished_sandwiches.append(order)


print("I have made the following sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)