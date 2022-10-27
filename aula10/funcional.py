def fact(x):
    x = int(x)
    return 1 if(x == 0) else (x*fact(x-1))

def fib(n):
    n = int(n)
    if (n == 2):
        return 1
    
    return 0 if (n == 0 or n == 1) else (fib(n-1) + fib(n-2))


with open('./aula10/output.dat', 'w') as f_out:
    
    f_in = open('./aula10/input.dat', 'r')
    
    f_out.write(''.join(list(map(lambda x : str(x[0])+' '+str(x[1])+ '\n', list(map(lambda x : [fib(x[0]), fact(x[0])], map(lambda x : x.split(',') if (',') in x else x.split(), f_in.read().split('\n'))))))))
    
    """
    #Ler o arquivo de entrada(input)
    db = f_in.read()
    
    #Criei uma lista de listas
    lista_de_listas = map(lambda x : x.split(',') if (',') in x else x.split(), db.split('\n'))

    #Aplicando fib() e fact() em cada um dos elementos
    res = map(lambda x : [fib(x[0]), fact(x[0])], lista_de_listas)
    
    
    #Transcrever de novo para o formato de string
    str_form = map(lambda x : str(x[0])+' '+str(x[1])+ '\n', list(res))
    
    #Dar criar uma string com join() iterando todos elementos das listas
    str_final = ''.join(list(str_form))
    

    f_out.write(str_final)
    """
    
    
    