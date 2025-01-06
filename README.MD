# Function:
1. to define a funtion we use - def
2. indentation is important here as we don't use {} for function body
3. to print something we write print()- it's also a function
4. without 'return' if we assign variable to a functon it will hold 'none' value
5. optional parameter: when we give a default parameter in function; default parameter must be in right side  
6. tuple- when with one parameter multiple arguments can be passed on; serves as array (args)
7. kargs- Tuple Parameter in Keyword Arguments; in python it's called dictionary; ('key': value) pair; used **
8. can do for loop in kargs with kargs.items()
9. 'global' keyword only works inside a function

# built in module
Get python built-in module list- https://docs.python.org/3/py-modindex.html 
1. random()
2. randint(x,y) //int range
3. choice() ; pick a random number from given list
4. now() -> optional time zone info in datetime
5. ctime(), date()


Built-in functions- https://docs.python.org/3/library/functions.html

python packages- https://pypi.org/

## pip- official package manager for python
-->It allows you to install, manage, and uninstall Python packages from the Python Package Index (PyPI) or other sources.

--> check version: pip --version


## PyAutoGUI
--> PyAutoGUI is a Python library that allows you to programmatically control the mouse and keyboard to automate tasks on your computer. With PyAutoGUI, you can perform actions like moving the mouse, clicking, typing text, and interacting with the graphical user interface of applications.

--> documentation in: https://pypi.org/project/PyAutoGUI/

--> install: pip install PyAutoGUI

## OpenCV (Open Source Computer Vision)
is a library designed to process images and videos to Perform operations like face detection, object tracking, and optical flow. Develop advanced computer vision and machine learning solutions. 

--> opencv-contrib-python is a Python package that provides bindings for OpenCV. The "contrib" part of the name refers to the extra modules that are included in this package, which are not part of the core OpenCV library.

--> documentation: https://pypi.org/project/opencv-contrib-python/

--> install: pip install opencv-contrib-python

## Exceptions:
--> https://docs.python.org/3/tutorial/errors.html

# list
1. in list (like array) indexing is possible to the reversed way (-1,-2 )
2. alternative of push : append() -> add item at the eand of the list
3. insert(i,x) ->inserting at a particular position
4. remove(x)  -> removing given value.
5. pop() -> removing the last item from the list
6. pop([i])  -> can also add index number
7. clear()  -> removing everything
8.  count()  -> how many items are there on the list
9. reverse()  -> to reverse the array; also possible like list[ : : -1]
10. sort()  -> important one. sort items in the list
11. copy()  -> return a shallow copy of the list


# data structure similar to list- set , tuple
# set
array alike , but where can only store unique values
1. to create set we can use '{}' or 'set()'
2. to add any element in the set we use - add()
3. we cannot add duplicate numbers
4. remove() - to remove any element from the set
5. len() - length of the set
6. sets in Python cannot be accessed using an index number because sets are unordered collections. This means that the elements in a set do not have a specific order or index, unlike lists or tuples.



# tuple
use of '()' only ;(not [] or {}) 
1. tuple is immutable - we cannot change it
2. we can access tuple
3. but if we give mutable vlaue in tuple we can change
4. tuple() - make a tuple from any list

# dictionaries
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

del --> to delete a value from the dictionary

dictionary keys in Python must be immutable. This is a strict rule, and it's essential for ensuring that dictionaries work as intended.

# enumerate
https://docs.python.org/3/library/functions.html#enumerate

enumerate() --> gives the index number of a list, tuple or string in the for loop

# lambda
--> A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression. works like arrow function of javascript

--> lambda functions in Python do not contain explicit return statements. However, they inherently return the result of the single expression they evaluate

--> map(function,interable) 
--> filter(function,interable)

# comprehension
Comprehension in Python is a concise and powerful way to create new sequences like lists, dictionaries, or sets by processing existing iterables. They allow you to write cleaner and more readable code in just one line.

Python provides the following types of comprehensions:

1. List Comprehension ->[expression for item in iterable if condition]
2. Dictionary Comprehension --> {key_expression: value_expression for item in iterable if condition}
3. Set Comprehension  --> {expression for item in iterable if condition}
4. Generator Comprehension  --> (expression for item in iterable if condition)

@@ generator comprehension is not tuple; there is no such thing as a tuple comprehension in Python. If you want to create a tuple, you must explicitly convert the generator expression into a tuple using the tuple() function.

# built-in functions

1. reversed() --> set ,int, float obj cannot be reversed
2. dict() cretes a dictionary
3. any()  returns True if at least one element in the iterable is truthy
4. all() returns True (if all elements are truthy)
5. abs() makes the number positive even if i give negative number
6. sorted() sorts the number; sorted(x, reversed=True)
    for dictionary sorted=(x,key) ;key cannot be string, list

# iter()
The iter() function in Python is used to create an iterator object from an iterable. An iterator is an object that allows you to traverse (or iterate over) all the elements in a collection (like a list, tuple, dictionary, or set) one at a time.
it remembers which value you used last. after getting all values it will show error to 'stop iteration'. so its better to use inside a try-except block

next()->in iter() to travers all the value at time we use next() [avoid list()]; We use next() in Python to manually retrieve the next item from an iterator. It is a built-in function that works with iterators, allowing you to control the iteration process step by step.

# generator ; yield
generator-->  A generator in Python is a special type of iterable that allows you to iterate over a sequence of values without storing the entire sequence in memory. Generators are defined using functions and the yield keyword. 

yield -->  instead of computing all values at once and storing them in memory, it produces them one at a time as you iterate over it.When a function with a yield statement is called, it doesn't execute the function body immediately. Instead, it returns a generator object.

to end a function, returns a generator

yield is not return totally , after giving one value it waits for some time again gives another value

next()--> here we also use the next() to traverse one value at a time; We use next() in Python to manually retrieve the next item from an iterator. It is a built-in function that works with iterators, allowing you to control the iteration process step by step.

# python keywords

https://phitron.io/ph891/video/ph891-5-9-module-summary-and-python-keywords-overivew

1. in / not in
2. pass -> a hold in the function as interpreter not letting me to go forward ; a null statement that will do nothing


# decode('UTF-8')
response=requests.get(api_url)
content=response.content.decode('UTF-8')

--> response.content provides the data in its original byte form.

-->'UTF-8' is a widely used character encoding standard for handling textual data.

# download image from url
use the write of python and write binary ('wb') the response.content