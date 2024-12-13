# function 1
def double_num(num):
    result=num*2
    print(result)
double_num(14)

# function 2
def add(num1,num2):
    sum=num1+num2
    print(sum)
add(10,8)

# function 3 : return a value
def multiply(num1,num2):
    result=num1*num2
    return result
output=multiply(10,5)
print(output)

# function 3: assign a variable to function with no return
def sub(num1,num2):
    result=num1-num2
    print(result)
sub_output=sub(5,3)
print(sub_output)