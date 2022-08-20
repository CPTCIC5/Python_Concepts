def main(name):
    def wrapper():
        print(name)
    return wrapper


x = main('aryan')
print(x)

@main
def xyz():
    print('xyz')

xyz()