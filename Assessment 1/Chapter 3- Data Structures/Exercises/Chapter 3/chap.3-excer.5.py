#my apologies for having long codes
list = ['alisa','caitlyn','dee']

for num in list:
    print('\nlets have dinner on the new restaurant:',num)

print('\nsadly our guest',list[2],'could not make it')

list.pop(2)
list.append('nearl')

for num in list:
    print('\nlets have dinner on the new restaurant:',num)