"""
    * we've discussed scope a bit in the past,
        but python's scope rule can sometimes confuse beginners, so let's quickly go ever 
        the key rulse of python's scope.
    
    
    * python scope follows the LEGB rule:
        - L:
            Local:
                names assigned in any way within a function (def or lambda), and
                not declared global in that function.

        - E:
            Enclosing function locals: (EFLs)
                name in the local scop of any and all enclosing function (def or lambda),
                from inner to outer.

        - G:
            Global: (module)
                names assigned at the top-level of a module file, or declared global in a def
                within the file.
        - B:
            Builte-in: (python)
                names preassigned in the built-in names module:
                    open, range, syntaxerror, ...


""" 

x = 25
def my_func():
    x = 50
    return x

print(x) # 25
print(my_func()) # 50

print(my_func())
print(x)




# local
lambda x:x**2


# Enclosing function locals
name = 'this is a global name!'

def greet():
    name = 'Ruhollah'
    def hello():
        return 'hello : {}'.format(name)

    return hello() # built-in

print(greet())



def greet(inOrout = 'out'):
    name = 'Ruhollah'
    def hello():
        global name
        return 'hello : {}'.format(name)
    if inOrout == 'in':
        return 'hello : {}'.format(name)
    return hello()
    
print(greet('out'))



def change():
    global name
    name = 'change global name!'

print('before function call: ',name)
change()
print('after function call: ',name)