import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QSlider, QDialog, QLineEdit
from PyQt6.QtGui import QPixmap, QIcon
from martypy import Marty

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Login')
        self.setStyleSheet("background-color: lightblue;")

        layout = QVBoxLayout()

        # EntÃªte
        header_label = QLabel("ROBOT MARTY")
        layout.addWidget(header_label)

        # Affichage de l'image avec des dimensions personnalisÃ©es
        image_label = QLabel()
        pixmap = QPixmap('image_login.jpg').scaled(200, 200)  # Redimensionner l'image Ã  200x200 pixels
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)

        # Label et champ de saisie pour l'adresse IP
        self.ip_label = QLabel('Enter Robot IP Address:')
        self.ip_input = QLineEdit()

        layout.addWidget(self.ip_label)
        layout.addWidget(self.ip_input)

        # Bouton de connexion
        self.login_button = QPushButton('Connexion')
        self.login_button.clicked.connect(self.handle_login)

        layout.addWidget(self.login_button)
        self.setLayout(layout)

        # DÃ©finir la couleur de fond en bleu clair
        self.setStyleSheet("background-color: lightblue;")

    def handle_login(self):
        ip_address = self.ip_input.text()
        if ip_address:
            print(f"IP Address entered: {ip_address}")  # Afficher l'adresse IP dans la console
            self.accept()
        else:
            self.ip_label.setText('Please enter a valid IP address')


class RobotInterface(QWidget):
    
    def __init__(self, ip_address):
        super().__init__()
        self.ip_address = ip_address
        print(self.ip_address)
        self.my_marty=Marty("wifi",self.ip_address)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Robot Control Interface')
        self.setStyleSheet("background-color: lightblue;")

        # Layouts
        main_layout = QVBoxLayout()  # Modifier pour un layout vertical
        battery_layout = QHBoxLayout()  # Ajout d'un layout horizontal pour la batterie
        control_layout = QGridLayout()
        action_layout = QGridLayout()

        # Battery level indicator
        battery_label = QLabel("Battery Level: 100%")  # CrÃ©er un label pour afficher le niveau de batterie
        battery_layout.addWidget(battery_label)  # Ajouter le label au layout

        # Direction buttons
        avancer_button = QPushButton("avancer")
        reculer_button = QPushButton("reculer")
        tourner_button = QPushButton("tourner")

        avancer_button.setIcon(QIcon('avancer.png'))
        reculer_button.setIcon(QIcon('reculer.png'))
        tourner_button.setIcon(QIcon('tourner.png'))

        avancer_button.clicked.connect(self.avancer)
        reculer_button.clicked.connect(self.reculer)
        tourner_button.clicked.connect(self.tourner)

        # Add direction buttons to layout
        control_layout.addWidget(avancer_button, 0, 2)
        control_layout.addWidget(reculer_button, 0, 0)
        control_layout.addWidget(tourner_button, 0, 1)

        # Action buttons with images
        actions = [
            ('Get Ready', 'get_ready.png', self.stand_right),
            ('Pas chassé D', 'show_off.png',self.pas_chasseD),
            ('pas chassé G', 'wave_left.png',self.pas_chasseL),
            ('danser', 'wave_right.png',self.danser),
            ('celebrer!', 'dance.png',self.celebrer),
            ('be_happy', 'wiggle_eyes.png',self.be_happy),
            ('be sad', 'kick_left.png',self.be_sad),
            ('obstacle', 'kick_right.png',self.obstacle),
        ]

        for i, (label, img_file,function) in enumerate(actions):
            button = QPushButton()
            button.setIcon(QIcon(img_file))
            button.setIconSize(QPixmap(img_file).scaled(64, 64).size())
            action_layout.addWidget(button, i // 4, i % 4)
            button.setToolTip(label)
            button.clicked.connect(function)

        # Add control and action layouts to main layout
        main_layout.addLayout(battery_layout)  # Ajouter le layout de la batterie
        main_layout.addLayout(control_layout)
        main_layout.addLayout(action_layout)

        self.setLayout(main_layout)

    def danser(self):
            self.my_marty.dance()

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

def main():
    app = QApplication(sys.argv)

    login = LoginWindow()
    if login.exec() == QDialog.DialogCode.Accepted:
        ip_address = login.ip_input.text()
        window = RobotInterface(ip_address)
        window.show()
        sys.exit(app.exec())

if __name__ == '__main__':
    main()
