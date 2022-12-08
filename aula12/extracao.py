config_in = open('./aula12/config.txt', 'r')

config_list = list(config_in.read().split('\n#\n'))

qnt_unit = len(config_list)


print(config_list)
list_temp_name = list()
list_temp_val = list()

unit_list = list()
combo_opt = list()
mtx_conv = list()

for combo_list in config_list:
    
    
    element_list =combo_list.split('\n')
    
    print(element_list)
    print()
    
    #Append do título da lista em outra lista(de títulos especificamente)
    unit_list.append(element_list[0])
    
    #Retirar o título da lista
    element_list.pop(0)
    
    print()
    print(element_list)
    print()
    for i in range(len(element_list)):
        
        name_value_list = element_list[i].split(' - ')
        print(name_value_list)
        list_temp_name.append(name_value_list[0].strip())
        list_temp_val.append(float(name_value_list[1].strip()))
    
    combo_opt.append(list_temp_name.copy())  
    mtx_conv.append(list_temp_val.copy())  
    list_temp_name = list_temp_val = []

print()
print(unit_list)
print(combo_opt)
print()
print(mtx_conv)

