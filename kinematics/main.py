from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.graphics.context_instructions import PushMatrix, PopMatrix, Rotate
from kivy.graphics import Color
from kivy.graphics import Ellipse
from kivy.lang import Builder
import math


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
    MAX_ANGLE = 85.0
    min_angle = 0.0
    MAX_VELOCITY = 10.0 #TODO -- assign me better
    MIN_VELOCITY = 2.0

    #How many times the simulator should draw the proj per second
    interval = 50

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.projectile = Projectile() # violates DI, but thats okay

    def update_height(self, text):
        try:
            if float(text) >= self.MAX_HEIGHT:
                self.height = self.MAX_HEIGHT
            else:
                self.height =  float(text)
            self.min_angle = self.height * -5 #TODO -- maybe make this like 10 or somehting
            self.update_angle(self.angle) #Ensure vector is above min angle even if height changes
            self.projectile.y_pos = self.height / 10
            self.window.draw_platform(self.height)
        except:
            print('maybe dont do bad types')
    
    def update_angle(self, text):
        try:
            if float(text) >= self.MAX_ANGLE:
                self.angle = self.MAX_ANGLE
            elif float(text) <= self.min_angle:
                self.angle = self.min_angle
            else:
                self.angle = float(text)
            self.window.rotate_vector(self.angle)
        except:
            print('angle bruh')

    def update_velocity(self, text):
        try:
            if float(text) >= self.MAX_VELOCITY:
                self.initial_velocity = self.MAX_VELOCITY
            elif float(text) <= self.MIN_VELOCITY:
                self.initial_velocity = self.MIN_VELOCITY
            else:  
                self.initial_velocity = float(text)
            self.window.resize_vector(self.initial_velocity)
        except:
            print('numbers or something')


    def start_sim(self):
        #Set the velocity value based on the final values the user inputs
        rad = (self.angle * math.pi) / 180
        self.projectile.x_velocity = self.initial_velocity * math.cos(rad) / self.interval
        self.projectile.y_velocity = self.initial_velocity * math.sin(rad) / self.interval
        Clock.schedule_interval(self.run_sim_logic, 0.05)


    #Func to be called only when the simualator starts
    #Every time its called, update the velocity and position based on given vals
    def run_sim_logic(self, dt):
        self.projectile.y_velocity += self.projectile.y_acceleration
        self.projectile.y_pos += self.projectile.y_velocity
        self.projectile.x_pos += self.projectile.x_velocity
        
        x = self.projectile.x_pos
        y = self.projectile.y_pos
        self.window.move_proj(x, y)

        if self.projectile.y_pos < 0.0:
            print('sim ended...')
            self.window.move_proj(x, 0)
            return False

    def reset(self):
        #restore to defaults
        self.projectile = Projectile() #violates DI again, but its fine
        self.window.move_proj(0.065, 0, sim_start=False)
        self.window.draw_platform(0)
        self.window.rotate_vector(0)


    #'Inject' the projectile dependency into the window class
    #TODO -- find a way to call this on widget load, ignore me for now
    def on_load(self):
        self.ids.sim_window.projectile = self.projectile
    

#Widget where the drawing/actual simulation will take place
class SimulatorWindow(FloatLayout):
    projectile_img = ObjectProperty(None) #These should really be instance vars, but its fine
    vector = ObjectProperty(None)
    platform = ObjectProperty(None)
    def draw_platform(self, height):
        height = height / 10
        self.platform.size_hint[1] = height
        self.vector.pos_hint['y'] = height + 0.015 #Vector is slightly higher than projectile
        self.projectile_img.pos_hint['y'] = height

    def rotate_vector(self, angle):
       self.vector.angle = angle

    def resize_vector(self, size):
        size = size / 50
        self.vector.size_hint[0] = size

    def move_proj(self, x_pos, y_pos, sim_start=True):
        if sim_start:
            self.vector.opacity = 0
        else:
            self.vector.opacity = 1
        self.projectile_img.pos_hint = {'x': x_pos, 'y': y_pos}

        

#Class containing information about the projectile to be launched, such as velocity, position, etc
class Projectile:
    def __init__(self): #TODO-- update these values to fit better with the GUI representation of projectile
        self.x_pos = 0.065 #TODO -- make this normz2
        self.x_velocity = 0

        self.y_pos = 0.0
        self.y_velocity = 0
        #self.y_acceleration = -0.981
        self.y_acceleration = -9.81 / 500


if __name__=='__main__':
    KinematicsApp().run()