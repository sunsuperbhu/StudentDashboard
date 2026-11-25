
print("=========================================")
print("            REGISTER BOARD")
print("=========================================")

Studentname = input("Enter Student Name: ")
StudentID = input("Enter Student ID: ")
sex = input("Enter Student gender: ")

Subject = input("Enter Subject: ")
hour1 = int(input("Enter number of hours: "))

Subject2 = input("Enter second subject: ")
hour2 = int(input("Enter number of hours for second subject: "))

Subject3 = input("Enter third subject: ")
hour3 = int(input("Enter number of hours for the third subject: "))

Numofhrspesubject1 = 3

total_hours = hour1 + hour2 + hour3
average_hours = total_hours / Numofhrspesubject1

print("=========================================")
print("            STUDENT DASHBOARD")
print("=========================================")

print("Student Name:", Studentname)
print("Student ID:", StudentID)
print("Gender:", sex)

print("Total number of subjects:", Numofhrspesubject1)

print("Subject:", Subject)
print("Hours:", hour1)

print("Subject 2:", Subject2)
print("Hours:", hour2)

print("Subject 3:", Subject3)
print("Hours:", hour3)

print("Total hours for all subjects:", total_hours)
print("Average hours for all subjects:", average_hours)

print("=========================================")
