# python day-3.py

print("Welcome to the rollercoaster.")

height = int(input("What is your height in cm? "))

if height > 120:
        age = int(input("What is your age? "))
        if age < 12:
                print('pay 4 dollars')
        elif age < 18:
                print('pay 7 dollars')
        else:
                print('pay 12 dollars')
else:
        print('Sorry, you have to grow taller before you can ride.')

print("Welcome to our pizzeria!")
size = str.lower(input("What size pizza do you want? S, M, or L "))
add_pepperoni = str.lower(input("Do you want pepperoni? Y or N "))
extra_cheese = str.lower(input("Do you want extra cheese? Y or N "))
total = 0

# print all the options
print(f"{size}, {add_pepperoni}, {extra_cheese}")

if size == 's':
        total += 15
elif size == 'm':
        total += 20
elif size == 'l':
        total += 25

if add_pepperoni == 'y' and size == 's':
        total += 2
else:
        total += 3

if extra_cheese == 'y':
        total += 1

print(f"Your final bill is ${total}.")
