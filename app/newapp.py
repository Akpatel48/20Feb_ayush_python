import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from  kivy.uix.textinput import TextInput
from  kivy.uix.button import Button

class childapp(GridLayout):
    def __init__(self,**kwargs):
        super(childapp,self).__init__()
        self.cols=2
        self.add_widget(Label(text='student name'))
        self.s_name=TextInput()
        self.add_widget(self.s_name)
class pa(App):
    def build(self):
        return childapp()

if __name__=='__main__':
    pa().run()