try:
    n1=int(input('ENTER ANY DIGIT'))
    income=2000
    risk=income/n1
    print(n1)
except ZeroDivisionError:
    print('CANT BE DIVIDE BY 0')
except ValueError:
    print('ENTER INT RATHER THEN STR')

