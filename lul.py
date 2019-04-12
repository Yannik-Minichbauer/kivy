from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

class RootWidget(BoxLayout):

     def __init__(self, **kwargs):
         super(RootWidget, self).__init__(**kwargs)
      
         self.status = Button(text='Status: es ist Frieden')
         self.add_widget(self.status)
         #self.status.bind(on_press = self.atomkrieg)
         cb = CustomBtn()
         cb.bind(pressed=self.btn_pressed)
         self.add_widget(cb)
         self.suizid= Button(text='Suizid')
         self.add_widget(self.suizid)
         self.suizid.bind(on_press = self.suizid2)
         self.add_widget(Button(text='btn 2'))
         self.krieg = Button(text='Atomkrieg!')
         self.add_widget(self.krieg)
         self.krieg.bind(on_press = self.atomkrieg)


     def btn_pressed(self, instance, pos):
         print ('pos: printed from root widget: {pos}'.format(pos=pos))

     def atomkrieg(self, instance):
         print("Bummmmmmmm!")
         self.status.text="Es ist finster"
         
     def suizid2(self, instance):
         self.status.text="RIP Erde"
         
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
