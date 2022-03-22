#dictionaries are objects in which we store data in form of key value pair 
#mutable/data can be changed

'''n1={
"hello":"hello",
"name":"ARYAN",
'class':11,
'subject':'PCM'
}
n1['migrate']={"b":'MAGGIE','D':'chicken'}
print(n1['migrate'])
del n1['migrate']/n1.pop('migrate')
print(n1.get('migrate'))
'''


'''
n1={"name":'Corey',
"age":15,
"first_name":"Corey",
"last_name":"MS",
}
n1['email']='@GMAIL.COM'
print(n1['email'])
del n1['email']
print(n1.get('email'))
'''

'''
#adding 2 dict by .update() same as .extend() in lists
n1={
    'name':'Aryan',
    'age':16,
    'data' : 5.5
}
n2={
    'Subject':'PCM+CS',
    "Bio" :'A CODER'
}
n1.update(n2)
print(n1)
'''

'''
#copying a dict
n1={
    'name':'Aryan',
    'age':16,
    'data' : 5.5
}
n2=n1.copy()
print(n2)
print(n1==n2)
'''


'''
n1={
"hello":"hello",
"name":"ARYAN",
'class':11,
'subject':'PCM',
'data' : {'Breakfast':'Paneer','Lunch': 'Tikka','Dinner' :'Masala'}
}
n1['INFO'] = 'SOME BASIC INFO'
print(n1.items())


x1=['One','Two','Three']
x2=[1,2,3]
x3=dict(zip(x1,x2))
print(x3)
'''