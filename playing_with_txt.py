'''
with open('test.txt','r') as f:
    f_content=f.read(100)  #  this will read only first 100 character then break  # reads the file (retrieve whole content)
   
   
   #f.content=f.readline() --> it reads line one
    
    print(f_content)

    #print(f.name) display's file name , f.mode displays mode of files opened
'''

'''
#when we use read or readline function it requires much memory as it reads whole file at once best way is 
with open('test.txt','r') as f:
    for line_by_line in f:
        print(line_by_line,end='')
'''

'''
#writing in a file
with open('test2.txt','w') as d:
    d.write('HEY')
'''

with open('data.txt','w') as e:
    roll_no=[]
    marks=[]
    total_students=int(input('Enter total no. of students who need data'))
    for data in range(total_students):
        r_no=int(input("Enter roll no."))
        mrk=int(input("Enter marks"))
        roll_no.append(r_no)
        marks.append(mrk)
    e.write(f"{roll_no}-{marks}")
'''
with open('dictionary.txt','r') as f:
    content = f.read()
    print(content)
    x1=content.replace(' ',',')
    print(x1)
with open('dictionary.txt','w') as e:
    e.write(x1)
'''
