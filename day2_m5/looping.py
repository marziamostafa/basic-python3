# looping in list

# default built in function
numbers=[12,45,68,56,45,12,30]
total=sum(numbers)
print("built in : ",total)

# for loop
total_for=0
for i in numbers:
    total_for+=i
print("list total in for loop : ",total_for)


# enumerate
for num in enumerate(numbers):
    print(num)

for i, num in enumerate(numbers):
    print(i,num)

# looping in set
# for loop
num={12,45,68,56,45,12,30}
set_total_for=0
for i in num:
    set_total_for+=i
print("set total in for loop : ",set_total_for)



# looping in tuple
# for loop
number_tuple=12,45,68,56,45,12,30
tuple_total_for=0
for i in number_tuple:
    tuple_total_for+=i
print("tuple : ",number_tuple)
print("set total in for loop : ",tuple_total_for)


# looping in dictionary
# for loop

marks={'physics':12,'chemistry':45,'math':50}

for mark in marks:
    val=marks[mark]
    print(mark,val)

for subject,mark in marks.items():
    print(subject,mark)
