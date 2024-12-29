marks={'physics':12,'chemistry':45,'math':50}

# change the value
marks['physics']=35
print(marks)

# add on the set
marks['English']= 54
print(marks)

# delete from the set
del marks['chemistry']
print(marks)

# keys of the set
marks_keys=marks.keys()
print(marks_keys)

# values of the set
marks_values=marks.values()
print(marks_values)

# items of the set
marks_items=marks.items()
print(marks_items)

# clear the set
marks.clear()
print(marks)