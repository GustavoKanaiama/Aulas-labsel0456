import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from os.path import abspath, dirname, join


class TheApp:
    '''The Application Class.'''

    def __init__(self):
        # Build GUI
        self.builder = Gtk.Builder()
        self.builder.add_from_file('./aula12/execicio_glade.glade')

        # Get objects
        self.window = self.builder.get_object('window')
        # Cria uma array de duas colunas, a primeira para ser uma espécie de
        # identificador, ID, e a outra, o texto mostrado. Poderia ser uma
        # coluna int e outra string, caso os Ids fossem numéricos.
        self.liststore = Gtk.ListStore(int, str)

        # Initialize interface
        volume_list = [
            [1, 'Litro (L)'],
            [2, 'Mililitro (ml)'],
            [3, 'Metro cúbico (m³)']]
        for vol in volume_list:
            self.liststore.append(vol)

        # Associando a array (ListStore) ao ComboBox
        self.combo_1 = self.builder.get_object('combo_box1')
        self.combo_2 = self.builder.get_object('combo_box2')
        
        self.combo_1.set_model(self.liststore)
        self.combo_2.set_model(self.liststore)
        # É necessário adicionar um renbderizador de texto ao ComboBox
        renderer_text = Gtk.CellRendererText()
        
        self.combo_1.pack_start(renderer_text, True)
        self.combo_2.pack_start(renderer_text, True)
        
        # Escolher qual coluna mostrar:
        self.combo_1.add_attribute(renderer_text, "text", 1)
        self.combo_2.add_attribute(renderer_text, "text", 1)

        # Opção ativa default
        self.combo_1.set_active(0)
        self.combo_2.set_active(0)

        # Connect signals
        self.builder.connect_signals(self)

        # Everything is ready
        self.window.show()

    def on_window_destroy(self, widget):
        '''Classical window close button.'''
        Gtk.main_quit()

    def on_button_clicked(self, button):
        '''Do something...'''

        vol_1 = self.builder.get_object("vol_1")
        vol_2 = self.builder.get_object("vol_2")
        
        model1 = self.combo_1.get_model()
        active1 = self.combo_1.get_active()
        
        model2 = self.combo_2.get_model()
        active2 = self.combo_2.get_active()
        
        print("O valor da entrada é ", vol_1.get_text(), model1[active1][1])
        print("O valor da saida é ", vol_2.get_text(), model2[active2][1])


    def on_combo_changed(self, widget):
        '''Verify which option is selected'''
        model1 = widget.get_model()
        active1 = widget.get_active()
        if active1 >= 0:
            print('Opção selecionada: {} = {}'.format(model1[active1][0], model1[active1][1]))
        else:
            print('Sem opção.')


if __name__ == '__main__':
    try:
        gui = TheApp()
        Gtk.main()
    except KeyboardInterrupt:
        pass
