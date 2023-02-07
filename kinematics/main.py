from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.graphics import Color
from kivy.graphics import Ellipse
from kivy.lang import Builder

#Base application class
class KinematicsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    #Setting our root widget 
    def build(self):
        self.root = Builder.load_file('kinematics-sim.kv')


#Main class containing info about the simulation, such as height, angle, etc
class Simulator(Widget):
    height = 0.0
    angle = 0.0
    initial_velocity = 0.0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.projectile = Projectile() # violates DI, but thats okay

    def update_height(self, text):
        self.height = float(text)




    #'Inject' the projectile dependency into the window class
    #TODO -- find a way to call this on widget load, ignore me for now
    def on_load(self):
        self.ids.sim_window.projectile = self.projectile
    

#Widget where the drawing/actual simulation will take place
class SimulatorWindow(FloatLayout):
    platform = ObjectProperty(None)
        

#Class containing information about the projectile to be launched, such as velocity, position, etc
class Projectile:
    def __init__(self): #TODO-- update these values to fit better with the GUI representation of projectile
        self.x_pos = 100 #TODO --
        self.x_velocity = 0

        self.y_pos = 100
        self.y_velocity = 0
        self.y_acceleration = 9.81



if __name__=='__main__':
    KinematicsApp().run()