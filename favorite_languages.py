favorite_languages = {
    'jen':['python','ruby'],
    'sarah':'c',
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title()+ "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

# you can get too many layers and get complicated

users = {
    'aeinstein': {
        'first': 'Albert',
        'last': 'Einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'Curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: "+full_name.title())
    print("\tLocation: "+location.title())
