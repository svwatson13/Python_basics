# For loops
## Iterate over an iterable and run a block of code
## Iteratables are: Lists, Ranges, Dictionaries and Strings

#Syntax
## For <placehold> in <iterable>:
    ## Do stuff
    ## Do other things

# Note: The block of code exists after colon (:)
## It is the lines of code that are indented, stops when indentation ends


wish_list = ['RC Car', 'Xbox Controller', 'MW3', 'Money', 'Cheerleaders',
               'Sugar Laces', 'Reeses Pieces', 'Pasteis De Nata']
# ## Import time so we can see loop work slowly
# import time
# import random
# for item in wish_list:
#     print(item)
#     # Wait for 1.2 seconds before iterating again
#     time.sleep(1.2)
#     # Print random number between 200 and 207 every iteration
#     print(random.randint(1, 8))

# Lists within a list
list_data = [['RC Car', 'Xbox Controller', 'MW3', 'Money'],
             ['Sugar Laces', 'Reeses Pieces' 'Pasteis De Nata', 'White Shirts']]
## Iterating through lists within a list
for data in list_data:
    for num in data:
        print(num)

# Counting within a list
a = 0
for item in wish_list:
    a += 1
    print(a, item)

# Loops with dictionaries
dict_data = {
    1: {
        'Name': 'Bronson',
        'Money': 0.50
    },
    2: {
        'Name': 'Dilan',
        'Money': 3.50
    },
    3: {
        'Name': 'Harry',
        'Money': 150
    },
    4: {
        'Name': 'Filipe',
        'Money': 14000 }
}

# Print out keys of dictionary
for item in dict_data:
    print(item)

# Print out keys and values of dictionary
for item in dict_data:
    print(item)
    print(dict_data[item])

# Print out specific values of keys
for item in dict_data:
    print(dict_data[item]['Name'])

# Print name of person and how much they owe based on Money * Interest/12months
for item in dict_data:
    print(dict_data[item]['Name'], 'Owes us: ', (dict_data[item]['Money']*4000/12))

# Can also iterate over a string using index



# WHILE loops and IF statements
# Syntax:
    ## While <condition>:
        ## Block of code
        ## More code

# Using to substitue for loop for printing out items in a list

## Find out lenght of list
print(len(wish_list))

## Create variable containing index length (-1 because lists indexed at 0)
index_length = len(wish_list)-1
counter = 0
while counter <= index_length:
    print(wish_list[counter])
    counter += 1

