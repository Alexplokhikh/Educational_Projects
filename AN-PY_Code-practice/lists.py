# different types of items can be stored in a list, including integers, strings, floats, other lists, and dictionaries.

my_list = [456, "hey", 3.14, [1, 2, 3], {"key":"name", "value":"Mario"}]
## ================================================================== ##
print(my_list)
print("\n\n let's see how to access items in the list and manipulate them\n")
## -------- accessing items in the list and slicing

# the length of the list can be found using the len() function
print("the length of the list is: ", len(my_list))
# we can access items in the list using their index, which starts at 0
print("the first item in the list is: ", my_list[0])
# we can also access items from the end of the list using negative indices, where -1 is the last item, -2 is the second to last item, and so on
print("the last item in the list is: ", my_list[-1])
print("\n")

# we can also access a range of items in the list using slicing, which is done using the syntax list[start:end],
# where start is the index of the first item to include and end is the index of the first item to exclude
print("the sublist from index 1 to 3 is: ", my_list[1:4])

print("\nwe can Display THE WHOLE LIST using slicing as well:") 
# note that the end index is exclusive, so we need to use len(my_list) to include the last item in the list
print("the whole list in correct order is: ", my_list[0:len(my_list)])
# or a number greater than the length, see what happens.
print("the whole list from index 0 to a number greater than len: ", my_list[0:100])
# and actually, it is not even necassary. the next one will work just as fine:
print("the whole list from index 0 to the end: ", my_list[0:])

# by omitting the start and end indices, we also can display the whole list
print("again, but written in a different way is: ", my_list[:])
# the output of this exact slicing operation is the same, it displays the whole list in correct order
print("or simply: ", my_list)
print("\n")

### WHY DO YOU THINK ALL OF THESE DIFFERENT WAYS WORK EXACTLY THE SAME? OR, DO THEY ACTUALLY? - google it!

# we can also display the whole list in reverse order using slicing, by using a step of -1
print("the whole list in reverse order is: ", my_list[::-1]) #not using reverse() method, but using SLICING to reverse the list

# individual indices can be manipulated
print("the first item in the list is: ", my_list[0])
# we can change the value of an item in the list by assigning a new value to its index
my_list[0] = 123
print("list after changing the first item: ", my_list)

print("\n\n let's see how to add and remove items from the list\n")
## -------- add, append, extend, insert, pop and remove methods

# append: adds an item TO THE END of the list
append_list = [4, 5, 6]
my_list.append(append_list)
print("list after appending: ", my_list)

# extend: adds EACH ITEM in the given list TO THE END of the original list
extend_list = [7, 8, 9]
my_list.extend(extend_list)
print("list after extending: ", my_list)

# insert: adds an item AT A GIVEN INDEX
my_list.insert(1, "hey")
print("list after inserting 'hey' at index 1: ", my_list)

#pop: REMOVES AND RETURN the item AT THE GIVEN INDEX (by default is the last item)
pop_item = my_list.pop()
print("popped item: ", pop_item)
print("list after popping: ", my_list)
# to REMOVE AN ITEM AT A SPECIFIC INDEX, we can pass the index to the pop() method
pop_item = my_list.pop(5)
print("popped item: ", pop_item)
print("list after popping item at index 5: ", my_list)
# in that manner, to remove the first item in the list, we can pass index 0 to the pop() method
pop_item = my_list.pop(0)
print("popped item: ", pop_item)
print("list after popping the first item: ", my_list)

# remove: removes the first occurrence of the given item from the list
remove_item = [1,2,3]
my_list.remove(remove_item)
print("list after removing: ", my_list)

## -------- other useful list methods: in, count, insert, index
print("\n\n let's see some other useful list methods: in, .count(), .insert(), .index()\n")

# in operator: checks if an item is in the list. returns True if the item is in the list, and False otherwise
print("check if 'hey' is in the list: ", "hey" in my_list)

# count: counts the number of occurrences of an item in the list
print("count of 'hey' appearances in the list: ", my_list.count("hey"))

# insert: adds an item at a given index
# contrary to my_list[index]=item , which replaces the item at the given index...
# insert() method shifts the items to the right and inserts the new item at the given index
my_list.insert(1, "hey")
print("list after inserting 'hey' at index 1: ", my_list)
print("count of 'hey' appearances in the list after inserting: ", my_list.count("hey"))

# index: returns the index of the first occurrence of an item in the list
print("the index of the first appearance of 'hey' in the list is: ", my_list.index("hey"))

## ================================================================== ##

print("\n\nLet's manipulate a list of numbers and sort it:\n")
## -------- .reverse() .sort(), sorted() and reverse sorting.

