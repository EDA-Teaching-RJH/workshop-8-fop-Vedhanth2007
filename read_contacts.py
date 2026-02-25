import csv

contact = []

with open("contacts.csv", mode = 'r') as file:
        read = csv.DictReader(file)
        for line in read:
            contact.append({"name": line["name"], "email": line["email"]})
for person in contact:
   print(f"name: {person['name']}, email: {person['email']}")
