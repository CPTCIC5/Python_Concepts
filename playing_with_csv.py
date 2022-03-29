import csv

'''
name=input("Name :")
no=input("Number :")
with open("phonebook.csv","a") as e:
    writer=csv.writer(e)
    writer.writerow([name,no])

'''

with open('phonebook.csv','r') as file:
    reader=csv.reader(file)
<<<<<<< HEAD
    next(reader)
=======
>>>>>>> test
    #csv_reader=csv.DictReader(file)
    for row in reader:
        print(row)
