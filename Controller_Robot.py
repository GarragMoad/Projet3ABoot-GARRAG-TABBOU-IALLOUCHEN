from typing import Union
from martypy import Marty
from collections import OrderedDict
class Control_Base():
    my_marty=None
    red=0
    blue=0
    green=0

 

    # Initialisation du dictionnaire avec des listes vides
    couleurs = OrderedDict({
        'red': [],
        'green': [],
        'blue': [],
        'yellow': [],
        'purple': []
    })

 



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
    
    def get_battery(self):
        return self.my_marty.get_battery_remaining()
    
    def obstacle(self):
        return self.my_marty.foot_obstacle_sensed('right')
    
    def testCouleur(self):
        self.red=self.my_marty.get_color_sensor_value_by_channel("left","red")
        self.blue=self.my_marty.get_color_sensor_value_by_channel("left","blue")
        self.green=self.my_marty.get_color_sensor_value_by_channel("left","green")
        print(self.red)
        print(self.blue)
        print(self.green)


    def couleur_ajust(self):
        self.testCouleur()
        for couleur, valeurs in self.couleurs.items():
            if (self.red > valeurs[0] and self.red < valeurs[0]) and (self.green > valeurs[1] and self.green < valeurs[1]) and (self.blue > valeurs[2] and self.blue < valeurs[2]):
                print(couleur, valeurs)
                return couleur
        print("couleur non reconnue")



