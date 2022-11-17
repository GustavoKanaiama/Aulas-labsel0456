	

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window): # *1
    def __init__(self):
        super().__init__(title="Hello World") # 'Super' é o ancestral ( no caso Gtk.Window que esta sendo herdado em *1)

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked) # Conectando o sinal 'clicked' com o método *2
        self.button.connect("enter", self.on_button_enter)
        
        self.add(self.button)

    def on_button_clicked(self, widget): # *2
        print("Hello World")
        
    def on_button_enter(self, widget): # 'widget' é o próprio objeto button
        print("Mouse entrou")
    

#Cria os widgets
win = MyWindow()

#Conecta os sinais
win.connect("destroy", Gtk.main_quit)

# Apresenta
win.show_all()

#Entra no loop
Gtk.main()
