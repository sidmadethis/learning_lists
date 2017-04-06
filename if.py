cars = ['audi', 'bmw', 'toyota', 'subaru']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title()+", you can post a response")