## our list of numbers 
my_numbers = [5, 2, 9, 1, 5, 6]
print("original numbers list: ", my_numbers)
## ------------------------------------------------------------------ ##

my_reversed_list_of_numbers = my_numbers.reverse()
# the list.reverse() method mutates the original list and returns None
print(".reverse() method Reverses the elements of the list IN-PLACE, and returns None: ", my_reversed_list_of_numbers)
print("we can see that the ORIGINAL LIST gets MUTATED: ", my_numbers)

# sort() function: sorts the list in place (modifies the original list)
# .sort() method does not return a new list, it modifies the original list and returns None

sorted_list = my_numbers.sort()
print("the original, sorted list: ", my_numbers)
print("sorted_list variable: ", sorted_list)

print("\nlet's reinitialize the list of numbers to its original state, before sorting, then look at REVERSE SORTING \n")
my_numbers = [5, 2, 9, 1, 5, 6]
print("original list: ", my_numbers)
# reverse sorting using sort() method
my_numbers.sort(reverse=True)
print("sorted list in reverse order: ", my_numbers)

print("")
# we can also use the sorted() function to sort a list, which RETURNS A NEW sorted list and DOES NOT MODIFY the original list
my_numbers = [5, 2, 9, 1, 5, 6]
print("original list: ", my_numbers)
ascending_list = sorted(my_numbers)
print("sorted list: ", ascending_list)
# my_numbers variable STAYS THE SAME, and additionaly, a new - reversed_list variable is created using that way.
print("original list after sorting: ", my_numbers)

## --------------------------------------------------------------------- ##
## -------- min(), max() and sum() .copy() and .clear()

# from a given list of values we can also determine the minimum and maximum:
print("\nthe highest value of our numbers list is: ", max(my_numbers))
print("and the lowest value of the same list is: ", min(my_numbers))
# we can also obtain the total sum from a list of numbers:
print("the sum of all numbers in this list: ", sum(my_numbers))

print("\nfor avoiding mutation bugs, we can use manipulations on a SHALLOW COPY of a list.")
# to create one, we use the .copy() method:
new_numbers_shallow = my_numbers.copy()
new_numbers_copy = my_numbers

# and with that shallow copy, even if we erased all its content,
# the origin stays untouched. like for instance performing .clear() on the copy

print("the original numbers list: ", my_numbers)
print("the shallow copy: ", new_numbers_shallow)

new_numbers_shallow.clear()
#.clear() - mutates the list, by erasing/DELETING all the content.
print("the shallow copy list after clearing: ", new_numbers_shallow)
# the original remains untouched
print("the original numbers list after clearing the SHALLOW copy: ", my_numbers)

print("but what if we clear a direct copy?")
new_numbers_copy.clear()
print("the DIRECT copy of the original list: ", new_numbers_copy)
# the original gets ALSO ERASED because its pointing to the same place in memory!
print("the original numbers list after clearing the DIRECT copy: ", my_numbers)



### =========================================================================


print("")

print("\nanother useful built-in function to use with lists is the zip() function. \n")
## -------- zip() function: combines two lists into a list of tuples
print("the zip() function aggregates elements from multiple lists (or other iterables)" \
" into an iterator of tuples, matching elements based on their index")

# a list of characters:
my_chars = ["a", "t", "c","f", "b", "e"]
# a list of numbers:
my_numbers = [5, 2, 9, 1, 5, 6]

## we have a list of numbers and a list of characters, we can zip them together to create a list of tuples
combined = list(zip(my_chars, my_numbers))
print(f"the characters list: ", my_chars)
print(f"the numbers list: ", my_numbers)
print(f"the combined list: ", combined)

  # zip() function takes two or more iterables and returns an iterator of tuples,
  #  where the i-th tuple contains the i-th element from each of the input iterables.
if len(my_numbers) == len(my_chars):
  print("the two lists have the same length, we can zip them together")
  mapped_list = list(zip(my_numbers, my_chars))
  for num, char in mapped_list:
    print(f"number: {num}, char: {char}")

print(f"let's create a new list of another characters, but make it longer this time\n")    
print(f"then let's see how does it zips two iterables that are of a different size each.\n")

my_string = "thanks for reading this far!"
my_new_chars = list(my_string)

print(f"this gives us the characters list of: {my_new_chars}")

print(f"this time the chars list is longer than the numbers list. let's zip them, and see it.\n")
  # if the two iterables are of a different length:
  # The returned iterator is truncated in length to the length of the shortest input iterable.
new_zip = list(zip(my_numbers, my_new_chars))
for num, char in new_zip:
  print(f"number: {num}, char: {char}")