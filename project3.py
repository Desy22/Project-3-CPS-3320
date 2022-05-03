import csv

with open('Schedule.csv', 'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(["Class Name", "Section", "Description", "Credits", "Semester", "Days", "Time"])
    noOfClasses = int(input("Please enter how many classes you are taking: "))
    for i in range(noOfClasses):
        className = input("Please enter the name of your class: ")
        section = input("Please enter the section of your class: ")
        desc = input("Please enter the description of the class: ")
        credits = input("Please enter the amount of credits for this class: ")
        semester = input("Please enter the semester for this class: ")
        days = input("Please enter what days this class falls on(M/T/W/TH/F): ")
        time = input("Please enter the time of class(Ex= 9:00am-10:15am): ")
        myFile.writerow([className, section, desc, credits, semester, days, time])

import pandas as pandasForSortingCSV
sortClasses = input("Would you like to sort these classes in alphabetical order?(Y/N): ")

if sortClasses == 'Y':
    csvData = pandasForSortingCSV.read_csv("Schedule.csv")
    csvData.sort_values(["Class Name"], 
                        axis=0,
                        ascending=[True], 
                        inplace=True)
    print("\nAfter sorting:")
    print(csvData)

else:
    print("Okay!")

