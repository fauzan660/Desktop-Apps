import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button




class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        
        self.cols = 1
        
        self.topgrid = GridLayout()
        self.topgrid.cols =2
        
        
        self.topgrid.add_widget(Label(text= "Name"))
        self.name = TextInput(multiline=False)
        self.topgrid.add_widget(self.name)
        
        
        self.topgrid.add_widget(Label(text= "Favourite Food"))
        self.food = TextInput(multiline=False)
        self.topgrid.add_widget(self.food)
        
        
        self.topgrid.add_widget(Label(text= "Favourite Car"))
        self.car = TextInput(multiline=False)
        self.topgrid.add_widget(self.car)
        
        self.add_widget(self.topgrid)
        
        
        self.submit = Button(text="Submit",
                             font_size= 20,
                             size_hint_y=None,
                             height = 100,
                             size_hint_x = None,
                             width= 200)
        
        self.submit.bind(on_press= self.press)
        self.add_widget(self.submit)



    def press(self, instance):
        name = self.name.text
        food = self.food.text
        car = self.car.text
        
        self.add_widget(Label(text=f"{name} likes to eat {food} and likes to ride in a {car}"))
            
        self.name.text = ""
        self.food.text = ""
        self.car.text= ""    
            
            
class MyApp(App):
    def build(self):
        return MyGridLayout()
    
    
if __name__ == "__main__":
    MyApp().run()