# abs() makes the number positive even if i give negative number

positive=abs(-3.92)
print(positive)

# all() returns True (all elements are truthy)
numbers=[1,2,3,4]
print(all(numbers))

mixed=[1,0,3,6]
print(all(mixed))

number = [2, 4, 6, 8]
print(all(x%2==0 for x in number))


# any()  returns True if at least one element in the iterable is truthy

check=[0,0,3]
print(any(check))


# dict() cretes a dictionary

pairs = [("name", "Alice"), ("age", 25), ("city", "New York")]
my_dict = dict(pairs)
print(my_dict)

# max() min()
nums={12,45,68,56,45,12,30}
big_nums=max(nums)
min_nums=min(nums)
print(big_nums)
print(min_nums)

# reversed()

nums_rev=reversed([12,45,68,56,45,12,30])
print(list(nums_rev))

# sorted()

sorted_nums=sorted(nums)
sorted_rev=sorted(nums, reverse=True)
print(sorted_nums)
print(sorted_rev)


# sort dictionary
students=[
{'name':'Marzia','age':25},
{'name':'Topu','age':24},
{'name':'Linkon','age':26},
{'name':'Tonmoy','age':24},
{'name':'Rakib','age':21}
]


# sort with age
sorted_std=sorted(students,key=lambda std: std['age'])
print(sorted_std)

sorted_std_rev=sorted(students,key=lambda std: std['age'],reverse=True)
print(sorted_std_rev)

# sort with name
sorted_std_name=sorted(students,key=lambda std: std['name'])
print("\nSort with name: ",sorted_std_name)

sorted_std_name_rev=sorted(students,key=lambda std: std['name'],reverse=True)
print("\nSort with name reversed: ",sorted_std_name_rev)


# sort list
names=['topu','tonmoy','rakib','su','marzia']
sorted_name=sorted(names)
print(sorted_name)