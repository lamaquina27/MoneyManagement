from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.config import Config
from kivy.properties import NumericProperty, ListProperty
class ManagerScreenStats(MDScreenManager):
    pass
class BaseScreen(MDScreen):
    pass
class Manager(MDScreenManager):
    pass
class InicioScreen(MDScreen):
    pass
class CunetaScreen(MDScreen):
    pass
class StatsScreen(MDScreen):
    selected_button = None  # Guardar el último botón seleccionado
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.seleccionar_boton_inicial, 0)

    def seleccionar_boton_inicial(self, dt):
        self.selected_button = self.ids.get("btnStats")
        if self.selected_button:
            self.cambiar_color_boton(self.selected_button, (1, 1, 1, 0.7))  # Blanco semitransparente

    def seleccion(self, bid):
        boton = self.ids.get(bid)
        
        # Restaurar el color del botón previamente seleccionado
        if self.selected_button:
            self.cambiar_color_boton(self.selected_button, (0, 0, 0, 0))  # Transparente

        # Cambiar color del botón seleccionado
        if boton:
            self.cambiar_color_boton(boton, (1, 1, 1, 0.7))  # Blanco semitransparente

        # Actualizar el botón seleccionado
        self.selected_button = boton

    def cambiar_color_boton(self, boton, color):
        """Cambia el color de fondo del `canvas.before` del botón."""
        boton.canvas.before.children[0].rgba = color  # Modifica el color dinámicamente

        
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
    def change_screen(self, screen_name):
        self.root.ids.manager.current = screen_name
        
 
if __name__ == "__main__":
    MyApp().run()
