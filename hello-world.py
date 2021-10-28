def hello_world(x):
    x = x * ['hello world!']
    a =  0
    for c in x:
        a = a + 1
        print(str(a) + '. ' +  str(c))

hello_world(6)
