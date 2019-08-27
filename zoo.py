# Create a tuple named zoo that contains 10 of your favorite animals.
# Find one of your animals using the tuple.index(value) syntax on the tuple.
# # Example
# flowers = ("daisy", "rose")
# flower.index("rose") # Output is 1
# Determine if an animal is in your tuple by using value in tuple syntax.
# animal_to_find = "kangaroo"
# if animal_to_find in zoo:
# Print that the animal was found
# Create a variable for the animals in your zoo tuple, and print them to the console.
# Convert your tuple into a list.
# Use extend() to add three more animals to your zoo.
# Convert the list back into a tuple.

# A tuple named zoo
zoo = ("zebra", "tiger", "hippo", "pigeon", "walrus",
       "peacock", "elephant", "giraffe", "ostrich", "moose")
whereisthehippo = zoo.index("hippo")
print("The index of hippo in the animal tupple is", whereisthehippo)

# change the animal to find to see how the if statement executes
animal_to_find = "tiger"

if animal_to_find in zoo:
    position_of_animal = zoo.index(animal_to_find)
    print(
        f'I found the {animal_to_find} in the zoo at index {position_of_animal}')
else:
    print("No animal matching your description is in the zoo")

for eachanimal in zoo:
    print("An animal in the zoo is", eachanimal)

# convert tuple into a list
zoo_list = list(zoo)

# add 3 animals using extend
zoo_list.extend(["kangaroo"])
zoo_list.extend(["bear"])
zoo_list.extend(["koala"])

# convert the list back to a tuple
new_zoo = tuple(zoo_list)
print("new tuple-->", new_zoo)
