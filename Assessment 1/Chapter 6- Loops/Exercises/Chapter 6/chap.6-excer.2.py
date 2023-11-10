#i nested a conditional statement inside a while loop (O _ O)

while True:
    age = int(input("Enter your age: ")) 
    if age < 3: 
        print("Your ticket is free.")
    elif age <= 12: 
        print("Your ticket is $10.")
    else: 
        print("Your ticket is $15.")