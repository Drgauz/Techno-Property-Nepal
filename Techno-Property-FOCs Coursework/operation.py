import datetime
from write import billRenting, update_land_status, ReturnBill

def rent_land(lands, Kitta_no, Name, Phone_no, rentingPeriod, RentingDict): # This function carries out renting process 
    rented_land = None
    total_cost = 0
    for land in lands:
        kitta, location, direction, annas, cost, status = land
        if status.replace(" ","").lower() == "available" and kitta.replace(" ","") == Kitta_no.replace(" ",""):
            land_cost = int(cost) * rentingPeriod # calculate the renting cost of land
            total_cost += land_cost  # calculate the total renting cost of land
            billRenting(Name, Phone_no, land, rentingPeriod)
            update_land_status('lands.txt', kitta, 'Not Available') # Updates the status of rented land into Not Available
            
            # Store customer rental information in the dictionary
            RentingDict[kitta] = {
                "Purchaser's name": Name,
                "Purchaser's phone": Phone_no,
                "Purchaser's rented_duration": rentingPeriod,
                "Purchaser's rented_date": datetime.date.today()
            }
            rented_land = land
            break
    
    if rented_land:
        print("Land "+ Kitta_no+"  rented successfully. Total cost: NPR "+str(total_cost)) #display the message when land rented successfully.
        print("Customer information has been recorded.")
    else:
        print("Land with kitta "+ Kitta_no+" is not available for rent.") #display message when tried to rent rented land or entered invalid kitta number.

def return_land(lands, kitta, name, phone, real_rentingPeriod, RentingDict): # This function carries out returning process 
    returned_land = 0
    for land in lands:
        if land[0].replace(" ", "") == kitta.replace(" ", ""):
            returned_land = land
            break
    
    if returned_land ==0 :
        print("Land with kitta "+kitta+" not found.")
        return

    if returned_land[5].replace(" ", "").lower() == "available":
        print("Land with kitta "+kitta+" is not currently rented.")
        return

    # Retrieve customer information from the dictionary
    rental_info = RentingDict.get(kitta)
    if rental_info:
        renter_name = rental_info["Purchaser's name"]
        renter_phone = rental_info["Purchaser's phone"]
        expected_duration = rental_info["Purchaser's rented_duration"]
        rental_date = rental_info["Purchaser's rented_date"]
        
        # Check if the person returning is the same as the renter
        if name != renter_name or phone != renter_phone:
            print("The provided name and phone number do not match the rental records.")
            return 
    else:
        print("No rental information found for land with kitta "+kitta+".")
        return

    # Calculate fine if returned late
    fine = 0
    if real_rentingPeriod > expected_duration:
        months_late = real_rentingPeriod - expected_duration
        fine = int(returned_land[4]) * months_late * 0.1  # 10% fine per month when returned late

    ReturnBill(renter_name, renter_phone, kitta, rental_date, real_rentingPeriod, expected_duration, land, returned_land, fine)

    # Update land status to availabe after land has been returned
    update_land_status('lands.txt', kitta, 'Available')

    # Calculate total cost
    total_cost = int(returned_land[4]) * real_rentingPeriod + fine

    # Print return bill
    print("\n")
    print("\t\t\t\t Techno Property Nepal")
    print("\t\t\t\t New Baneshwor, Kathmandu, | Contact no. : 9793104925")
    print("\n")
    print("Return Invoice Date: "+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print("\n")
    print("Customer Name: "+renter_name)
    print("Phone Number: "+renter_phone)
    print("\n")
    print("Land Details:")
    print("Kitta Number: "+returned_land[0])
    print("Location: "+returned_land[1])
    print("Direction: "+returned_land[2])
    print("Area: "+returned_land[3]+" annas")
    print("Monthly Rent: NPR "+str(returned_land[4]))
    print("\n")
    print("Rental Date: "+str(rental_date))
    print("Expected Rental Duration: "+str(expected_duration)+" months")
    print("Actual Rental Duration: "+str(real_rentingPeriod)+" months")
    print("Rental Cost: NPR "+str(int(returned_land[4]) * real_rentingPeriod))
    print("Late Return Fine: NPR "+str(fine))
    print("Total Cost: NPR "+str(total_cost))
    print("\nReturn Date: "+str(datetime.datetime.now().date()))
    print("\n")
    print("    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    print("Land "+kitta+" has been returned successfully.")
    print("Thank you for using Techno Property Nepal's rental service.")
    print("Have a nice day! :)")
    print("\n")
    print("\t Enter 1 to Rent the Land")
    print("\t Enter 2 to Return the Land")
    print("\t Enter 3 to Exit from system")
    print("\n")
    print("    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    # Remove the rental information from the dictionary
    del RentingDict[kitta]

    
