
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Seleciona os componentes gráficos
win = Gtk.Window()


# Conecta os sinais do usuário
win.connect("destroy", Gtk.main_quit) # faz com que o 'X' encerre o programa


# Mostra os componentes de interesse
win.show_all()

# Entra no loop de execução
Gtk.main()