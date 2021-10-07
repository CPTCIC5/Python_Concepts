can_be_played=3
till_now=0

while till_now<can_be_played:
    n1=input('enter help for options')
    till_now=till_now + 1

    if n1=='help' or 'HELP' :
        n2=input('WRITE START TO START THE GAME \n WRITE END TO END THE GAME ')

        if n2=='START' or 'start':
            print('GAME HAS BEEN STARTED')

        if n2=='END'or 'end':
            print('ENDED THE GAME')

    else:
        print('GYA')
