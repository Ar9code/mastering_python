temperature = int(input("Enter Temp: "))

if temperature > 35:
    print("It's Hot")
elif temperature > 30:
    print("It's Almost To Hot For A Normal Day")
elif temperature > 25:
    print("It's A Normal Day")
elif temperature > 20:
    print("It's Almost To Cold For A Normal Day")
else:
    print("It's Cold")