# ---------- KIVYTUT5.PY ----------
 
import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
 
# A stack layout arranges widgets vertically or horizontally
# as they best fit
 
class StackLayoutApp(App):
 
    def build(self):
        return StackLayout()
 
slApp = StackLayoutApp()
 
slApp.run()
