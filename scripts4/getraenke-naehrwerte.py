import kivy 
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
   
kivy.require('1.11.1')   
  
class MyFirstKivyApp(App): 
     def build(self): 
        return Label(text ="Program is still empty.")           
  
print("begin gui")
MyFirstKivyApp().run()  
print("end gui")

