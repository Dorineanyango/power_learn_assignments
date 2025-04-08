#create an empty list
my_list = []

#append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Print the list
print("Initial list:", my_list)

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Print the list after insertion
print("List after inserting 15 at index 1:", my_list)

# Extend the list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# Print the list after extending
print("List after extending with [50, 60, 70]:", my_list)

# Remove the last element
my_list.pop()

# Print the list after removing the last element
print("List after removing the last element:", my_list)

# Sort the list in ascending order
my_list.sort()

# Print the sorted list
print("Sorted list:", my_list)

# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)