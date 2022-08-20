"""
try:
    x =  int(input('whats x'))
except ValueError:
    print('pls enter int inside x input not str')

print(f"x is {x}")"""


"""
while True:
    try:
        x =  int(input('whats x?'))
        break
    except ValueError:
        print('x isnt an int')
"""

def main():
    x = get_int()
    print(f'x is {x}')

def get_int():
    while True:
        try:
            x =  int(input('whats x?'))
            break
        except ValueError:
            #print(f'{x} isnt an int')
            pass

main()