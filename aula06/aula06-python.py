a = 1
b = 2

print("a = {a}, b = {b}".format(a = a, b = b))

d = 10


def f(x, y):
    global d
    
    c = x + y + d
    
    
    return c


print(f(3, 5))




def f_com_args(x, *args):
    
    print("x = {k}".format(k = x))
    
    for i in args:
        print(i)
        
        
g = [1, 2, 3, 34, 5, 6, 7]

f_com_args(12, g)
    
