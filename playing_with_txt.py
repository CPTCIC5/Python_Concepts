'''
with open('test.txt','r') as f:
    f_content=f.read(100)  #  this will read only first 100 character then break  # reads the file (retrieve whole content)
   
   
   #f.content=f.readline() --> it reads line one
    
    print(f_content)

    #print(f.name) display's file name , f.mode displays mode of files opened
'''
#when we use read or readline function it requires much memory as it reads whole file at once best way is 
with open('test.txt','r') as f:
    for line_by_line in f:
        print(line_by_line,end='')

#writing in a file
with open('test2.txt','w') as d:
    d.write('HEY')
    