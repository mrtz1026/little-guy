import gi
import cairo
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk 

Gtk.init()
window = Gtk.Window()
window.fullscreen()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
window.set_app_paintable(True)
screen = window.get_screen()
visual = screen.get_rgba_visual()
window.set_visual(visual)
def make_click_through(window):
    region = cairo.Region()          
    window.input_shape_combine_region(region)
make_click_through(window)
Gtk.main()