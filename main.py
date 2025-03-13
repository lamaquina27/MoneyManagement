from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.properties import NumericProperty, ListProperty
class Manager(ScreenManager):
    pass
class StatsScreen(Screen):
    pass
class PieApp(MDBoxLayout):
    
    # Propiedades para la barra de selección
    indicator_pos = NumericProperty(0)  # Posición de la barra (0 = izquierda, 1 = centro, 2 = derecha)
    indicator_color = ListProperty([0, 0, 0, 0])  # Color de la barra (inicialmente invisible)

    def select_tab(self, tab_name):
        self.current_tab = tab_name

        # Determinar la posición de la barra de selección
        if self.current_tab == "detalles":
            self.indicator_pos = 0
        elif self.current_tab == "stats":
            self.indicator_pos = 1
        elif self.current_tab == "gastos":
            self.indicator_pos = 2

        # Activar la barra con color blanco
        self.indicator_color = [0,0,0, 1]
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
