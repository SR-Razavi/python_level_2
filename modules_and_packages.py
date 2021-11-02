"""
    * Module and Package.
    * you have seen puthon import statments, but have probably wondered, how do they work
        and how do we create our own?
    
    * in this lecture you learn how can create you'r own module and then import it into another file.
"""
# built in module
# and basiclly what happens is when you run a program in python? the interpreter compiles it to byte code first.
# and that's kind of an oversimplification but essentially it is stores that in the pie cache folder.
import my_nodule

# use the built in module
my_nodule.func_in_module()


# it is another wey to call it
import my_nodule as mm

mm.func_in_module()

# it is another wey to call it
from my_nodule import func_in_module

# you don't need prifixing
func_in_module()

# this will import everything from my_module
from my_nodule import *

func_in_module()