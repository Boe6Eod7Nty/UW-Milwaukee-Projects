
magicians = ['alice', 'david', 'carolina']
for magician in magicians: # for loop to iterate through each item in list
    print(magician.title() + ", that was a great trick!")                       # each line in the for loop is indented 1 tab
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")

for value in range(1,5): # range() functions create a list of numbers from 1 to 5.
    print(value)         # When used in a for loop, it will iterate through each value in the list excluding the last value.

numbers = list(range(1,6)) # list() creates a list from an iterable object. (range() in this case)
print(numbers)

even_numbers = list(range(2,11,2)) # third argument in range() is the step amount & starting point. 2,4,6,8,etc
print(even_numbers)

# merging previous concepts
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print( min(digits)
     , max(digits)
     , sum(digits)
     )

# list comprehensions, combines the for loop and creation of elements into one line.
squares = [value**2 for value in range(1,11)]
print(squares)

# Try it yourself on page 64


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # list can be sliced, 0:3 = 0,1,2

print(players[-3:]) # -3: = last 3 players

print("Here are the first three players on my team:")
for player in players[:3]: # looping through a sliced list
    print(player.title())



my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]                      # use [:] to make a copy of the list
                                                # friend_foods = my_foods doesn't work. It creates a reference to the same list.
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Try it yourself on page 69

# Creating a tuple, which is like a list, but cannot be changed.
dimensions = (200, 50) # () as variable creates a tuple
for dimension in dimensions:
    print(dimension)

# code styling

# Always indent 4 spaces (1 tab) for levels

# max line length of 80 characters
#23456789ten3456789twenty6789thirty6789fourty6789fifty56789sixty56789seventy7890
#===============================================================================
# comment lines limited to 72 characters ==============================|

# blank lines should be used to group your program visually

