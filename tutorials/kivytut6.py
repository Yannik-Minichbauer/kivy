# ---------- KIVYTUT6.PY ----------
 
import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
 
# A page layout is used to create multi-page layouts
# that you can flip through
 
class PageLayoutApp(App):
 
    def build(self):
        return PageLayout()
 
plApp = PageLayoutApp()
 
plApp.run()
