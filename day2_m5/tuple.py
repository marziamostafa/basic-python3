numbers=[12,45,68,56,45,12,30]
print(numbers)

# tuple
number_tuple=12,45,68,56,45,12,30
print(number_tuple)

nums_tuple=(12,68,56,45,30)
print(nums_tuple)
print(nums_tuple[2])

# if we give mutable vlaue in tuple we can change

tuple2D=([12,45,68,56],[45,12,30])
tuple2D[0][1]=25
print(tuple2D)

#  make a tuple from any list
tuple_from_list=tuple(numbers)
print(tuple_from_list)