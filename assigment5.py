# 1-2
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car != 'ford'? I predict True.")
print(car != 'ford')

print("\nIs car == 'Subaru'.lower()? I predict True.")
print(car == 'Subaru'.lower())

print("\nIs car == 'SUBARU'.lower()? I predict True.")
print(car == 'SUBARU'.lower())

print("\nIs 10 > 5? I predict True.")
print(10 > 5)

print("\nIs 5 < 2? I predict False.")
print(5 < 2)

print("\nIs 8 >= 8? I predict True.")
print(8 >= 8)

print("\nIs 7 <= 6? I predict False.")
print(7 <= 6)

# 3
alien_color = 'green'
if alien_color == 'green':
    print("Player earned 5 points!")

alien_color = 'red'
if alien_color == 'green':  # X
    print("Player earned 5 points!")

# 4
alien_color = 'green'
if alien_color == 'green':
    print("Player earned 5 points for shooting the alien!")
else:
    print("Player earned 10 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("Player earned 5 points!")
else:
    print("Player earned 10 points!")

# 5
alien_color = 'red'
if alien_color == 'green':
    print("Player earned 5 points!")
elif alien_color == 'yellow':
    print("Player earned 10 points!")
elif alien_color == 'red':
    print("Player earned 15 points!")

# 6
age = 25
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

# 7
favorite_fruits = ['banana', 'apple', 'grape']
if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'grape' in favorite_fruits:
    print("You really like grapes!")
if 'mango' in favorite_fruits:
    print("You really like mangoes!")
if 'orange' in favorite_fruits:
    print("You really like oranges!")

# 8
usernames = ['admin', 'jon', 'salo', 'nika', 'mari']
for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

# 9
usernames = []
if not usernames:
    print("We need to find some users!")

# 10
current_users = ['Jon', 'Salo', 'Nika', 'Mari', 'Giorgi']
new_users = ['giorgi', 'Misha', 'Jon', 'Andro', 'Salo']
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user} is already taken. Please enter a new username.")
    else:
        print(f"{new_user} is available.")

# 11
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
