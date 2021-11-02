

def new_decorator(func):

    def wrap_func():
        print("code here befor executing func")
        func()
        print('func() has been called')
    return wrap_func


@new_decorator
def func_needs_decorator():
    print('this function is in need of a decorator!')


# new_decorator(func_needs_decorator)()

# print('------------------------------ b')

# func_needs_decorator = new_decorator(func_needs_decorator)
# func_needs_decorator()


# print('------------------------------ e')



# func_needs_decorator = new_decorator(func_needs_decorator)
# func_needs_decorator()

# print('------------------------------ b')

# new_decorator(func_needs_decorator)()



