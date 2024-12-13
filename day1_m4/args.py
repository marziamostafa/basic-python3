def add(num1,num2):
    result=num1+num2
    print(num1, num2)
    return result
total= add(num2=16,num1=20)

# oprional parameter: default parameter
def multiply(num1,num2=3):
    result=num1*num2
    return result
output= multiply(5)
print(output)

# tuple

def multiply2(*num): #arbitrary positional arguments tuple
    print(num)
    print(type(num))
    #return result
final_result=multiply2(4,5,6)
print(final_result)

# tuple with loop

def multiply3(*num): #arbitrary positional arguments tuple
    result=1
    for n in num:
        result=result*n
        #print(n)
    print(type(num))
    return result
final_result=multiply3(4,5,6,7,8)
print(final_result)

# tuple and usual parameter
def multiply4(num1,num2,*num): #arbitrary positional arguments tuple
    result=1
    print(num1,num2,num)
    print(type(num))
    #return result
final_result=multiply4(4,5,6,7,8)
print(final_result)
