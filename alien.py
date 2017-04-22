# alien_0 = {'color':'green','points':5}
#
# print(alien_0['color'])
# print(alien_0['points'])
#
#
# new_points = alien_0['points']
# print("you just earned "+str(new_points)+ " points!")
#
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)
#
#
# person1 = {
#     'name': 'paul',
#     'aage': 63,
#     'city': 'severna park',
# }
# print(person1)


# make empty list for storing aliens
aliens=[]

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

# show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created
print("total number of aliens: " + str(len(aliens)))
