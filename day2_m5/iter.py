# if we want to get any value from list or set or tuple we can get  b indexing; but sometimes we want to get value one by one- doing iteration

# iter()

numbers=[12,45,68,56,45,12,30]
numbers_iter=iter(numbers)

# after making iteration if we use next() it will give one value, list() will make the same previous one
print(next(numbers_iter))   #12
print(next(numbers_iter))   #45
print(next(numbers_iter))   #68
print(next(numbers_iter))   #56

# it remembers which value you used last. after getting all values it will show error to 'stop iteration'
print(next(numbers_iter))   #45
print(next(numbers_iter))   #12
print(next(numbers_iter))   #30
#print(next(numbers_iter))   #error

# so its better to use inside a try catch with a loop

try:
    number=[12,45,68,56,45,12,30]
    numbers_iter=iter(numbers)

    print("inside try block")
    print(next(numbers_iter))   #12
    print(next(numbers_iter))   #45
    print(next(numbers_iter))   #68
    print(next(numbers_iter))   #56
    print(next(numbers_iter))   #45
    print(next(numbers_iter))   #12
    print(next(numbers_iter))   #30
    print(next(numbers_iter))   #error
except StopIteration:
  print(" iteration stopped")