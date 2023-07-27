import csv


name=input('Enter ur name').strip().upper()
with open("phonebook.csv","r") as file:
    reader=csv.DictReader(file)
    counter=0
    for row in reader.up:
        if row['NAME'].strip().upper() == name:
            counter+=1

print(counter)