#here is the define function to be able to call the command as many times i want
def funct():

    # the container for variables
    is_quit = False
    item = ''

    # the start of the code for it to run
    while is_quit == False:
        
        # initial message when the code runs
        print("\nWelcome to the DSVM - Deluxe Sandwich Vending Machine"
            '\nwhat would you like?\n'
            )
        print('code: Price:\tItem Name:\n')
        
        # the code to list down every item inside the menu
        for i in items:
            print(f"  {i['code']}\t{i['price']}\t{i['name']}")
        
        # the container and query to put the code of the item wanted
        query = int(input("\nEnter the code number of the item you want to get: "))
        
        # the code to list the name of the menu or item once the code is inputed and a container for the variable
        for i in items:
            if query == i['code']:
                item = i
        
        # the code for which the item code is not on the list
        if item == '':
            print('INVALID CODE')
        
        # the code to print out the item you chose after entering the item code
        else:
            print(f"\nWonderful choice, {item['name']} will cost you {item['price']} dollars")
            
            # the container for the money to purchase the menu or item
            price = int(input(f"Enter dollars to purchase: "))
            
            # the code to subract the item price from the money inserted and message for the money dispensed and change
            if price >= item['price']:
                change = price - item['price']
                print(f"\nThank you for buying, here is your {item['name']}")
                print('here is your change:',change)
            
            # incase the money number entered is invalid
            else:
                print('invalid ammount')
            
        # the code for the program to keep running or to quit
        query = input("\nTo quit the machine enter q and to continue buying enter anything: ")
            
        if query == 'q':
                is_quit = True
        else:
                is_quit = False
        print('')

#the initial greeting or statement when the program starts
print('Welcome to Deluxe Sandwich Vending Machine'
      ,'\n\nenter a for Regular Sandwiches'
             '\nenter b for Ice cream Sandwiches'
             '\nenter c for Drinks')

pick = input('\nenter the letter of a category would like to check and buy:')

#from here on out is the if and elif statements for the 3 categories             
if pick == 'a':
    items = [
    {'code': 3, 'name': 'scrambled egg SW', 'price': 3},
    {'code': 4, 'name': 'sunny side up SW', 'price': 3},
    {'code': 5, 'name': 'ham & cheese', 'price': 5},
    {'code': 6, 'name': 'bacon & eggs SW', 'price': 5},
    ]
    funct()

elif pick == 'b':
    items = [
    {'code': 0, 'name': 'vanilla ice cream SW', 'price': 4},
    {'code': 1, 'name': 'chocolat ice cream SW', 'price': 4},
    {'code': 2, 'name': 'strawberry ice cream SW', 'price': 4},
    ]
    funct()

elif pick == 'c':
    items = [
    {'code': 7, 'name': 'coca cola', 'price': 3},
    {'code': 8, 'name': 'pepsi', 'price': 3},
    {'code': 9, 'name': 'fanta orange', 'price': 3},
    {'code': 10, 'name': 'water', 'price': 1},
    ]
    funct()