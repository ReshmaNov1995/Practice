# Approach - 1:
import Animal
import Bird

Animal.fly()
Animal.color()

Bird.fly()
Bird.color()

# Approach - 2:

from Module_Package import Animal
from Module_Package import Bird

Animal.fly()
Animal.color()

Bird.fly()
Bird.color()

# In the above case the latest statement "from Bird import *" only considered not the existing statement "from Bird import *"

# from Animal import *
# fly()
# color()
#
# from Bird import *
# fly()
# color()