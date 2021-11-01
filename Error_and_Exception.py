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
# try:
#     f = open('simple.txt' , 'w')
#     f.write("test write to simple text!")
# except IOError:
#     print('error: could not find file or read data!')
# else:
#     print('success!')
#     f.close()


# exception is true becouse we can just read 
# try:
#     f = open('simple.txt' , 'r')
#     f.write("test write to simple text!")
# except IOError:
#     print('error: could not find file or read data!')
# else:
#     print('success!')
#     f.close()


# If we managed the exception, the program would continue to run 
# f = open('simple.txt' , 'r')
# f.write("test write to simple text!")
# print('hello world')



# exception not unconditionally fatal having your code being able to handle these sort of unexpected
# that's really the whole point of this
# if you expect something wrong may occur
# or you have a certain condition that may actually mess up you code
# you can counter it with an except clause
# now another thing you may be wondering is well have am i supposed to know what error is going to happen
# i can't have all these error codes memorized.
# you know the basic one like syntax error or name error but you may not how known.
# i know there are other errors where you can do is you actually don't need to give any error code 
# if you just have a general except here it is going to print on any sort of air
# so you don't actually need to specify the specific error.
# so a lot of times you're going to be writing except they're ok
# try:
#     f = open('simple.txt' , 'r')
#     f.write("test write to simple text!")
# except:
#     print('error: could not find file or read data!')
# else:
#     print('success!')
#     f.close()



# so now let's introduce the finally keyword and the finally key block of code, 
# will always be run regardless if there is an exception in the try code block.
try:
    f = open('simple.txt' , 'r')
    f.write("test write to simple text!")
except:
    print('error: could not find file or read data!')
finally:
    print('i alwayes work no matter what!')