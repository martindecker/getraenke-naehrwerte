import kivy 
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView

   
kivy.require('1.11.1')   
  
class MyFirstKivyApp(App): 
     def build(self): 
        return Label(text ="Still no List displayed.")           
  
print("begin gui")
MyFirstKivyApp().run()  
print("end gui")

