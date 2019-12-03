# IF functions
# Control FLow
# While loops also part of control flow

#syntax
# if <condition>:
    ## Block of code
# elif <condition>:
    ## Block of code
# else:
    ## Block of code

# Set user input to pass through loop
age = int(input('whats your age? '))
# Loop deciding what will be printed

if age <= 23 and age > 18:
    print('You are in your prime')
elif age > 23:
    print('Ancient')
elif age >= 12 and age < 18:
    print('You are a teenager')
else:
    print('Infant')