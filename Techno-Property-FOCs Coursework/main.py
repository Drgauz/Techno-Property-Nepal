
from read import Lands
from operation import rent_land, return_land
import read
import operation
#Empty Dictionary Created
RentingDict = {}

print("\n")
print("\n")
print("\t \t \t \t \t       Techno Property Nepal")
print("\n")
print("\t \t \t \t New Baneshwor, Kathmandu | Contact no. : 9793104925")
print("\n")
print("\t \t _____________________________________________________________________")
print("\t \t Greetings from the system administrator! I wish you a wonderful day ahead of you today!")
print("\t \t _____________________________________________________________________")
print("\n")
print("\t ---------------------------------------------------------------------------------------------------------")
print("\t A couple of options available to you to do the necessary action within the system")
print("\t ---------------------------------------------------------------------------------------------------------")
print("\n")
print("\t Enter 1 to Rent the Land")
print("\t Enter 2 to Return the Land")
print("\t Enter 3 to Exit from system")
print("\n")
print("    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#Function named main() created
def main():
    lands = Lands()
    
    while True:
        A = input("Enter a number from above option = ")  #Ask user whether to rent, return or exit from the system.
        if A == "1": #carries our rent process
            file = open("lands.txt", "r")  # This line shows details of available and unavailable lands
            print(file.read())
            file.close()

            Kitta_no = input("Enter the kitta number of the land to rent: ")  #Input details required for renting
            Name = input("Enter purchaser name: ")
            Phone_no = input("Enter purchaser phone number: ")
            
            try:
                rentingPeriod = int(input("Enter the renting span: "))
            except ValueError:
                print("Invalid Input!")
                return main()
            
            rent_land(lands, Kitta_no, Name, Phone_no, rentingPeriod, RentingDict)
            lands = read.Lands()  
                
        elif A == "2": #carries our return process
            
            kitta = input("Enter kitta number: ")
            name = input("Enter customer name: ")
            phone = input("Enter customer phone number: ")
            
            try:
                real_rentingPeriod = int(input("Enter the span purchaser holding the land: "))
            except ValueError:
                print("Invalid Input!")
                return main()
                
            return_land(lands, kitta, name, phone, real_rentingPeriod, RentingDict)
            lands = read.Lands() 
            
        elif A == '3':
            print("Exiting from the system. Thank you!")  # Exit the program
            exit()
        else:
            print("Invalid Input! Please try again.")
  
print(main())
