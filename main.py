from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class MainScreen(BoxLayout):
    pass

class MyApp(MDApp):
    def build(self):
        Builder.load_file("vista.kv")
        return MainScreen()
 
if __name__ == "__main__":
    MyApp().run()
