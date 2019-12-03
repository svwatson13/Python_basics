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
              'Sugar Laces', 'Reeses Pieces' 'Pasteis De Nata']
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
