'''
#
answer=69
no_of_turns=int(input('No of times u wanna play babess'))
for i in range(no_of_turns):
    inp=int(input('Enter input'))
    if inp==answer :
        print('nice')
        break
    else:
        print('tumse nai hopaega')
        continue
'''


'''
answer=69
no_of_turns=int(input("No.of times u want to play babess"))
turns_used=0
while no_of_turns>turns_used:
    turns_used+=1
    inp=int(input("Enter input"))
    if inp == answer:
        print('nice')
        break
    else:
        print("tumse nai hopaega")
        continue
'''

'''
mrk=[]
roll_no=[]
inp=int(input('Total inputs'))
turns_used=0
while inp>turns_used:
    turns_used+=1
    r_no=int(input('roll no'))
    marks=int(input('marks'))
    roll_no.append(r_no)
    mrk.append(marks)
x1=dict(zip(mrk,roll_no))
print(x1)
'''

'''
mrk=[]
roll_no=[]
inp=int(input('How many users input u want'))
for i in range(inp):
    r_no=int(input('roll no'))
    marks=int(input('marks'))
    roll_no.append(r_no)
    mrk.append(marks)
x1=dict(zip(mrk,roll_no))
print(x1)
'''


'''
users=int(input("How many users data u wanna save save"))
name_of_user=[]
result_of_user=[]
total_used_users=0
while users>total_used_users:
    total_used_users+=1
    name=input('Aryan')
    result=int(input('(Int input required) No.of marks'))
    name_of_user.append(name)
    result_of_user.append(result)
typecasting=dict(zip(name_of_user,result_of_user))
print(typecasting)
'''


'''
users=int(input("How many users data u wanna save"))
name_of_user=[]
result_of_user=[]
for i in range(users):
    name=input('Name')
    result=int(input('(Int input required) No.of marks'))
    name_of_user.append(name)
    result_of_user.append(result)
typecasting=dict(zip(name_of_user,result_of_user))
print(typecasting)
'''