n1=int(input('ENTER UR WEIGHT'))
n2=input('ENTER  K OR G')

if n2=='K' or 'k':
    xd=n1 *1000
    print(xd,"g")

if n2=='G' or 'g':
    xdd=n1 //1000
    print(xdd,"kg")