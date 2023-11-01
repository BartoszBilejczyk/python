# python day-2.py

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# calculate BMI

bmi = int(weight) / float(height) ** 2

print(round(bmi, 2))

if (bmi < 18.5):
        print("underweight")
elif (bmi > 25):
        print("overweight")
elif (bmi > 30):
        print("obese")
else:
        print("normal weight")

score = 12
height = 1.9
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

age = input("What is your current age?")

years_left = 90 - int(age)
weeks_left = years_left * 52
days_left = weeks_left * 7
hours_left = days_left * 24

print(f"You have {years_left} years, {weeks_left} weeks, and {days_left} days left and {hours_left} hours left.")

print("Welcome to the tip calculator.")

total_bill = float(input('What was the total bill? $'))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))
tip = total_bill * (tip_percentage / 100)
total_bill += tip

print('Each person should pay $' + str(round(total_bill / people, 2)))
