from martypy import Marty
class Controller_Robot:
    my_marty = Marty("wifi","192.168.0.100")

    def __init__(self):
        self.connect_to_robot()
    
    def connect_to_robot(self):
        try:
            print("Connexion établie avec le robot Marty.")
            self.danser()
        except Exception as e:
            print("Erreur lors de la connexion au robot Marty:", e)

    def disconnect_from_robot(self):
        try:
            print("Déconnexion du robot Marty.")
        except Exception as e:
            print("Erreur lors de la déconnexion du robot Marty:", e)

    def danser(self):
        self.my_marty.dance()