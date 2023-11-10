# not gonna lie, i had to search the internet for this (x-x), update im stillusing it to help me (OwO)
sandwich_orders = ["tuna", 'pastrimi', "chicken", 'pastrimi', "ham and cheese", 'pastrimi', "veggie", "egg salad"]

#the message
print('Sorry, the deli have run out of pastrami.')

# remove those pastrimissssssss
while 'pastrimi' in sandwich_orders:
    sandwich_orders.remove('pastrimi')

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