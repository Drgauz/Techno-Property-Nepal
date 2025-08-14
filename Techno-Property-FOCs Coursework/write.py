
import datetime

def billRenting(Name, Phone_no, land, rentingPeriod):# This function carries out billing for rent process 
    kitta, location, direction, annas, cost, status = land
    total_cost = int(cost) * rentingPeriod
    filename = "rent_invoice_" + Name + "_" + kitta + "_" + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".txt"
    
    file = open(filename, "w")
    file.write("\t\t\t\t Techno Property Nepal\n")
    file.write("\t\t\t\t New Baneshwor, Kathmandu, | Contact no. : 9793104925\n\n")
    file.write("Renting Date: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n\n")
    file.write("Purchaser's Name: " + Name + "\n")
    file.write("Purchaser's Phone Number: " + Phone_no + "\n\n")
    file.write("Land Details:\n")
    file.write("Kitta Number: " + kitta + "\n")
    file.write("Location: " + location + "\n")
    file.write("Direction: " + direction + "\n")
    file.write("Area: " + annas + " annas\n")
    file.write("Monthly Rent: NPR " + str(cost) + "\n\n")
    file.write("Rental Duration: " + str(rentingPeriod) + " months\n")
    file.write("Total Cost: NPR " + str(total_cost) + "\n")
    file.write("\nRental Start Date: " + str(datetime.date.today()) + "\n")
    file.close()
    
    print("Rent invoice generated: " + filename) #prints the rent bill .txt file

    # print rent bill
    print("\n")
    print("\t\t\t\t Techno Property Nepal")
    print("\t\t\t\t New Baneshwor, Kathmandu, | Contact no. : 9793104925")
    print("\n")
    print("Renting Date: "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("\n")
    print("Purchaser's Name: "+Name)
    print("Purchaser'sPhone Number: "+Phone_no)
    print("\n")
    print("Land Details:")
    print("Kitta Number: "+kitta)
    print("Location: "+location)
    print("Direction: "+direction)
    print("Area: "+annas+" annas")
    print("Monthly Rent: NPR "+str(cost))
    print("\n")
    print("Rental Duration: "+str(rentingPeriod)+" months")
    print("Total Cost: NPR "+str(total_cost))
    print("\nRental Start Date: "+str(datetime.date.today()))
    print("\n")
    print("    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t Enter 1 to Rent the Land")
    print("\t Enter 2 to Return the Land")
    print("\t Enter 3 to Exit from system")
    print("\n")
    print("    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

def ReturnBill(renter_name, renter_phone, kitta, rental_date, real_rentingPeriod, expected_duration, land, returned_land, fine): #This function carries out billing for return process in .txt file
    kitta, location, direction, annas, cost,status = land
    total_cost = int(returned_land[4]) * real_rentingPeriod + fine

    filename = "return_invoice_" + renter_name + "_" + kitta + "_" + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".txt"
    
    file = open(filename, "w")
    file.write("\t\t\t\t Techno Property Nepal\n")
    file.write("\t\t\t\t New Baneshwor, Kathmandu, | Contact no. : 9793104925\n\n")
    file.write("Rented Date: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n\n")
    file.write("Purchaser's Name: " + renter_name + "\n")
    file.write("Purchaser's Phone Number: " + renter_phone + "\n\n")
    file.write("Land Details:\n")
    file.write("Kitta Number: " + kitta + "\n")
    file.write("Location: " + location + "\n")
    file.write("Direction: " + direction + "\n")
    file.write("Area: " + annas + " annas\n")
    file.write("Monthly Rent: NPR " + str(returned_land[4]) + "\n\n")
    file.write("Rental Date: " + str(rental_date) + " months\n")
    file.write("Expected Rental Duration: " + str(expected_duration) + " months\n")
    file.write("Actual Rental Duration: " + str(real_rentingPeriod) + " months\n")
    file.write("Rental Cost: NPR " + str(int(returned_land[4]) * real_rentingPeriod)+ "\n")
    file.write("Late Return Fine : NPR " + str(fine) + "\n")
    file.write("Total Cost : NPR " + str(total_cost) + "\n")
    file.close()

    print("Return invoice generated: " + filename)
    
#function for updating the land status
def update_land_status(filename, Kitta, new_status):
    lands = []
    file = open(filename, "r")
    for line in file:
        line = line.replace("\n", "")
        land_data = line.split(",")
        current_kitta = land_data[0]
        current_kitta = current_kitta.replace(" ", "")
        Kitta = Kitta.replace(" ", "")
        if current_kitta == Kitta:
            land_data[-1] = new_status
        land_string = ""
        for i in range(len(land_data)):
            if i > 0:
                land_string += ","
            land_string += land_data[i]
        lands.append(land_string)
    file.close()
    
    file = open(filename, "w")
    for land in lands:
        file.write(land + "\n")
    file.close()
    
