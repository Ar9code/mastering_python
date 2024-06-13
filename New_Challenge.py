print("------ Choose Your Role ------")


first_name = input("Enter First Name : ")
last_name = input("Enter Last Name : ")
role = input("Choose Your Role (farmer/adventurer) : ")

if role == "farmer":
    print("You have a seed, an axe, and a hand picker.")
else:
    print("You have a sword, a shield and a bow")