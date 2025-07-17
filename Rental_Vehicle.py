def display_booking(name, aadhar, licence, days, vehicle, price):
    print(f"\nVehicle Name      : {vehicle}")
    print(f"Price Per Day     : ₹{price}")
    print(f"Aadhaar Number    : {aadhar}")
    print(f"Licence Number    : {licence}")
    print(f"Days of Booking   : {days} Days")
    total = price * days
    print(f"Total Amount      : ₹{total}")
    confirm = int(input("Confirm Booking?\n1. Yes\n2. No\n> "))
    if confirm == 1:
        print(f"{name}, your booking is confirmed!\nPlease submit your documents and payment at the office.")
    else:
        print(f"Sorry {name}, your booking was not confirmed.")


print("\n\t🚗 Welcome to Rental Vehicle Of Pondicherry 🚗")
print("---------------------------------------------------")

name = input("Enter Your Name: ")
aadhar = input("Enter Your Aadhaar Number: ")
licence = input("Enter Your Licence Number: ")
days = int(input("How many days you want to book the vehicle? "))

if len(aadhar) != 12 or not aadhar.isdigit():
    print("❌ Invalid Aadhaar Number!")
else:
    vehicle_type = int(input("\nChoose Vehicle Type:\n1. 2-Wheeler\n2. 4-Wheeler\n> "))

    if vehicle_type == 1:
        category = int(input("1. Bike\n2. Scooter\n> "))
        if category == 1:
            models = {
                1: ("Royal Enfield", 1800),
                2: ("Himalayan", 2100),
                3: ("Honda Spender Plus", 1400)
            }
        elif category == 2:
            models = {
                1: ("Honda Activa 5G", 1300),
                2: ("Access 125", 1500),
                3: ("N Torque 125", 1700)
            }
        else:
            print("❌ Invalid choice!")
            exit()
    elif vehicle_type == 2:
        models = {
            1: ("Mahindra Thar", 2300),
            2: ("Maruti Jimny", 2500),
            3: ("TATA Nexon", 2000)
        }
    else:
        print("❌ Invalid choice!")
        exit()

    print("\nSelect Model:")
    for key, (model, price) in models.items():
        print(f"{key}. {model} - ₹{price}/day")

    choice = int(input("> "))
    if choice in models:
        model, price = models[choice]
        display_booking(name, aadhar, licence, days, model, price)
    else:
        print("❌ Invalid Model Selection!")

print("\n✅ Be safe and enjoy your journey!")
