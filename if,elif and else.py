age = int(input("Enter your age: "))

if age < 18:
    print("You are not old enough to vote.")
elif age >= 18 and age < 65:
    print("You are eligible to vote.")
else:
    print("You are too old to vote.")
