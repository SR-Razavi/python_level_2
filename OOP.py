"""
    OOP

    * object oriented programing is a way to use python to create our own objects.
    * it can be a point of great confusion for beginners, mainly because often it is taught poorly

    * let's try our best to save you from any confusion by systimaticlly showing you the thought
        process behind OOP and why we would need it.

    * we will use it quite a bit for django, so let's get started
"""

# everything in python is class


print(type(12))

print(type(12.3))

print(type("scscds"))

print(type([1,2,3,5]))


print('---------------')


class MyClass():
    pass
x = MyClass()

print(x)


print('---------------')


# The self Parameter

# * The self parameter is a reference to the current instance of the class,
#       and is used to access variables that belongs to the class.

# * It does not have to be named self , you can call it whatever you like,
#       but it has to be the first parameter of any function in the class

# __init__ isconstructor

class Dog():

    # class object attribute
    specise = 'mammal'

    def __init__(self , breed, name):

        self.name = name
        self.breed = breed

mydog = Dog('Lab', 'Sammy')

print(mydog.breed)
print(mydog.name)
print(mydog.specise)


print('---------------')


class Circle():
    pi = 3.14
    def __init__(self, reduce) -> None:
        self.reduce = reduce

    def area(self):
        return self.reduce * self.reduce * Circle.pi

    def set_reduce(self, new_r):
        self.pi = new_r

myc = Circle(4)
myc.set_reduce(99)
print(myc.area())


print('---------------')


class Animal():
    def __init__(self) -> None:
        print('Animal created')

    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating')

myanimal = Animal()
myanimal.whoAmI()
myanimal.eat()


print('---------------')

# inheritance
class Dog(Animal):
    def __init__(self) -> None:
        # Animal.__init__(self)
        print("Dog created")

    def bark(self):
        print('woof')

    # method over writhing
    def eat(self):
        print("Dog eating")

mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()


print('---------------')


# special methods
class Book():
    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return 'title: {}, author: {}, pajes: {}'.format(self.title, self.author, self.pages)

    def __len__(self):
        return len(self.author)

    def __del__(self):
        print('a book is destroyed!')

book = Book('python', 'ruhollah', 100)
print(book)
print(len(book))
del book

