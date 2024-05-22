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

    
    def tourner(self):
        self.my_marty.walk(9,'auto',-10,25,1500)

    def reculer(self):
        self.my_marty.walk(2,'auto',-10,-25,1500)
    
    def avancer(self):
        self.my_marty.walk(2)

    def danser(self):
        self.my_marty.dance()
    
    def celebrer(self):
        self.my_marty.celebrate()
    
    def be_happy(self):
        self.my_marty.eyes('excited')
    
    def be_sad(self):
        self.my_marty.eyes('angry')
    
        
        
    


