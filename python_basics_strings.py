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

## Useful method for stings
