# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetables)
print(both)
#I think tomato will be printed
# Why does the following code diplay five items?

food = fruit.union(vegetables)
print(food)
#returns elements of fruit and vegetables but does not display duplicates, therefore 5 items
# Add an item to fruit
fruit.add("banana")
print(fruit)

# Remove an item from vegetables
vegetables.discard("potato")
print(vegetables)
# Find and display symmetric difference of the two sets
difference = fruit.symmetric_difference(vegetables)
print(difference)
