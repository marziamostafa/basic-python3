numbers=[12,45,68,56,45,12,30]

odd_numbers=[]

for i in numbers:
    if i%2!=0:
        odd_numbers.append(i)
print(odd_numbers)

# 1. comprehension in list
# [expression for item in iterable if condition]

odd_numbers2=[num for num in numbers if num%2!= 0 if num%5==0] #multiple condition
print(odd_numbers2)

double_it=[num*2 for num in numbers]
print(double_it)


names=['topu','tonmoy','rakib','su','marzia']
ages=[23,23,21,21,24]

# nested for loop
pair=[(name,age) for name in names for age in ages if age<23]

print(pair)