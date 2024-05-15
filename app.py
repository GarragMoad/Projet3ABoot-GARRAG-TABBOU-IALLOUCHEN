import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import socket
from martypy import Marty
import Controller_Robot

class IHM(QWidget):
    Robot_controll=Controller_Robot()

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Robot Controller")

        self.connect_button = QPushButton("Connecter")
        self.connect_button.clicked.connect(self.connect_to_robot)

        self.disconnect_button = QPushButton("Déconnecter")
        self.disconnect_button.clicked.connect(self.disconnect_from_robot)
        self.disconnect_button.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.connect_button)
        layout.addWidget(self.disconnect_button)

        self.setLayout(layout)

    
    def connect_to_robot(self):
        try:
            print("Connexion établie avec le robot Marty.")
            self.Robot_controll.connect_to_robot()
        except Exception as e:
            print("Erreur lors de la connexion au robot Marty:", e)

    def disconnect_from_robot(self):
        try:
            self.connect_button.setEnabled(True)
            self.disconnect_button.setEnabled(False)
            print("Déconnexion du robot Marty.")
        except Exception as e:
            print("Erreur lors de la déconnexion du robot Marty:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = IHM()
    controller.show()
    app.exec()
