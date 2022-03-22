'''

#prog to take input of marks n roll no. of 4 students n send into a dict
r_no=[]
marks=[]
#to ask user for no. if inputs
total_turns=int(input("How many student's results u want?"))
for i in range(total_turns):
    roll_no=int(input('Enter Roll no.'))
    mark=int(input('Enter Marks'))
    r_no.append(roll_no)
    marks.append(mark)
x1=dict(zip(r_no,marks))
print(x1)
'''

'''
#prog to  convert 2 lists into a dict , 1 list keys n 1 values
keys=['One','Two','Three']
values=[1,2,3]
x1=dict(zip(keys,values))
print(x1)
'''

'''
#prog to print 2nd highest digit on a array
x1=[111,25,35,42,51]
x1.sort()
x1.reverse()
print(x1[1])
'''

'''
#prog to print every element of a arr in a seperate line with indexing, n reverse indexing
l=['q','w','e','r','t','y']
lenght=len(l)
for x in range(lenght):
    print(x,x-lenght,l[x])
'''

