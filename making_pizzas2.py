import pizza2

pizza2.make_pizza(16, 'pepperoni')
pizza2.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# this was to show how modules work. the import statement looks for pizza2.py, and sees the function make_pizza.  when you run making_pizzas2 the import statement works behind the scenes and you get the correct output.  similar to import in node?

#
# you can import the whole module with import module_name
#
# you can import just specific functions with:
# from module_name import function_name1, function_name2, etc


# or you can use as to give a function an alias.
# from module_name import function_name as fn
# from pizza2 import make_pizza as mp
#
# mp(16,'pepperoni')
#
# or you can do the alias for the module.
# import module_name as mn
#
# import pizza2 as p
# p.make_pizza(16, 'pepperoni')
#
# and you can tell python to import every function in a module with the *
#
# from pizza2 import *
