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