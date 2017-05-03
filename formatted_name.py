def get_formatted_name(first_name, last_name):
    """return full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


musician2 = get_formatted_name('aaaa', 'bbbb')
print(musician2)
