 
# def square(x):
    # return x*x

square= lambda x:x*x   # square is a function now
result=square(3)
print(result)

add=lambda x,y:x+y
sum=add(5,6)
print(sum)


# on a list
numbers=[12,45,68,56,45,12,30]

def double_it(x):
    return x*2

doouble_it2=lambda x:x*2

# map

doubled_numbers=map(double_it,numbers)
doubled_numbers2=map(lambda x:x*2,numbers)

print(numbers)
print(list(doubled_numbers))
print("doubled_numbers2 : ",list(doubled_numbers2))

squared_numbers=map(lambda x:x*x,numbers)
print("squared_numbers : ",list(squared_numbers))


# filter

bigger_numbers=filter(lambda num:num>50, numbers)
print("bigger_numbers: ",list(bigger_numbers))

odd_number=filter(lambda num:num%2!=0,numbers)
print("odd numbers: ",set(odd_number))

even_number=filter(lambda num:num%2==0,numbers)
print("even numbers: ",set(even_number))


students=[
{'name':'Marzia','age':25},
{'name':'Topu','age':24},
{'name':'Linkon','age':26},
{'name':'Tonmoy','age':24},
{'name':'Rakib','age':21}
]

senior_citizen=filter(lambda std:std['age']>24,students)
print(list(senior_citizen))

under_aged=filter(lambda std:std['age']<22,students)
print(list(under_aged))