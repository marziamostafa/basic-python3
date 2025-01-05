numbers=[12,45,68,56,45,12,30]

def get_numbers(nums):
    for num in nums:
        #return num # returning only 12
        yield num

result=get_numbers(numbers)
print(next(result))
print(next(result))
print(next(result))
print('Exploring generator')
print(next(result))