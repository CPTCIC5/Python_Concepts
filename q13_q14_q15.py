import random


'''
#q13
queryset=[
'Adoni',
'Amaravati',
'Anantapur',
'Chandragiri',
'Chittoor',
'Dowlaiswaram',
'Eluru',
'Guntur',
'Kadapa',
'Kakinada',
'Kurnool',
'Machilipatnam',
'Nagarjunakoṇḍa',
'Rajahmundry',
'Srikakulam',
'Tirupati',
'Vijayawada',
'Visakhapatnam',
'Vizianagaram',
'Yemmiganur'] #data of cities

add_query=input('ENTER CITY NAME >>> ') #for taking another city as input
conversion=str(add_query) #converts str to list so can be added(appended) on list on cities
queryset.append(conversion) #retrieve the input and adds to list

print(random.choice(queryset))  #the main output **THE RANDOM CITY**
print(queryset) #whole list REASON:to check the appended input is added to list or not
'''

'''
#q14
x1=random.randint(1,6)

guess_count=0
guess_limit=5

while guess_count<guess_limit:
    n1=int(input('ENTER SCORE FOR PLAYER ONE.'))
    guess_count= guess_count +1
    score_inputs=n1
    final_score=n1+x1
print(f" final score for player one is{final_score}")

guess_count1=0
guess_limit1=5

while guess_count1<guess_limit1:
    n1=int(input('ENTER SCORE FOR PLAYER TWO.'))
    guess_count1= guess_count1 +1
    score_inputs=n1
    final_score1=n1+x1
print(f"final score for player two is{final_score}")
'''

#Q15
import csv
login=False

while login==False:
    data=[]
    with open('login.csv') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            data.append(row)
    print(data)

    un=input('Please enter username')
    pw=input('Please enter password')

    col0=[x[0] for x in data]
    col1=[x[0] for x in data]

    if un in col0:
        for k in range (0,len(col0)):
            if col0[k] ==un and col1[k] ==pw:
                print('You r logged in ')
                login=True
    else:
        print('Wrong username n password')


'''
#q9
def CountWordsToThe():
    f=open('Poem.txt','r')
    count=0
    data=f.read()
    word=data.split()
    for i in word:
        if i=='to' or i=='the':
            count+=1
    print("Total words 'the' and 'to':",count)
    f.close()
CountWordsToThe()
'''

'''
#Q8
class Student:
    def __init__(self,roll_no,name,age,percentage):
        self.roll_no=roll_no
        self.name=name
        self.age=age
        self.percentage=percentage
stud1=Student(1,'Aryan',17,65.3)
stud2=Student(2,'xyz',17,24)
stud3=Student(3,'yzs',17,53)
stud4=Student(4,'stud4',17,94)
stud5=Student(5,'stud5',17,94)
stud6=Student(6,'stud6',17,2)
stud7=Student(7,'stud7',17,2)
stud8=Student(8,'stud8',17,9)
stud9=Student(9,'stud9',17,9)
stud10=Student(10,'stud10',17,9)

x1=stud1.roll_no,stud1.name,stud1.age,stud1.percentage,stud2.roll_no,stud2.name,stud2.age,stud2.percentage,stud3.roll_no,stud3.name,stud3.age,stud3.percentage,stud4.roll_no,stud4.name,stud4.age,stud4.percentage,stud5.roll_no,stud5.name,stud5.age,stud5.percentage,stud6.roll_no,stud6.name,stud6.age,stud6.percentage,stud7.roll_no,stud7.name,stud7.age,stud7.percentage,stud8.roll_no,stud8.name,stud8.age,stud8.percentage,stud9.roll_no,stud9.name,stud9.age,stud9.percentage,stud10.roll_no,stud10.name,stud10.age,stud10.percentage
with open('output.txt','w') as f:
    f.write(str(x1))
'''

#Q10
'''import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)'''

#Q12
name=input('ENTER SPORTSMAN NAME ')
sport=input('ENTER  FAV SPORT NAME')
biodata=f"{name},{sport}"

if sport=='longjump' or 'long jump' and sport=='Swimming' or 'swimming':
    with open('sports.txt','w') as e:
        e.write(biodata)
else:
    with open('data.txt','w') as x:
        x.write(biodata)