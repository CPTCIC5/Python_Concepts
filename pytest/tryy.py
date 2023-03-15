"""
def main():
    x=int(input())
    print('x squared is ',square(x))

def square(m):
    return m*m

if __name__ == "__main__":
    main()

"""


def main():
    inp_name=input('whats ur good name ')
    greet()

def greet(name='world'):
    return f'Hello, {name}'


if __name__=="__main__":
    main()