from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config


class MainScreen(BoxLayout):
    pass

class MyApp(MDApp):
    def build(self):
        # Opcional: Si estás en PC, fija la resolución para simular un móvil
        Window.size = (360, 640)  # Simula un celular en modo vertical
        Config.set('graphics', 'fullscreen', 'auto')  # Pantalla completa en móviles

        Builder.load_file("vista.kv")
        return MainScreen()
 
if __name__ == "__main__":
    MyApp().run()
