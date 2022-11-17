import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Handler:
    def on_destroy(self, *args): # precisa entrar no glade e linkar (exatamente) o nome da função no 'Handler' da parte Signals
        Gtk.main_quit()
        
    def b1_pressionado(self, button):
        global builder #para ele ficar visível
        
        text = builder.get_object("nome").get_text() # metodo get text
        
        print(f"Oi {text}")
        
builder = Gtk.Builder()
builder.add_from_file("./aula12/teste1.glade")

#conectando os sinais
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()
        