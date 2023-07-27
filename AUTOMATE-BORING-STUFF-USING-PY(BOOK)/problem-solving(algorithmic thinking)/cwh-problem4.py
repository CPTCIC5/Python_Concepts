import random

a=int(input('from:'))
b=int(input('to:'))
rand=random.randint(a,b)
name=input("Ur name")
info=[]
guess_taken=0
while True:
    guess=int(input(f"Hey,{name}enter ur guess from {a} to {b}:"))
    guess_taken+=1
    if guess == rand:
        info.append(name)
        info.append(guess_taken)
        break
    else:
        continue
print(name,guess_taken)    

print(rand)
print(guess_taken)