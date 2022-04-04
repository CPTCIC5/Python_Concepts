li=eval(input())
x=list(li)
#sol 1
#x.reverse()
#print(x)

#sol 2
#print(x[::-1])

#sol 3
i=len(x)-1
for j in range(0,len(x)//2):
    x[j], x[i] = x[i], x[j]
    i-=1
