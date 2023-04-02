# Joseph Martz
# M02_Lab
# Gets the names and gpa of students and displays if they are on the deans list or honor roll
while True:
    lastName = input("Students last name ['ZZZ' to quit]: ")
    if lastName.upper() == "ZZZ":
        quit()
    
    firstName = input("Students first name: ")
    name = firstName + " " + lastName
    
    gpa = float(input(name + "'s gpa: "))
    
    if gpa >= 3.5:
        print(name + " has made the Dean's List! ")
    if gpa >= 2.25:
        print(name + " has made the Honor Roll! ")
    if input("Another Student? [Y to continue]: ").upper() != "Y":
        quit()

