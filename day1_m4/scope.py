# from a local scope we can access or read a global variable but we cant set the value of s global variable. 
# to set it we have to use 'global' keyword and call the global variable

balance=580 # global variable

def total_cost(price,quantity):
    global balance
    cost=price*quantity
    remaining=balance-cost
    balance=balance-cost  #set the global variable value
    print(remaining)
    return cost

print(f"Balance before: {balance}")

pay=total_cost(10,3)
print('please pay: ',pay)
print(f"Balance after:{balance}")


""" 
-->global variable is not recommended to use
--> it creates bug
-->reduce readability
--> tough to find out the changes

 """ 