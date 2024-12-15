# way 1
import function
function.add(5,6)

# way 2
from function import add,multiply

add(10,2)
res=multiply(2,2)
print(res)

# way 3

from function import *   # * means everything

sub(10,2)