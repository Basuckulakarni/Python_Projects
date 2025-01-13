print("\t\t\tWel Come \n\tRental Vehicle Of Pondicherry!!")
print("----------------------------------------------")
print("Enter Your Name")
name = input()
print("Enter Your Aadhaar Number")
user_aadhar = int(input())
aadhar = str(user_aadhar)
print("Enter Your Licence Number")
licence_no = input()
print("How much day you want")
days = int(input())
vehicle_choice = int(input("Which Vehicle you want\n1.2 Wheeler\n2.4 Wheeler\n"))
if vehicle_choice == 1:
    if len(aadhar) <= 12:
        print("1.Bike\n2.Scooter")
        type_choice = int(input())
        if type_choice == 1:
            print("1.Royal Enfield\n2.Himalayan\n3.Honda Spender Plus")
            model_choice = int(input())
            if model_choice == 1:
                print("Bike Name : Royal Enfield")
                print("Price :1800")
                print("Aadhaar Number :",aadhar)
                print("Licence Number :",licence_no)
                print("Days of Booking :",days,"Days")
                print("Total Amount : ₹",1800*days)
                print("Confirm Your Book press\n1.Yes\n2.No")
                confirm_choice = int(input())
                if confirm_choice == 1:
                    print(name,"Your Booking is Confirmed!!\nSummit your Document and Amount once you Visit Office!!")
                elif confirm_choice == 2:
                    print("Sorry",name,"!! Your Booking is Not Confirmed")
                else:
                    print("Invalid Choice!!")
            elif model_choice == 2:
                print("Bike Name : Himalayan")
                print("Price :2100")
                print("Aadhaar Number :",aadhar)
                print("Licence Number :",licence_no)
                print("Days of Booking :", days, "Days")
                print("Total Amount : ₹",2100*days)
                print("Confirm Your Book press\n1.Yes\n2.No")
                confirm_choice = int(input())
                if confirm_choice == 1:
                    print(name, "Your Booking is Confirmed!!\nSummit your Document and Amount once you Visit Office!!")
                elif confirm_choice == 2:
                    print("Sorry", name, "!! Your Booking is Not Confirmed")
                else:
                    print("Invalid Choice!!")
            elif model_choice == 3:
                print("Bike Name : Spender Plus")
                print("Price :1400")
                print("Aadhaar Number :",aadhar)
                print("Licence Number :",licence_no)
                print("Days of Booking :", days, "Days")
                print("Total Amount : ₹",1400*days)
                print("Confirm Your Book press\n1.Yes\n2.No")
                confirm_choice = int(input())
                if confirm_choice == 1:
                    print(name, "Your Booking is Confirmed!!\nSummit your Document and Amount once you Visit Office!!")
                elif confirm_choice == 2:
                    print("Sorry", name, "!! Your Booking is Not Confirmed")
                else:
                    print("Invalid Choice!!")
            else:
                print("Invalid choice!!")
        elif type_choice == 2:
            print("1.Honda Active 5G\n2.Access 125\n3.N Torque 125")
            model_choice = int(input())
            if model_choice == 1:
                print("Bike Name : Honda Active 5G")
                print("Price :1300")
                print("Aadhaar Number :", aadhar)
                print("Licence Number :", licence_no)
                print("Days of Booking :", days, "Days")
                print("Total Amount : ₹", 1300 * days)
                print("Confirm Your Book press\n1.Yes\n2.No")
                confirm_choice = int(input())
                if confirm_choice == 1:
                    print(name, "Your Booking is Confirmed!!\nSummit your Document and Amount once you Visit Office!!")
                elif confirm_choice == 2:
                    print("Sorry", name, "!! Your Booking is Not Confirmed")
                else:
                    print("Invalid Choice!!")
            elif model_choice == 2:
                print("Bike Name : Access 125")
                print("Price :1500")
                print("Aadhaar Number :", aadhar)
                print("Licence Number :", licence_no)
                print("Days of Booking :", days, "Days")
                print("Total Amount : ₹", 1500 * days)
                print("Confirm Your Book press\n1.Yes\n2.No")
                confirm_choice = int(input())
                if confirm_choice == 1:
                    print(name, "Your Booking is Confirmed!!\nSummit your Document and Amount once you Visit Office!!")
                elif confirm_choice == 2:
                    print("Sorry", name, "!! Your Booking is Not Confirmed")
                else:
                    print("Invalid Choice!!")
            elif model_choice == 3:
                print("Bike Name : N Torque 125")
                print("Price :1700")
                print("Aadhaar Number :", aadhar)
                print("Licence Number :", licence_no)
                print("Days of Booking :", days, "Days")
                print("Total Amount : ₹", 1700 * days)
                print("Confirm Your Book press\n1.Yes\n2.No")
                confirm_choice = int(input())
                if confirm_choice == 1:
                    print(name, "Your Booking is Confirmed!!\nSummit your Document and Amount once you Visit Office!!")
                elif confirm_choice == 2:
                    print("Sorry", name, "!! Your Booking is Not Confirmed")
                else:
                    print("Invalid Choice!!")
            else:
                print("Invalid Choice!!")
        else:
            print("Invalid Choice!!")
    else:
        print("Aadhaar Number Not Valid!!")
elif vehicle_choice ==2:
    if len(aadhar) <= 12:
        print("1.Mahindra Thar\n2.Maruti Jimny\n3.TATA Nexon")
        model_choice = int(input())
        if model_choice == 1:
            print("Bike Name : Mahindra Thar")
            print("Price :2300")
            print("Aadhaar Number :", aadhar)
            print("Licence Number :", licence_no)
            print("Days of Booking :", days, "Days")
            print("Total Amount : ₹", 2300 * days)
            print("Confirm Your Book press\n1.Yes\n2.No")
            confirm_choice = int(input())
            if confirm_choice == 1:
                print(name, "Your Booking is Confirmed!!\nSummit your Document and Amount once you Visit Office!!")
            elif confirm_choice == 2:
                print("Sorry", name, "!! Your Booking is Not Confirmed")
            else:
                print("Invalid Choice!!")
        elif model_choice == 2:
            print("Bike Name : Maruti Jimny")
            print("Price :2500")
            print("Aadhaar Number :", aadhar)
            print("Licence Number :", licence_no)
            print("Days of Booking :", days, "Days")
            print("Total Amount : ₹", 2500 * days)
            print("Confirm Your Book press\n1.Yes\n2.No")
            confirm_choice = int(input())
            if confirm_choice == 1:
                print(name, "Your Booking is Confirmed!!\nSummit your Document and Amount once you Visit Office!!")
            elif confirm_choice == 2:
                print("Sorry", name, "!! Your Booking is Not Confirmed")
            else:
                print("Invalid Choice!!")
        elif model_choice == 3:
            print("Bike Name : TATA Nexon")
            print("Price :2000")
            print("Aadhaar Number :", aadhar)
            print("Licence Number :", licence_no)
            print("Days of Booking :", days, "Days")
            print("Total Amount : ₹", 2000 * days)
            print("Confirm Your Book press\n1.Yes\n2.No")
            confirm_choice = int(input())
            if confirm_choice == 1:
                print(name, "Your Booking is Confirmed!!\nSummit your Document and Amount once you Visit Office!!")
            elif confirm_choice == 2:
                print("Sorry", name, "!! Your Booking is Not Confirmed")
            else:
                print("Invalid Choice!!")
        else:
            print("Invalid Choice!!")
    else:
        print("Invalid Aadhaar Number!")
else:
    print("Invalid Choice!!")
print("Be safe and Enjoy Your Journey!!")