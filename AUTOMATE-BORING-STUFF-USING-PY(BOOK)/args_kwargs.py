#what are *args
#THESE ARE THE ARGUMENTS WHICH HANDLES PARAMATER OF STR OR INT(IN DEF(FUNC))

#what are **kwargs
#THESE ARE THE ARGUMENTS WHICH HANDLES PARAMATER OF VARS 
'''
def function(*args,**kwargs):
    print(f'QUESTION ID I {args}',kwargs) # here this args will print all int and str values #kwargs handle vars
function('hello','op','aryan',id=123) #result=QUESTION ID I ('hello', 'op', 'aryan')
'''

#discoving args  more
#without args and kwargs 
'''
def my_func(first_name,last_name):
    print(f'{first_name}{last_name}')
my_func('ARYAN','OP')
'''

'''
#with args
def my_func(*args):
    print({args})
my_func('ARYAN''OP')
'''

'''
#without kwargs
def my_func(error_message):
    error_message="Error Occured"
    print(f"{error_message}")
my_func(error_message="error_message")
'''

'''
#with kwargs
def my_func(**kwargs):
    print(f'kwargs work as',kwargs)
my_func(n1='3r3r3r',n2='effeef')
'''