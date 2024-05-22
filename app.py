import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from Controller_Robot import Control_Base

class IHM(QWidget):
    Robot_controll=None

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Robot Controller")

        self.connect_button = QPushButton("Connecter")
        self.connect_button.clicked.connect(self.connect_to_robot)

        self.disconnect_button = QPushButton("tourner")
        self.disconnect_button.clicked.connect(self.tourner)

        self.reculer_button= QPushButton("reculer")
        self.reculer_button.clicked.connect(self.reculer)

        self.avancer_button=QPushButton("avancer")
        self.avancer_button.clicked.connect(self.avancer)

        self.celebrer_button=QPushButton("celebrer")
        self.celebrer_button.clicked.connect(self.celebrer)

        self.danser_button=QPushButton("danser")
        self.danser_button.clicked.connect(self.danser)

        self.be_happy_bouton=QPushButton("Be_happy")
        self.be_happy_bouton.clicked.connect(self.be_happy)

        self.be_sad_button=QPushButton("Be_sad")
        self.be_sad_button.clicked.connect(self.be_sad)



        layout = QVBoxLayout()
        layout.addWidget(self.connect_button)
        layout.addWidget(self.disconnect_button)
        layout.addWidget(self.reculer_button)
        layout.addWidget(self.avancer_button)
        layout.addWidget(self.celebrer_button)
        layout.addWidget(self.danser_button)
        layout.addWidget(self.be_happy_bouton)
        layout.addWidget(self.be_sad_button)

        self.setLayout(layout)


    def connect_to_robot(self):
        try:
            self.Robot_controll=Control_Base("192.168.0.112")
            self.Robot_controll.avancer()
        except Exception as e:
            print("Erreur lors de la connexion au robot Marty:", e)

    def disconnect_from_robot(self):
        try:
            self.connect_button.setEnabled(True)
            self.disconnect_button.setEnabled(False)
            print("Déconnexion du robot Marty.")
        except Exception as e:
            print("Erreur lors de la déconnexion du robot Marty:", e)

    def tourner(self):
        try:
            self.Robot_controll.tourner()
        except Exception as e:
            print("Erreur dans la fonction tourner:", e)

    def reculer(self):
        try:
            self.Robot_controll.reculer()
        except Exception as e:
            print("Erreur dans la fonction tourner:", e)
    
    def avancer(self):
        try:
            self.Robot_controll.avancer()
        except Exception as e:
            print("Erreur dans la fonction tourner:", e)

    def celebrer(self):
        try:
            self.Robot_controll.celebrer()
        except Exception as e:
            print("Erreur dans la fonction tourner:", e)

    def danser(self):
        try:
            self.Robot_controll.danser()
        except Exception as e:
            print("Erreur dans la fonction tourner:", e)

    def be_happy(self):
        try:
            self.Robot_controll.be_happy()
        except Exception as e:
            print("Erreur dans la fonction tourner:", e)

    def be_sad(self):
        try:
            self.Robot_controll.be_sad()
        except Exception as e:
            print("Erreur dans la fonction tourner:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = IHM()
    controller.show()
    app.exec()
