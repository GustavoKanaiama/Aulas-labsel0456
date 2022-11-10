def fact(x):
    x = int(x)
    return 1 if(x == 0) else (x*fact(x-1))

def fib(n):
    n = int(n)
    if (n == 2):
        return 1
    
    return n if (n == 0 or n == 1) else (fib(n-1) + fib(n-2))

f_in = open('./aula11/teste.data', 'r')

list_read = f_in.read().split()


list_pri = list()
list_sec = []

n_col = 3
    
acum = 0

# (0) -> número de entrada
# (1) -> seu resultado (a ser verificado) em fib()
# (2) -> seu resultado (a ser verificado) em fact()

#Formatando os dados em uma lista de listas
for i in list_read:

    if acum >= 3:
        list_pri.append(list_sec.copy())
        list_sec = []
        acum = 0
        
    list_sec.append(i)
    
    acum += 1
    
#print(list_pri)

for i in range(len(list_pri)-1):
    
    i += 1 #pulando o cabeçalho
    
    print(i)