try:
  num=45/0
  print(num)
except:  # we used 'catch' in java, c++, c#, javaScript
  print('something went wrong')
finally:
  print('math is done')