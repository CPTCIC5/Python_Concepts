'''
def spam():
    eggs=10
    print(eggs)
print(eggs) #LOCAL SCOPE VAR CANT BE USED AT GLOBAL LVL
'''

#CALLING A FUN INSIDE FUN /CALLSTACK

'''
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
spam()
'''

'''
#USING LOCAL VAR AS GLOBAL
def spam():
    global eggs
    eggs=10
    print(eggs)
print(eggs) #LOCAL SCOPE VAR CANT BE USED AT GLOBAL LVL
'''

'''
def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
'''

'''
import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
'''

#QUESTIONS
#1.Cuz it saves the whole set of program inside a func,n then can be called later n in 1 time via callbacks,fast,cleanliness
#2.when the function is called
#3.def
#4. in function we define it's name n what it will execute/do , we use callbacks to execute stuff inside func at required place when needed
#5.One global scope,1 local scope
#6.it gets stored as output of callback of that particular function
#7.return saves the output of a function n save it , it doesn't print unless the callback is printed/it's output of the function
#8.The function always returns None if explicit return is not written./anything isn't printed
#9.global <varname>
#10.it itself is a seperate datatype which represent nthg /None
#11 no module/function on local disk like that == error
#12. by it's prefix after .
#13.by  using exceptions , adding the code into try n error into expect block
#14.try clause try to the run the program , expect block handles the error to ensure the code doesn't break


#PROBLEM STATEMENT SOL
#1
'''
def collatz(number):
    if number % 2 ==0:
        x1=number // 2
        return x1
    elif number %2 != 0:
        x2=3 * number + 1
        return x2
print(collatz(3))
'''
