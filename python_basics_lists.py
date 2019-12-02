# Lists
## Ordered by indexes
## Lists are also known as arrays or objects in JavaScript

# Syntax
## Define lists using []
## Seperate items using ,

## Creating list with items
crazy_x_landlords = ['Sr. Julio', 'Jane', 'Alfred', 'Marksons']
print(crazy_x_landlords)
print(type(crazy_x_landlords))

# How to access 1 record in the list: <list>[] - index starts at 0
## minus starts from the end so -1 is the last in the list
print(crazy_x_landlords[2])
print(crazy_x_landlords[0])
print(crazy_x_landlords[-1])

# New list of places to live
places_to_live = ['California', 'Rio De Janeiro', 'Melbourne', 'Manchester', 'Singapore']
# Reassign Index
places_to_live[3] = 'Hawaii'
print(places_to_live)

# Method .append()
places_to_live.append('Amsterdam')
print(places_to_live)

# Method .insert(<Index>, <item>): Insert new item
places_to_live.insert(4, 'Prague')
print(places_to_live)

# Method .pop(<Index>): Delete specific item
places_to_live.pop(3)
print(places_to_live)

# List slicing
## Used to manage lists
### Printing from index to end of list - Not including index specified
print(places_to_live[3:])
### Printing from index to beginning of list -Not including index specified
print(places_to_live[:3])
### Printing from specified index to second specified index (Not inlusive of last but does include first)
print(places_to_live[0:3])
### Skip slicing - first number where it starts : middle number is limit : last number is increments
### Start:Stop:Increment
print(places_to_live[0:6:2]) # Start at 0, go to 6 in increments of 2
print(places_to_live[::-1]) # Backwards

# Tuples ()
## Immutable lists
## syntax
mortal_enemies = ('Mario', 'Sailormoon', 'MOON CAKE', 'Jerry', 'Berry')
print(type(mortal_enemies))

#Example of creating amazing list for end of the world survival
list_of_kit = []
item_1 = input('What is your first item to keep?')
list_of_kit.append(item_1)
item_2 = input('What is your first item to keep2?')
list_of_kit.append(item_2)
item_3 = input('What is your first item to keep3?')
list_of_kit.append(item_3)
print("Hey there partner! You have a nice list of stuff!")
print(list_of_kit)