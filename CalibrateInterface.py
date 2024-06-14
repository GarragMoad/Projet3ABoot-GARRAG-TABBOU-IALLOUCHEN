from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit
from PyQt6.QtGui import QColor
import sys
from martypy import Marty


class calibrateWindow(QMainWindow):
    def __init__(self , marty , interface):
        super().__init__()
        self.my_marty=marty
        self.interface=interface
        self.setWindowTitle("Interface avec Boutons ColorÃ©s")

        layout = QVBoxLayout()
        

        # Liste des couleurs et des noms des boutons
        couleurs = [
            ("Bleu", "blue"),
            ("Rouge", "red"),
            ("Vert", "green"),
            ("Jaune", "yellow"),
            ("Blue Marin", "navy"),
            ("Rose", "pink"),
            ("Noir","black")
        ]


        for nom, couleur in couleurs:
            bouton = QPushButton(nom)
            bouton.setStyleSheet(f"background-color: {couleur};")
            bouton.clicked.connect(lambda _, clr=(nom): self.bouton_clique(clr))
            layout.addWidget(bouton)

        # Label pour afficher les informations de la couleur sÃ©lectionnÃ©e
        self.label_infos = QLabel("Aucune couleur sÃ©lectionnÃ©e")
        layout.addWidget(self.label_infos)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def bouton_clique(self, nom):
        hex_code =self.my_marty.get_color_sensor_hex("left")
        infos = f"Couleur sÃ©lectionnÃ©e: {nom}\nCode Hex: {hex_code}"
        self.label_infos.setText(infos)
        self.interface.displayColor(nom,hex_code)

    def envoyer_couleur_a_marty(self, nom, hex_code):
        
        print(f"Envoi de la couleur {hex_code} pour {nom} au robot Marty")


# if __name__ == "__main__":
#     app = QApplication([])
#     main_window = calibrateWindow()
#     main_window.show()
#     sys.exit(app.exec())
