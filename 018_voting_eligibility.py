age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")

if age >= 18 and nationality == "nigerian":
        print("You are eligible to vote in Nigeria.")

elif age < 18 and nationality == "nigerian":
        print("You are too young to vote.")

else:
        print("You must be a Nigerian citizen to vote here.")
