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

print("\n")

# positional arguments looks at order of arguments
def describe_pet(pet_name, animal_type = 'dog'):
    print("\nI have a "+ animal_type+".")
    print("My "+animal_type+"'s name is "+ pet_name.title()+".")
# describe_pet("llama", "lloyd")
# describe_pet("dog", "chester")

# keyword argument
# note the order of parameters had to be changed
describe_pet(pet_name = 'willie')


describe_pet(pet_name='harry', animal_type="bird")


print("\n")
def make_shirt(shirt_size, shirt_text):
    print("The shirt size is "+shirt_size+" and the text on the shirt will read: " + shirt_text)

make_shirt("small", "math is big time")
