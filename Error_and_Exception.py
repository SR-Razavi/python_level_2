"""
    * often times our code isn't perfect, meaning we are run into errors!
    * but how we do actually set-up our own erroe and exception calls?
    * let;s find out.

    * we can use these keywords:
        - try
        - except
        - finally
        
        * to dictate por code logic in case of an error.

    * to show how this keyword we will be opening files, one weay to open files 
        is to use the open() finction: 
        -open("myfile.txt", 'r')
    * the second parameter in the open() function dictates whether you are opening
        the file for just reading, just writhing, or to do both.
    * if you use the wrong one, you may get an error!

    * let's use this to show how we can handle errors!

    * structure
        try:
            you do your operation here...
            ...
        except exceptionI:
            if there exceptionI, then execute this block.
        except exceptionII:
            if there exceptionII, then execute this block.
            ...
        else:
            if there is no exception then execute this block.
"""


# whrite in simple.txt file without exception 
try:
    f = open('simple.txt' , 'w')
    f.write("test write to simple text!")
except IOError:
    print('error: could not find file or read data!')
else:
    print('success!')
    f.close()