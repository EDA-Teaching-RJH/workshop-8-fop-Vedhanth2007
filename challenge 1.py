import re 
num = input("Enter a valid phone num: ")

if re.search(r"^07\d{9}$", num):
    print("Valid num")
else:
    print("Invalid num")