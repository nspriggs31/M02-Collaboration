""" Name: Nathan Spriggs
    Program Name: GPA Qualifications
    Purpose: Prompts user to input student last name. If last name is not "ZZZ" then program will prompt user to input student GPA. Program
              will determine is student qualifies for Dean's List, Honor Roll, or neither based on preset parameters. Program will continue until 
              "ZZZ" is input as the last name. """


lastName = input("Enter student last name: ")

while(lastName != "ZZZ"):

    firstName = input("Enter student first name: ")
    GPA = float(input("Enter GPA: "))
    name = firstName + " " + lastName
    
    if (GPA >= 3.5):
        print(name + " has made the Dean's List.")

    elif (GPA >= 3.25 and GPA < 3.5):
        print(name + " has made the Honor Roll.")

    elif (GPA < 3.25):
        print (name + " has not made the Honor Roll or Dean's List.")

    lastName = input("Enter student last name: ")

    if (lastName == "ZZZ"):
        exit()
