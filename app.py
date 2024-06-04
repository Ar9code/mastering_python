name = input("What is your name? ")
print("Hello " + name)

birth_year = input("Enter your birth year: ")
age = 2023 - int(birth_year)
print(age)

first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
print("Sum: " + str(sum))

course = 'Python for Beginners'
print('Python' in course)

temperature = 35

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: # (20, 30]
    print("It's a nice day")
elif temperature > 10: # (10, 20]
    print("It's a bit cold")
else:
    print("It's cold")

weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

i = 1
while i <= 5:
    print(i)
    i = i + 1