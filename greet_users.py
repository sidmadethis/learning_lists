def greet_users(names):
    """print a simple greeting to each user in the list"""
    for name in names:
        msg= "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#
# if you wanted a copy of a list (as to keep the original intact) you could use function_name(list_name[:])
# the slice notation makes a [:] copy of the list
