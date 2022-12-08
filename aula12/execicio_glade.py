import gi
from pint import UnitRegistry

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from os.path import abspath, dirname, join

global changed_box_1
global changed_box_2

global unit_vec
#global combo_opt
#global mtx_conv

config_in = open('./aula12/config.txt', 'r')

units_list = list(config_in.read().split('#'))

print(units_list)

#combo_opt = [['Litro', 'Mililitro'], ['Newton/mm²', 'Atmosfera']]
#mtx_conv = [[1, 1000], [1, 9.86923]]
"""
for i in range(len(combo_opt)):
    i += 1 #pular o cabeçalho
    list_linha = config_list[i].split(',')
    
    for j in range(len(list_linha)):
        
        temp_list.append(list_linha[j])
        
        if j == 2:
            #Casting each element in temp_list
            for i in range(len(temp_list)):
                temp_list[i] = float(temp_list[i])
            
            #append to 'matrix_conversion' list
            mtx_conv.append(temp_list.copy())
            temp_list = []
            
"""
config_in.close()


class TheApp:
    '''The Application Class.'''

    def __init__(self):
        global combo_opt
        global unit_vec
        
        # Build GUI
        self.builder = Gtk.Builder()
        self.builder.add_from_file('./aula12/execicio_glade.glade')
        # Get objects
        self.window = self.builder.get_object('window')
        # Cria uma array de duas colunas, a primeira para ser uma espécie de
        # identificador, ID, e a outra, o texto mostrado. Poderia ser uma
        # coluna int e outra string, caso os Ids fossem numéricos.
        self.liststore = Gtk.ListStore(int, str)
        self.liststore_units = Gtk.listStore(int, str)

        # Initialize interface
        
        acum = 0
        volume_list = list()
        temp_list = list()
        
        for i in combo_opt:
            
            temp_list.append(acum)
            temp_list.append(i)
            
            volume_list.append(temp_list.copy())
            temp_list = []
            
            acum += 1
        
        for vol in volume_list:
            self.liststore.append(vol)
        
        
        for unit in unit_vec:
            self.liststore_units.append(unit)

        # Associando a array (ListStore) ao ComboBox
        self.combo_1 = self.builder.get_object('combo_box1')
        self.combo_2 = self.builder.get_object('combo_box2')
        self.combo_units = self.builder.get_object('combo_units')
        
        self.combo_1.set_model(self.liststore)
        self.combo_2.set_model(self.liststore)
        self.combo_units.set_model(self.liststore_units)
        # É necessário adicionar um renbderizador de texto ao ComboBox
        renderer_text = Gtk.CellRendererText()
        
        self.combo_1.pack_start(renderer_text, True)
        self.combo_2.pack_start(renderer_text, True)
        self.combo_units.pack_start(renderer_text, True)
        
        # Escolher qual coluna mostrar:
        self.combo_1.add_attribute(renderer_text, "text", 1)
        self.combo_2.add_attribute(renderer_text, "text", 1)
        self.combo_units.add_attribute(renderer_text, "text", 1)

        # Opção ativa default
        self.combo_1.set_active(0)
        self.combo_2.set_active(0)
        self.combo_units.set_active(0)

        # Connect signals
        self.builder.connect_signals(self)

        # Everything is ready
        self.window.show()

    def on_window_destroy(self, widget):
        '''Classical window close button.'''
        Gtk.main_quit()

    def teste1_chg(self, dois):
        global changed_box_1, changed_box_2

        changed_box_2 = False
        changed_box_1 = True
        
        self.convert(1)
        
    
    def teste2_chg(self, dois):
        global changed_box_1, changed_box_2

        changed_box_2 = True
        changed_box_1 = False
        
        self.convert(2)
        
        
    def convert(self, ind_mud):
        global mtx_conv
        global changed_box_1, changed_box_2
        
        
        ind_mud -= 1 #1 - vol_1 será convertido, 2 - vol_2 sera convertido
        
        vol_1 = self.builder.get_object("vol_1")
        vol_2 = self.builder.get_object("vol_2")
        
        model1 = self.combo_1.get_model()
        active1 = self.combo_1.get_active()
        
        model2 = self.combo_2.get_model()
        active2 = self.combo_2.get_active()
        
        
        ind_box1 = model1[active1][0]
        ind_box2 = model2[active2][0]
        
        
        if(ind_mud == 0):
            vol1_num = float(vol_1.get_text())
            var_num = vol1_num
            
            #recebe o obj que ira mudar
            var_obj = vol_2
            
            convert_const = mtx_conv[0][ind_box2]/mtx_conv[0][ind_box1]
            
            
        else:
            vol2_num = float(vol_2.get_text())
            var_num = vol2_num
            
            #recebe o obj que ira mudar
            var_obj = vol_1
            
            convert_const = mtx_conv[0][ind_box1]/mtx_conv[0][ind_box2]
                

        resp = var_num * convert_const
        var_obj.set_text(str(resp))
        
    
    def on_button_clicked(self, button):
        global changed_box_1, changed_box_2

        if(changed_box_1 >= changed_box_2):
            self.convert(1)
        else:
            self.convert(2)
  
  
if __name__ == '__main__':
    try:
        gui = TheApp()
        Gtk.main()
    except KeyboardInterrupt:
        pass
