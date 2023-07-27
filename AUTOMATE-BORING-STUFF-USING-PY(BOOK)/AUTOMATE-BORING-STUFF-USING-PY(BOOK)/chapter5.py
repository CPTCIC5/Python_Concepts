birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name:(blank to quit)')
    name=input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name],'is bday of '+name)
    else:
        print('no user with this name found,lets add a user with this info')
        bday=input('bday')
        birthdays[name]=bday
        print('Birthday database updated.')
        break

#QUESTIONS
#1.{}
#2.x1={'foo':42}
#3. on dict we can't make keys of same name(but in list we can add 2 item of same name),
# on dict data is stored in the form of key-value pairs(but in list it's stored as item),
# n dict it's done by keys/can be of any datatype,but on list indexing starts from 0
# on dict we can fetch via keys , fetched by slicing
#4.error key value pair  not found in 'spam'
#5 <what-we-r-finding> in <varname> in keyword is used to find 
# if key-value pair is find(it searches key) but cat just mean key-value pair inside <varname>
#6 same as q5 but for values not keys 
#7.spam.setdefault('color', 'black')
