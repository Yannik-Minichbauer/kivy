from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.image import Image
import random


class Game():
    fragen = ["Putin's Wodkaflasche stehlen?",
              "Die Mauer errichten?", 
              "Fake News verbreiten?", 
              "Wresteln?"]

class RootWidget(BoxLayout):
    
         
         
    
     def __init__(self, **kwargs):
         super(RootWidget, self).__init__(**kwargs)
         
         self.atomic_war= 10
         self.status = Button(text='Status: Es ist Frieden Kriegschance: {}%'.format(self.atomic_war) )
         self.status.bind(on_press = self.next_question)
         self.add_widget(self.status)
         #self.status.bind(on_press = self.atomkrieg)
         #cb = CustomBtn()
         #cb.bind(pressed=self.btn_pressed)
         #self.add_widget(cb)
         
         self.ja = Button (text='Ja')
         self.add_widget(self.ja)
         self.ja.bind(on_press = self.bad_decision)
         self.nein = Button (text='Nein')
         self.add_widget(self.nein)
         self.nein.bind(on_press = self.good_decision)
        # self.suizid= Button(text='Suizid')
        # self.add_widget(self.suizid)
        # self.suizid.bind(on_press = self.suizid2)
        # #self.add_widget(Button(text='oof'))
        # self.krieg = Button(text='Atomkrieg!')
        # self.add_widget(self.krieg)
        # self.krieg.bind(on_press = self.atomkrieg)
        # self.frieden = Button(text='Frieden')
        # self.add_widget(self.frieden)
        # self.frieden.bind(on_press = self.weltfrieden)
         self.img = Image(source = 'data/planet_good.jpg')
         self.add_widget(self.img)
     
     def bad_decision(self, instance):
         self.atomic_war += random.randint(1,6)
         self.check_world()
         
         
     def good_decision(self, instance):
         self.atomic_war -= random.randint(1,3)
         self.check_world()
         
     def check_world(self):
         chance = random.random()
         print(chance)
         if chance * 100 < self.atomic_war:
             self.status.text = "Bummmmmm!"
             self.img.source="data/planet_nuclear.jpg"
         #if self.atomic_war 
         else:
             text='Status: Es ist Frieden Kriegschance: {}%'.format(self.atomic_war)
             text += "\n" + random.choice(Game.fragen)
             self.status.text = text

   
     def next_question(self, instance):
           text='Status: Es ist Frieden Kriegschance: {}%'.format(self.atomic_war)
           text += "\n" + random.choice(Game.fragen)
           self.status.text = text

     def btn_pressed(self, instance, pos):
         print ('pos: printed from root widget: {pos}'.format(pos=pos))

     def atomkrieg(self, instance):
         print("Bummmmmmmm!")
         self.status.text="Status: Es ist finster"
         self.img.source = 'data/planet_nuclear.jpg'
         
     def suizid2(self, instance):
         self.status.text="Status: RIP Erde"
         self.img.source = 'data/planet_dead.jpg'
         
     def weltfrieden(self, instance):
         self.status.text='Status: Es ist Frieden'
         self.img.source= 'data/planet_good.jpg'
         
class CustomBtn(Widget):

     pressed = ListProperty([0, 0])

     def on_touch_down(self, touch):
         if self.collide_point(*touch.pos):
             self.pressed = touch.pos
             # we consumed the touch. return False here to propagate
             # the touch further to the children.
             return True
         return super(CustomBtn, self).on_touch_down(touch)

     def on_pressed(self, instance, pos):
         print ('pressed at {pos}'.format(pos=pos))

class TestApp(App):

     def build(self):
         return RootWidget()


if __name__ == '__main__':
     TestApp().run()
