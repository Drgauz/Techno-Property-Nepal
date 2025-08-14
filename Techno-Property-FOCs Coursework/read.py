# This function  read and process land data
def Lands():
    lands = [] #create empty list
    file = open("lands.txt", "r")
    for line in file:
        line = line.replace("\n", "")
        line = line.replace(" ", "")
        parts = line.split(",")
        if len(parts) >= 6:
            kitta = parts[0].replace(" ", "")
            location = parts[1].replace(" ", "")
            direction = parts[2].replace(" ", "")
            annas = parts[3].replace(" ", "")
            cost = parts[4].replace(" ", "")
            status = parts[5].replace(" ", "")
            lands.append([kitta, location, direction, annas, cost, status]) 
    file.close()
    return lands

