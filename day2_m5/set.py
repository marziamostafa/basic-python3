
# list
numbers=[12,45,68,56,45,12,30]
print(numbers)

#set
num={12,45,68,56,45,12,30}
print(num)

# empty set
empty=set()
print(empty)

numbers_set=set(numbers) #numbers becomes a set here and removes the duplicates
print(numbers_set)

# add elements on the set
numbers_set.add(75)
print(numbers_set)

# remove elements from the set
numbers_set.remove(12)
print(numbers_set)

#length
print(len(numbers_set)) 
