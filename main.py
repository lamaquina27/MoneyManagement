from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
class Manager(ScreenManager):
    pass
class StatsScreen(Screen):
    pass
class PieApp(MDBoxLayout):
    pass
class MainLayout(MDBoxLayout):
    pass

class MyApp(MDApp):
    def build(self):
        # Opcional: Si estás en PC, fija la resolución para simular un móvil
        Window.size = (360, 640)  # Simula un celular en modo vertical
        Config.set('graphics', 'fullscreen', 'auto')  # Pantalla completa en móviles

        Builder.load_file("vista.kv")
        return MainLayout()
 
if __name__ == "__main__":
    MyApp().run()
