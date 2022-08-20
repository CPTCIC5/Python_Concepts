x = 0
def foo():
    x=2
    def bar():
        x = 7
        print('pttint',x)
    bar()
    print('ptint',x)

print('print2',x)
foo()
print('print',x)