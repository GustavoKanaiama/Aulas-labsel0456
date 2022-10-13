f = open("leitura.txt", "r")


core_list = list(f.read())

final_string = "";

aspas_counter = 0;

for i in core_list:
    #Aspas fechadas e encontrei uma aspas -> abrir
    if(i == '"') and (aspas_counter == 0):
        aspas_counter = 1
    
    #Aspas abertas e encontrei outra aspas -> fechar
    if(i == '"') and (aspas_counter == 1):
        #final_string = core_list.index(i)
        aspas_counter = 0
        
    #Aspas fechadas e encontrei virgula
    if(aspas_counter == 0) and (i == ','):
        core_list[core_list.index(i)] = ";"



full_words = ''

for i in core_list:
    full_words += i
    

print(full_words)

    

