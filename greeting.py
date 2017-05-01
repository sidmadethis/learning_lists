# def greet_user():
#     """Display a simple greeting"""
#     print("Hello")
#
# greet_user()


# the triple quote is a docstring, used for documentation by python

def greet_user(username):
    """display a simple greeting"""
    print("Hello, " + username.title()+"!")

greet_user('jesse')


# username is the parameter, jesse is the argument

def favorite_book(bookname):
    print("One of my favorite books is "+ bookname.title())

favorite_book("Alice in Wonderland")
