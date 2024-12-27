try:
  num=45/0
  print(num)
except:  # we used 'catch' in java, c++, c#, javaScript
  print('something went wrong')
finally:
  print('math is done')

# else- when no exception occurs in the try block

def display(**kwargs):
    for i in kwargs:
        print(i, end='')