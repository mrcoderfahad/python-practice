name = input("What Is Your Name: ")
phone_number = input("Your Phone Number: ")

if len(phone_number) > 11:
    print(f"{name} Your Phone Number Is Too Long {phone_number}")
elif len(phone_number) < 11:
    print(f"{name} Your Phone Number Is Too Short {phone_number}")
elif len(phone_number) == 11:
    print(f"{name} Thank You, We send Code In this Number {phone_number}")
