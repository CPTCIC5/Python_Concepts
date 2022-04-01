import csv

'''
name=input("Name :")
no=input("Number :")
with open("phonebook.csv","a") as e:
    writer=csv.writer(e)
    writer.writerow([name,no])
'''

'''
uniqueness=set()
with open('phonebook.csv','r') as file:
    #reader=csv.reader(file)
    #next(reader)
    reader=csv.DictReader(file)
    for row in reader:
        uniqueness.add(row['ARYAN'].upper())
for unique in sorted(uniqueness):
    print(unique)
'''
