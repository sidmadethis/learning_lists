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

for name,language in favorite_languages.items():
    print(name.title()+ "'s favorite language is " + language.title() + ".")
