import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QSlider, QDialog, QLineEdit
from PyQt6.QtGui import QPixmap, QIcon
from martypy import Marty
from CalibrateInterface import calibrateWindow

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
        self.CouleursList = {
        'Bleu': '#0000FF',          # Bleu
        'Rouge': '#FF0000',         # Rouge
        'Vert': '#008000',          # Vert
        'Jaune': '#FFFF00',         # Jaune         # Noir
        'Blue Marin': '#000080',    # Bleu Marine
        'Rose': '#FFC0CB',   
        'Noir':'#000000'       # Rose
    }
        
        self.couleurCalibrateNom="BLANC"
        self.valeurCouleurCaibrate="0"
        self.ip_address = ip_address
        self.RobotCalibrate=0
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
        tourner_button = QPushButton("couleurs")
        calibrer = QPushButton("calibrer couleurs")
        labyrinte = QPushButton("labyrinte")
        #verif=QPushButton("Verifier")

        avancer_button.setIcon(QIcon('avancer.png'))
        reculer_button.setIcon(QIcon('reculer.png'))
        tourner_button.setIcon(QIcon('tourner.png'))

        avancer_button.clicked.connect(self.avancer)
        reculer_button.clicked.connect(self.reculer)
        tourner_button.clicked.connect(self.getCouleurs)
        calibrer.clicked.connect(self.showCalibrateInterface)
        labyrinte.clicked.connect(self.detectColor)
        #verif.clicked.connect(self.detectC)

        # Add direction buttons to layout
        control_layout.addWidget(avancer_button, 0, 2)
        control_layout.addWidget(reculer_button, 0, 0)
        control_layout.addWidget(tourner_button, 0, 1)
        control_layout.addWidget(calibrer)
        control_layout.addWidget(labyrinte)
        #control_layout.addWidget(verif)


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
    
    def getCouleur(self):
        return self.my_marty.get_color_sensor_hex("left")

    def getCouleurs(self):
        print(self.CouleursList)

    def showCalibrateInterface (self):
        windowcalbirate = calibrateWindow(self.my_marty ,self)
        windowcalbirate.show()

    def displayColor(self , couleur, valeur, robot):
          print(couleur,valeur, robot)
          self.RobotCalibrate=robot
          self.CouleursList[couleur] = valeur

    def hex_to_rgb(self, hex_color):
        if hex_color is None:
            raise ValueError("Invalid color: None")
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(self, rgb_color):
        return '#{:02x}{:02x}{:02x}'.format(*rgb_color)

    def clamp(self, value, min_value=0, max_value=255):
        return max(min_value, min(value, max_value))

    def create_color_interval(self, hex_color, delta):
        r, g, b = self.hex_to_rgb(hex_color)
        
        r_min = self.clamp(r - delta)
        r_max = self.clamp(r + delta)
        g_min = self.clamp(g - delta)
        g_max = self.clamp(g + delta)
        b_min = self.clamp(b - delta)
        b_max = self.clamp(b + delta)
        
        min_color = self.rgb_to_hex((r_min, g_min, b_min))
        max_color = self.rgb_to_hex((r_max, g_max, b_max))
        
        return (min_color, max_color)

    def create_intervals(self):
        intervals = {}
        for color_name, hex_color in self.CouleursList.items():
                 intervals[color_name] = self.create_color_interval(hex_color, 10)
        return intervals

    def hex_in_interval(self, hex_color, interval):
        rgb = self.hex_to_rgb(hex_color)
        min_rgb = self.hex_to_rgb(interval[0])
        max_rgb = self.hex_to_rgb(interval[1])
        return all(min_rgb[i] <= rgb[i] <= max_rgb[i] for i in range(3))

    def color_in_intervals(self, hex_color, intervals):
        for color_name, interval in intervals.items():
            if self.hex_in_interval(hex_color, interval):
                return color_name
        return 'Jaune'

    def detectColor(self):
        intervals = self.create_intervals()
        #for color_name, interval in intervals.items():
            #print(f"Interval for {color_name}: {interval}")
        
        directions = []
        self.my_marty.stand_straight(1000, None)
        couleur = self.getCouleur()
        print("Couleur détectée",couleur)
        if couleur is None:
            raise ValueError("getCouleur returned None")
        detected_color = self.color_in_intervals(couleur, intervals)
        directions.append(detected_color)

        for _ in range(2):
            self.my_marty.walk(6, 'auto', 0, 35, 1500, None)
            self.my_marty.stand_straight(1000, None)
            couleur = self.getCouleur()
            print("Couleur détectée",couleur)
            if couleur is None:
                raise ValueError("getCouleur returned None")
            detected_color = self.color_in_intervals(couleur, intervals)
            directions.append(detected_color)

        self.my_marty.stand_straight(1000, None)
        self.my_marty.sidestep('right', 6, 35, 1000, None)
        couleur = self.getCouleur()
        print("Couleur détectée",couleur)
        if couleur is None:
            raise ValueError("getCouleur returned None")
        detected_color = self.color_in_intervals(couleur, intervals)
        directions.append(detected_color)

        for _ in range(2):
            self.my_marty.stand_straight(2000, None)
            self.my_marty.walk(6, 'auto', 0, -35, 1500, None)
            couleur = self.getCouleur()
            print("Couleur détectée",couleur)
            if couleur is None:
                raise ValueError("getCouleur returned None")
            detected_color = self.color_in_intervals(couleur, intervals)
            directions.append(detected_color)

        self.my_marty.stand_straight(2000, None)
        self.my_marty.sidestep('right', 6, 35, 1000, None)
        couleur = self.getCouleur()
        print("Couleur détectée",couleur)
        if couleur is None:
            raise ValueError("getCouleur returned None")
        detected_color = self.color_in_intervals(couleur, intervals)
        directions.append(detected_color)

        for _ in range(2):
            self.my_marty.stand_straight(2000, None)
            self.my_marty.walk(6, 'auto', 0, 35, 1500, None)
            couleur = self.getCouleur()
            print("Couleur détectée",couleur)
            if couleur is None:
                raise ValueError("getCouleur returned None")
            detected_color = self.color_in_intervals(couleur, intervals)
            directions.append(detected_color)
            self.my_marty.stand_straight(1000, None)

        print("chemin fini")
        print(directions)

    #def detectC(self):
        #intervals = self.create_intervals()
        #couleur = self.getCouleur()
        #detected_color = self.color_in_intervals(couleur, intervals)
        #print("Couleur détectée",detected_color)

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
