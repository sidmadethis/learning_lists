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

# age = 17
# if age >= 18:
#     print("You are old enough to vote")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry not yet old enough to vote")


age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your age is " + str(age) + " so your admission price is $" + str(price) + ".")
