# Week 5 Homework, If Statements

# Basic If Statement Syntax
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


requested_topping = 'mushrooms'
if requested_topping != 'anchovies': # != tests if two values are not equal
    print("Hold the anchovies!")

age = 18
if age == 18: # == tests if two values are equal, 1 = is an assignment operator
    print("You are old enough to vote!")


age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21: # 'and' can be used to test multiple conditions
    print("You are old enough to drink!")

age = 12
if age < 4:
    price = 0
elif age < 18: # 'elif' can be used to test additional conditions if the previous condition is not met
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".") # str() converts a value to a string


requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")


available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings: # 'in' can be used to test if a value is in a list
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

