def isEven(n):
    if n % 2 ==0:
        return True
    else:
        return False

def isOdd(e):
    if e %2 !=0:
        return True
    else:
        return False

for i in range(0,11,3):
    print(isEven(i))