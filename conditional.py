name = input("What Is Your Name: ")
age = int(input("What Is Your Age: "))

if(age <= 12):
    print("Child")

elif(age >= 13 and age < 20):
    print("Teenager")

elif(age >= 20 and age < 35):
    print("Young")

else:
    print("Old")
