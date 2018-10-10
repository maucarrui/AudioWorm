import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
from gi.repository.GdkPixbuf import Pixbuf

class SearchWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Busqueda")
        self.set_border_width(10)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.page1 = Gtk.ListBox()
        self.page1.set_border_width(10)

        self.general_entry = Gtk.Entry()
        self.general_entry.set_placeholder_text('Artist: A1. Song: S1.')

        self.search_button = Gtk.Button('Search')
        self.search_button_adv = Gtk.Button('Search')

        self.labels = [Gtk.Label('General Search'),
                       Gtk.Label('Advanced Search'),
                       Gtk.Label('Performer'),
                       Gtk.Label('Album'),
                       Gtk.Label('Song')]

        self.page1.add(self.labels[0])
        self.page1.add(self.general_entry)
        self.page1.add(self.search_button)

        self.notebook.append_page(self.page1, Gtk.Label('General'))

        self.page2 = Gtk.ListBox()
        self.page2.set_border_width(10)

        self.performer_entry = Gtk.Entry()
        self.album_entry = Gtk.Entry()
        self.song_entry = Gtk.Entry()

        self.page2.add(Gtk.Label('Busqueda Avanzada'))
        self.page2.add(Gtk.Label('Artista/Grupo'))
        self.page2.add(self.performer_entry)
        self.page2.add(Gtk.Label('Album'))
        self.page2.add(self.album_entry)
        self.page2.add(Gtk.Label('Rola'))
        self.page2.add(self.song_entry)
        self.page2.add(self.search_button_adv)

        self.notebook.append_page(self.page2, Gtk.Label('Avanzada'))

        self.show_all()
