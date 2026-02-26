import re 
id = input("Enter a valid id num: ")

if re.search(r"^[A-Za-z]{4}\d{4}$", id):
    print("Valid id number")
else:
    print("Invalid id number")