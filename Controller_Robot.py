from typing import Union
from martypy import Marty
class Control_Base():
    my_marty=None

    def __init__(self,addIp):
        self.connect(addIp)

    def connect(self, addIp):
        self.my_marty= Marty("wifi",addIp)
        
    def danser(self):
        try:
            self.my_marty.dance()
        except Exception as e:
            print("Erreur dans la fonction danser:", e)

    def disconnect_from_robot(self):
        try:
            print("Déconnexion du robot Marty.")
        except Exception as e:
            print("Erreur lors de la déconnexion du robot Marty:", e)
    def stand_right(self):
        self.my_marty.stand_straight()
    
    def tourner(self):
        self.my_marty.walk(9,'auto',-10,25,1500)

    def reculer(self):
        self.my_marty.walk(2,'auto',-10,-25,1500)
    
    def avancer(self):
        self.my_marty.walk(2)

    def pas_chasseD(self):
        self.my_marty.sidestep('right',11,40,900,None)

    def pas_chasseL(self):
        self.my_marty.sidestep('left',11,40,900,None)

    def danser(self):
        self.my_marty.dance()
    
    def celebrer(self):
        self.my_marty.celebrate()
    
    def be_happy(self):
        self.my_marty.eyes('excited')
    
    def be_sad(self):
        self.my_marty.eyes('angry')
    
    # def get_distance(self):
    #     return self.my_marty.get_distance_sensor()
    
    def get_battery(self):
        return self.my_marty.get_battery_remaining()
    
    def obstacle(self):
        return self.my_marty.foot_obstacle_sensed('right')
    
    def couleur(self):
        # return self.my_marty.get_ground_sensor_reading('left')
        red=self.my_marty.get_color_sensor_value_by_channel("left","red")
        blue=self.my_marty.get_color_sensor_value_by_channel("left","blue")
        green=self.my_marty.get_color_sensor_value_by_channel("left","green")
        print(red)
        print(blue)
        print(green)
        if(red>63 and red <68) and (green>56 and green <62) and(blue>86 and blue<92):
            print("blue")
            return("blue")
        if(red>165 and red<171) and (green>25 and green <27.5) and(blue>39 and blue<42):
            print("red")
            return ("red")
        if(red>190 and red <198) and (green>93 and green <95) and(blue>65 and blue< 68):
            print("yellow")
            return("yellow")
        if(red>58 and red <62) and (green>41 and green <44.5) and(blue>32 and blue<36):
            print("green")
            return("green")
        if(red>51 and red <57) and (green>25 and green <30) and(blue>44 and blue<49):
            print("blue")
            return("blue")
        else :
            print("couleur non reconnue")


