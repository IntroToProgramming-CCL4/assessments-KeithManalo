#my apologies for having long codes
list = ['alisa','caitlyn','dee']

for num in list:
    print('\nlets have dinner on the new restaurant:',num)

print('\nsadly our guest',list[2],'could not make it')

list.pop(2)
list.append('nearl')

for num in list:
    print('\nlets have dinner on the new restaurant:',num)

print('\nmy sincere apologies, there are only 2 seat available \ni could only invite 2 people')

print("sorry but lets have dinner another time",list[0])
list.pop(0)

for num in list:
    print('\nim glad to tell you that you are still invited for dinner:',num)

del list[-2:]

print(list)