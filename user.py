user_0= {
'username':'efermi',
'first':'enrico',
'last':'fermi',
}

for key,value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
# key value on line 7 can be replaced with k v, just variables


favorite_languages = {
    'jen': 'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print("\n")
for name,language in favorite_languages.items():
    print(name.title()+ "'s favorite language is " + language.title() + ".")


print("\n")
for name in favorite_languages.keys():
    print(name.title())

# this is the same as for name in favorite_languages:

# use sort to get dictionary in order
# note this does alphabetical sorting
print("\n")
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking our poll!")


print("\n")
print("the following langauges have been mentioned")
for language in favorite_languages.values():
    print(language.title())

# use set to not have duplicates
print("\nNo duplicates")
for language in set(favorite_languages.values()):
    print(language)


# nesting is storing dictionaries inside of a dictionary
alien_a = {'color':'green', 'points':5}
alien_b = {'color':'blue', 'points':52}
alien_c = {'color':'white', 'points':15}

print("\n")
aliens = [alien_a, alien_b, alien_c]
print(aliens)
