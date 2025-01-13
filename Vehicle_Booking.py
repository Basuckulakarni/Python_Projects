snNo = 0

def displayVehicle(name,model,price):
    print("-------------------------------------------")
    day = int(input("Enter how long you want to rent\n"))
    total = price * day
    print("*Vehicle Details*")
    print("Name :",name,"\nModel :",model,"\nPrice\\day :",price,"\nDay :",day,"\nTotal :",total)
    return name,model,price

def confirmBooking(name,model,price):
    print("-------------------------------------------")
    confirmChoice = int(input("Confirm Your Booking\n1.Processed\n2.Cancel\n"))
    if confirmChoice == 1:
        Name = input("Enter Your Name\n")
        ph_Number = input("Enter Your Number\n")
        Aadhaar = input("Enter Your Aadhar Number\n")
        return fileWrite(name, model, price, Name, ph_Number, Aadhaar)
    #     if len(ph_Number) == 10 and len(Aadhaar) == 12:
    #         return fileWrite(name,model,price,Name,ph_Number,Aadhaar)
    #
    # else:
    #     print("Thank You Visit Again")
    #     print("-------------------------------------------\nFill Details Of User\n______________________________")

def fileWrite(name,model,price,Name,ph_Number,Adhaar):
    global snNo
    f = open("Rental_Vehicle.txt","a+")
    if f.tell() == 0:
        f.write(
            f"{'Sn No'.ljust(10)}{'Vehicle Name'.ljust(20)}{'Model'.ljust(10)}{'Price/day'.ljust(15)}"
            f"{'Customer Name'.ljust(20)}{'Phone Number'.ljust(15)}{'Aadhaar Number'.ljust(15)}\n"
        )
        snNo+=1
    f.write(
        f"{str(snNo).ljust(10)}{name.ljust(20)}{str(model).ljust(15)}{str(price).ljust(10)}"
        f"{Name.ljust(20)}{ph_Number.ljust(15)}{Adhaar.ljust(15)}\n"
    )
    print("*Your Booking Is Confirmed*\nPlease Submit Your Documents Once reach Office\n*Thank you Visit Again*")
def fileRead():
    global snNo
    f = open("Rental_Vehicle.txt","r")
    lines=f.readlines()
    snNo=len(lines)
    return snNo

fileRead()
print("\t\tWel Come Rental Vehicle Booking")
print("1.Bikes\n2.Cars")
choice = int(input())
print("-------------------------------------------")
if choice == 1:
    print("1.Royal Enfield\n2.Activa 6g\n3.Himalayan")
    choice = int(input())
    if choice == 1:
       name,model,price = displayVehicle("Royal Enfield",2013,1500)
       confirmBooking(name,model,price)
    elif choice == 2:
        name,model,price =displayVehicle("Activa 6g", 2017, 800)
        confirmBooking(name, model, price)
    elif choice == 3:
        name,model,price = displayVehicle("Himalayan", 2020, 1250)
        confirmBooking(name, model, price)
    else:
        print("Enter Valid Inputs")
elif choice == 2:
    print("1.Thar\n2.Scorpio\n3.Bolero")
    choice = int(input())
    if choice == 1:
        name,model,price =displayVehicle("Thar 4*4", 2015, 3500)
        confirmBooking(name, model, price)
    elif choice == 2:
        name,model,price =displayVehicle("Scorpio", 2017, 3000)
        confirmBooking(name, model, price)
    elif choice == 3:
        name,model,price =displayVehicle("Bolero", 2020, 2600)
        confirmBooking(name, model, price)
    else:
        print("Enter Valid Inputs")
else:
    print("Enter Valid Input")
