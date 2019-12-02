# Strings
## Define String - using '' and ""
my_string = "I'm an amazing string"
my_string2 = 'So am I'

# Concatenation - Using + to concatenate and ' ' to create spaces or commas to do both
print('this is an example of concatenation ' + my_string)
print('this is an example of concatenation ' + my_string + ' ' + my_string2)
print('this is an example with no plusses', my_string, my_string2)
## Concatenated within a variable
concat_varaible = my_string +' '+ my_string2
print(concat_varaible)

# Interpolation
age = 21
name = 'Julia'
year = 2019
## This is where we need to interpolate
print('Welcome <person>, year are <age_years> old')
print('Welcome <person>, you were born on the year <date_birth>')

## This is us interpolating values
print(f'Welcome {name}, year are {age} old')
print(f'Welcome {name}, you were born on the year {year-age}')
print('Welcome {}, you were born on the year {}'.format(name, year-age))

# Useful method for stings
example_string = " HELLoo "
## Remove trailing white spaces
print(example_string.strip())
## Count for specifics e.g number of L's in string:
print(example_string.count('L'))
print(example_string.lower())
print(example_string.upper())
## First letter capital
print(example_string.capitalize())
## Chaining methods
print(example_string.strip().capitalize())

## Learning and using .split()
### Splits where you tell it e.g splitting the white space or where there is a letter i
text_to_split = 'this is some example text in our file'
results_split = text_to_split.split(' ')
results_split = text_to_split.split('i')
print(results_split)


# Standard built in functions
## length - not dependent upon the object(string)
print(len(example_string))

## casting and int
str_string = '1990'
## String --> Int
int_number = int(str_string)
print(type(int_number))
## Int --> String
new_str = str(int_number)
print(type(new_str))