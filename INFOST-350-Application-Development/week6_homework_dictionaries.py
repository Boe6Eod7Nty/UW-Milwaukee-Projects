# Python homework chapter 6 dictionaries

alien_0 = {'color': 'green', 'points': 5} # create a dictionary
print(alien_0['color']) # access a value
print(alien_0['points'])

alien_0['x_position'] = 0   # add a new key-value pair
alien_0['y_position'] = 25
print(alien_0)


alien_0 = {}    # starting with an empty dictionary
alien_0['color'] = 'green'  
alien_0['points'] = 5
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print("Original x_position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points'] # remove a key-value pair
print(alien_0)



favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()  # access a value
print("Sarah's favorite language is " + language + ".") # concatenate strings


user_0 = {  # create a dictionary with key-value pairs
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items(): # for loop to iterate through key-value pairs in a dictionary
    print("\nKey: " + key)
    print("Value: " + value)

friends = ['phil', 'sarah']
for name in favorite_languages.keys(): # for loop to iterate through keys in a dictionary
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(" Hi " + name.title() + ", I see your favorite language is " + language + ".")


for name in sorted(favorite_languages.keys()): # for loop to iterate through keys in a dictionary in order
    print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values(): # for loop to iterate through values in a dictionary
    print(language.title())


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2] # create a list of dictionaries
for alien in aliens: # for loop to iterate through each item in list
    print(alien)


aliens = [] # start with an empty list
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]: # print the first three aliens
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow': # print the three yellow aliens
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

print("The first 5 aliens in the list are: ")
for alien in aliens[:5]:    # print the first five aliens
    print(alien)
print("...")

print("There are " + str(len(aliens)) + " aliens in the list.")

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)


favorite_languages = {
    'jen': ['python', 'ruby'],  # list is used to store multiple values in a single key
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],          # note to not nest lists and dictionaries too deeply,
    }                                       # there's usually a simpler way to solve the problem.

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


