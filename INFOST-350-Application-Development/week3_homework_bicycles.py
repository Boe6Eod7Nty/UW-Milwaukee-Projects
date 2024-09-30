#homework week 3 lists

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] # lists are defined with square brackets
print(bicycles)

print(bicycles[0].title()) # title() capitalizes the first letter of the string

print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# [] is always used for lists, {} is used for dictionaries

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati' # *variable* followed by [brackets] targets an item in a list by the index value in the brackets
print(motorcycles)

motorcycles.append('ducati') # append adds an item to the end of a list
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati') # inserts an item at a specific index
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0] # items can be removed from lists with del
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1]) # -1 targets the list item by reverse index. -1 is the last item, -2 is the second to last item, etc.

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop() # pop removes the last item
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0) # pop removes an item at a specific index when given an index
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati') # remove removes an item from a list
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive) # you can use a variable to store the item you want to remove
print("\nA " + too_expensive.title() + " is too expensive for me.")

# left off on page 47 of python crash course (Matthes)

# continued textbook work on 9/23

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # sort a list in alphabetical order
            # this permanently changes the list values of the variable(list).
                # As oppossed to simply giving a result of the sorting and not saving to the source list's variable memory
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) # reverse=True reverses the order of the sort
print(cars,"\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the sorted list:")
print(sorted(cars))                      # sorted() returns a sorted list, does not change the source list unlike sort()
print("\nHere is the original list:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse() # reverses the order of a list. doesn't sort or order alphabetically, just reverses the existing order.
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Size of cars list:", len(cars))

# added code from python list tutorial YT video
print("\nVideo tutorial code below:\n")

primes = [2, 3, 5, 7, 11, 13]

primes.append(17) # adds a value to the end of a list
primes.append(19)

print(primes)

print(primes[0])
print(primes[2])
print(primes[-2])
print(primes[2:5]) #beginning value is included, ending value is not

numbers = [1, 2, 3]         #create a list of any data type
letters = ['a', 'b', 'c']

print(numbers + letters) # concatenate both lists
print(letters + numbers)

print("\n")
print(dir(primes)) # dir() lists the attributes and methods of an object