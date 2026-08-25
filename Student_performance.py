name = input("Enter Student Name:")
Computer_Science = float(input("Enter Computer Science Marks:"))
Mathematics = float(input("Enter Mathematics Marks:"))
Statistics = float(input("Enter Statistics Marks:"))

total = Computer_Science+Mathematics+Statistics
average = total/3

if average >= 60:
    grade = "A+"
elif average >= 50:
    grade = "A"
if average >= 40:
    grade = "B+"
elif average >= 30:
    grade = "B"
else :
    grade = "C"

print("\n------------Student Performance Report------------")
print("Student Name:",name)
print("Computer Science:",Computer_Science)
print("Mathematics:",Mathematics)
print("Statistics:",Statistics)
print("Total Marks:",total)
print("Average Marks:",average)
print("Grade:",grade)


