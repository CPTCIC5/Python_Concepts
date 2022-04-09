'''
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

supplies2 = ['pens', 'staplers', 'flamethrowers', 'binders']
for index,item in enumerate(supplies):
    print('Index '+ str(index) + ' in supplies is: ' + item)
'''

#print(supplies[::])
#print(supplies[::3])
#print(supplies[-1])

# program lets the user type in a pet name and then checks to see whether the name is in a list of pets.
'''
my_pets = ['Zophie', 'Pooka', 'Fat-tail']
name=input('Enter a pet name').capitalize()

if name not in my_pets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
'''

'''
#supplies.sort()
supplies.sort(reverse=True)
supplies.sort(key=str.lower)
'''

'''
import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)]) #=1 cuz len indexing 
#starts from 1 not 0 , n if the len val is maximixed n the random val is also maximized so it wont slice/find it/index it cuz indexing starts from 0
'''

'''
tuple(['cat', 'dog', 5])
list(('cat', 'dog', 5))
list('hello')
'''

#QUESTIONS
#1.Empty list
#2.
# lst=[2, 4, 6, 8, 10]
#lst.insert(2,'hello')
#print(lst)
#3.[3]
#4.[-1]last val of list /cuz it's reversing indexing cuz of **-** argument
#5.[2]Prints 2nd val of list
#6.tells the list indexing of the object
#7.adds the value at last
#8.removes the value
#9.+,.copy()
#10. appends add the object at last of string but by insert val is added at which index we want
#11..remove('value'),.pop(),del
#12.can be sliced,can be fetched via []
#13.Tuples r immutable/values cant be changed,lists r mutable /val can be changed 
#14.tuple(42)
#15.