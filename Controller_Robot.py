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

    #fonction qui prend en param le sens de rotation
    def tourner(self,position):
        self.my_marty.dance(position,3000)
    
    def avancer(self):
        self.my_marty.walk(2)
        
    


