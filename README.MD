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
Get python built-in module list- https://docs.python.org/3/py-modindex.html 

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

# tuple
use of '()' only ;(not [] or {}) 
1. tuple is immutable - we cannot change it
2. we can access tuple
3. but if we give mutable vlaue in tuple we can change
4. tuple() - make a tuple from any list

# dictionaries
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# enumerate
https://docs.python.org/3/library/functions.html#enumerate

enumerate() --> gives the index number of a list in for loop

# lambda
--> A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

--> map(function,interable) 
--> filter(function,interable)