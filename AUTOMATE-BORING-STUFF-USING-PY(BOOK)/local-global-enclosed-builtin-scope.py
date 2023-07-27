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

#global scope
global_var=10
def xyz():
    print('global scope',global_var)
    enclosed_var=8
    def xy():
        print('enclosed scope',enclosed_var)
        def local():
            local_var=9
        #print(local_var) #cant be called outside it's own iteration