 
# ---------- KIVYTUT3.PY ----------
 
import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
 
# The Grid Layout organizes everything in a grid pattern
 
class GridLayoutApp(App):
 
    def build(self):
        return GridLayout()
 
glApp = GridLayoutApp()
 
glApp.run()
