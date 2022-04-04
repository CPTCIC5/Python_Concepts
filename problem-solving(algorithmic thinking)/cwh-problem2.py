n=int(input('No.of apples'))
mn=int(input('Minimum:'))
mx= int(input('Maximum:'))
print(n)
if mn == mx:
    print('minimum n max val cant be same! ERROR')
    exit()
for i in range(mn,mx+1):
    if i % 2 ==0:
        print(f"{i} is a divisor")
    else:
        print(f"{i} isnt a divisor")