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
import re

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

    MAX_HEIGHT = 8.0
    max_angle = 85.0
    min_angle = 0.0
    MAX_VELOCITY = 0.0 #TODO -- assign me


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.projectile = Projectile() # violates DI, but thats okay


    def update_height(self, text):
        try:
            if float(text) >= self.MAX_HEIGHT:
                self.height = self.MAX_HEIGHT
            else:
                self.height =  float(text)
            self.projectile.y_pos = self.height
            self.window.draw_platform(self.height)
        except:
            print('maybe dont do bad types')




    #'Inject' the projectile dependency into the window class
    #TODO -- find a way to call this on widget load, ignore me for now
    def on_load(self):
        self.ids.sim_window.projectile = self.projectile
    

#Widget where the drawing/actual simulation will take place
class SimulatorWindow(FloatLayout):
    platform = ObjectProperty(None)
    projectile_img = ObjectProperty(None)
    def draw_platform(self, height):
        height = height / 10
        self.platform.size_hint[1] = height
        self.projectile_img.pos_hint['y'] = height
        

#Class containing information about the projectile to be launched, such as velocity, position, etc
class Projectile:
    def __init__(self): #TODO-- update these values to fit better with the GUI representation of projectile
        self.x_pos = 100 #TODO -- make this normz2
        self.x_velocity = 0

        self.y_pos = 0.0
        self.y_velocity = 0
        self.y_acceleration = 9.81



if __name__=='__main__':
    KinematicsApp().run()