import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QSlider, QDialog, QLineEdit
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
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
        self.ip_label1 = QLabel('Enter Robot1 IP Address:')
        self.ip_input1 = QLineEdit()

        self.ip_label2 = QLabel('Enter Robot2 IP Address:')
        self.ip_input2 = QLineEdit()

        layout.addWidget(self.ip_label1)
        layout.addWidget(self.ip_input1)
        layout.addWidget(self.ip_label2)
        layout.addWidget(self.ip_input2)

        # Bouton de connexion
        self.login_button = QPushButton('Connexion')
        self.login_button.clicked.connect(self.handle_login)

        layout.addWidget(self.login_button)
        self.setLayout(layout)

        # DÃ©finir la couleur de fond en bleu clair
        self.setStyleSheet("background-color: lightblue;")

    def handle_login(self):
        ip_address1 = self.ip_input1.text()
        ip_address2 = self.ip_input2.text()
        if ip_address1 and ip_address2:
            print(f"IP Address1 entered: {ip_address1}") 
            print(f"IP Address1 entered: {ip_address2}") # Afficher l'adresse IP dans la console
            self.accept()
        else:
            self.ip_label.setText('Please enter a valid IP address')


class RobotInterface(QWidget):
    
    def __init__(self, ip_address1,ip_address2):
        super().__init__()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFocus()
        self.directionsfusionner=[]
        self.CouleursList1 = {
        'Bleu': '#0000FF',          # Bleu
        'Rouge': '#FF0000',         # Rouge
        'Vert': '#008000',          # Vert
        'Jaune': '#FFFF00',         # Jaune         # Noir
        'Blue Marin': '#000080',    # Bleu Marine
        'Rose': '#FFC0CB',   
        'Noir':'#000000'       # Rose
    }
        self.CouleursList2 = {
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
        self.ip_address1 = ip_address1
        self.ip_address2 = ip_address2
        self.my_marty=Marty("wifi",self.ip_address1)
        self.marty=Marty("wifi",self.ip_address2)
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
        avancer_button = QPushButton()
        reculer_button = QPushButton()
        tourner_button = QPushButton()
        calibrer = QPushButton("calibrer couleurs")
        labyrinte = QPushButton("labyrinte")
        self.robot = QLabel('Enter le numéro du robot à qualibrer:')
        self.RobotCalibrate = QLineEdit()
        verif1=QPushButton("Verifier1")
        verif2=QPushButton("ListsFusionner")

        avancer_button.setIcon(QIcon('./img/avancer.png'))
        reculer_button.setIcon(QIcon('./img/reculer.png'))
        tourner_button.setIcon(QIcon('./img/tourner.png'))

        avancer_button.clicked.connect(self.avancer)
        reculer_button.clicked.connect(self.reculer)
        tourner_button.clicked.connect(self.tourner)
        calibrer.clicked.connect(self.showCalibrateInterface)
        labyrinte.clicked.connect(self.detectColor)
        verif1.clicked.connect(self.afficher_pattern_couleurs)
        verif2.clicked.connect(self.detectC2)

        # Add direction buttons to layout
        control_layout.addWidget(avancer_button, 0, 2)
        control_layout.addWidget(reculer_button, 0, 0)
        control_layout.addWidget(tourner_button, 0, 1)
        control_layout.addWidget(calibrer)
        control_layout.addWidget(labyrinte)
        control_layout.addWidget(self.robot)
        control_layout.addWidget(self.RobotCalibrate)
        control_layout.addWidget(verif1)
        control_layout.addWidget(verif2)

        # Action buttons with images
        actions = [
            ('Get Ready', './img/tourner.jpg', self.stand_right),
            ('Pas chassé D', './img/pas_chasseD.jpg',self.pas_chasseD),
            ('pas chassé G', './img/pas_chasseL.jpg',self.pas_chasseL),
            ('danser', './img/celebrate.jpg',self.danser),
            ('celebrer', './img/celebrate.jpg',self.celebrer),
            ('be_happy', './img/be_Happy.jpg',self.be_happy),
            ('be sad', './img/be_sad.jpg',self.be_sad),
            ('obstacle', '',self.obstacle),
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
            #self.marty.dance()

    def stand_right(self):
            self.my_marty.stand_straight()
            #self.marty.stand_straight()
    def tourner(self):
            self.my_marty.walk(9,'auto',-10,25,1500)
            #self.marty.walk(9,'auto',-10,25,1500)
    def reculer(self):
            self.my_marty.walk(2,'auto',-10,-25,1500)
            self.marty.walk(2,'auto',-10,-25,1500)
    def avancer(self):
            self.my_marty.walk(2)
            #self.marty.walk(2)
    def pas_chasseD(self):
            self.my_marty.sidestep('right',11,40,900,None)
            #self.marty.sidestep('right',11,40,900,None)
    def pas_chasseL(self):
            self.my_marty.sidestep('left',11,40,900,None)
            #self.marty.sidestep('left',11,40,900,None)
    def celebrer(self):
            self.my_marty.celebrate()
            #self.marty.celebrate()
    def be_happy(self):
            self.my_marty.eyes('excited')
            #self.marty.eyes('excited')
    def be_sad(self):
            self.my_marty.eyes('angry')
            #self.marty.eyes('angry')

    def get_battery(self):
            return self.my_marty.get_battery_remaining()
            
    def obstacle(self):
            return self.my_marty.foot_obstacle_sensed('right')
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Left or event.key() == Qt.Key.Key_4: # type: ignore
            self.pas_chasseL() # type: ignore
        elif event.key() == Qt.Key.Key_Right or event.key() == Qt.Key.Key_6: # type: ignore
            self.pas_chasseD() # type: ignore
        elif event.key() == Qt.Key.Key_Up or event.key() == Qt.Key.Key_8: # type: ignore
            self.avancer() # type: ignore
        elif event.key() == Qt.Key.Key_Down or event.key() == Qt.Key.Key_2: # type: ignore
            self.reculer() # type: ignore
        else:
                    print(f'Key {event.text()} is pressed')
    
    def getCouleur1(self ):
        return self.my_marty.get_color_sensor_hex("left")
    
    def getCouleur2(self):
          return self.marty.get_color_sensor_hex("left")

    def getCouleurs(self):
        print("Robot1:",self.CouleursList1)
        print("Robot2:",self.CouleursList2)

    def showCalibrateInterface (self):
        if(self.RobotCalibrate.text() == "1"):
            windowcalbirate = calibrateWindow(self.my_marty ,self)
        if(self.RobotCalibrate.text() == "2"):
            windowcalbirate = calibrateWindow(self.marty ,self)
        windowcalbirate.show()

    def displayColor(self , couleur, valeur):
          if(self.RobotCalibrate.text() == "1"):
             print(couleur,valeur, self.my_marty)
             self.CouleursList1[couleur] = valeur
          else :
               print(couleur,valeur, self.marty)
               self.CouleursList2[couleur] = valeur

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

    def create_intervals1(self):
        intervals = {}
        
        for color_name, hex_color in self.CouleursList1.items():
            intervals[color_name] = self.create_color_interval(hex_color, 10)
        return intervals
    
    def create_intervals2(self):
        intervals = {}
        
        for color_name, hex_color in self.CouleursList2.items():
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
        intervals1= self.create_intervals1()
        intervals2= self.create_intervals2()
        for color_name, interval in intervals1.items():
            print(f"Interval for {color_name}: {interval}")
        for color_name, interval in intervals2.items():
            print(f"Interval for {color_name}: {interval}")
        
        
        directions1 = []
        directions2 = []
        self.my_marty.stand_straight(1000, None)
        self.marty.stand_straight(1000, None)
        couleur1 = self.getCouleur1()
        couleur2 = self.getCouleur2()
        print("Couleur Robot 1  détectée",couleur1)
        print("Couleur Robot 2  détectée",couleur2)
        if couleur1 is None:
            raise ValueError("getCouleur returned None")
        detected_color1 = self.color_in_intervals(couleur1, intervals1)
        directions1.append(detected_color1)

        detected_color2 = self.color_in_intervals(couleur2, intervals2)
        directions2.append(detected_color2)

        for _ in range(2):
            self.my_marty.walk(6, 'auto', 0, 35, 1500, None)
            self.my_marty.stand_straight(1000, None)
            self.marty.walk(6, 'auto', 0, 35, 1500, None)
            self.marty.stand_straight(1000, None)
            couleur1 = self.getCouleur1()
            couleur2 = self.getCouleur2()
            print("Couleur Robot 1 détectée",couleur1)
            print("Couleur Robot 2 détectée",couleur2)
            if couleur1 is None:
                raise ValueError("getCouleur returned None")
            detected_color1 = self.color_in_intervals(couleur1, intervals1)
            directions1.append(detected_color1)
            detected_color2 = self.color_in_intervals(couleur2, intervals2)
            directions2.append(detected_color2)

        self.my_marty.stand_straight(1000, None)
        self.my_marty.sidestep('right', 6, 35, 1000, None)
        self.marty.stand_straight(1000, None)
        self.marty.sidestep('right', 6, 35, 1000, None)

        couleur1 = self.getCouleur1()
        print("Couleur robot1 détectée",couleur1)
        couleur2 = self.getCouleur2()
        print("Couleur robot2 détectée",couleur2)

        if couleur1 is None:
            raise ValueError("getCouleur returned None")
        detected_color1 = self.color_in_intervals(couleur1, intervals1)
        directions1.append(detected_color1)
        detected_color2 = self.color_in_intervals(couleur2, intervals2)
        directions2.append(detected_color2)

        for _ in range(2):
            self.my_marty.stand_straight(2000, None)
            self.my_marty.walk(6, 'auto', 0, -35, 1500, None)
            couleur1 = self.getCouleur1()
            self.marty.stand_straight(2000, None)
            self.marty.walk(6, 'auto', 0, -35, 1500, None)
            couleur2 = self.getCouleur2()
            print("Couleur robot1 détectée",couleur1)
            print("Couleur robot2 détectée",couleur2)
            if couleur1 is None:
                raise ValueError("getCouleur returned None")
            detected_color1 = self.color_in_intervals(couleur1, intervals1)
            directions1.append(detected_color1)
            detected_color2 = self.color_in_intervals(couleur2, intervals2)
            directions2.append(detected_color2)

        self.my_marty.stand_straight(2000, None)
        self.my_marty.sidestep('right', 6, 35, 1000, None)
        couleur1 = self.getCouleur1()
        print("Couleur Robot 1 détectée",couleur1)

        self.marty.stand_straight(2000, None)
        self.marty.sidestep('right', 6, 35, 1000, None)
        couleur2= self.getCouleur2()
        print("Couleur Robot 2 détectée",couleur2)
        if couleur1 is None:
            raise ValueError("getCouleur returned None")
        detected_color1 = self.color_in_intervals(couleur1, intervals1)
        directions1.append(detected_color1)
        detected_color2 = self.color_in_intervals(couleur2, intervals2)
        directions2.append(detected_color2)

        for _ in range(2):
            self.my_marty.stand_straight(2000, None)
            self.my_marty.walk(6, 'auto', 0, 35, 1500, None)
            couleur1 = self.getCouleur1()
            print("Couleur Robot 1 détectée",couleur1)

            self.marty.stand_straight(2000, None)
            self.marty.walk(6, 'auto', 0, 35, 1500, None)
            couleur2 = self.getCouleur2()
            print("Couleur Robot 1 détectée",couleur2)
            if couleur1 is None:
                raise ValueError("getCouleur returned None")
            detected_color1 = self.color_in_intervals(couleur1, intervals1)
            directions1.append(detected_color1)
            detected_color2 = self.color_in_intervals(couleur2, intervals2)
            directions2.append(detected_color2)

            self.my_marty.stand_straight(1000, None)
            self.marty.stand_straight(1000, None)

        print("chemin fini")
        self.fusionner(directions1,directions2)


    def detectC1(self):
        intervals = self.create_intervals1()
        couleur = self.getCouleur1()
        detected_color = self.color_in_intervals(couleur, intervals)
        print("Couleur détectée Robot 1 ",detected_color)

    def detectC2(self):
        intervals = self.create_intervals2()
        couleur = self.getCouleur2()
        detected_color = self.color_in_intervals(couleur, intervals)
        print("Couleur détectée Robot 2 ",detected_color)

    def fusionner(self,direction1 , direction2 ):
         print("Robot1 : ")
         print(direction1)
         print ("Robot2 : ")
         print(direction2)
         for item1, item2 in zip(direction1, direction2):
            if item1 == "Noir" and item2 != "Noir":
                self.directionsfusionner.append(item2)
            elif item2 == "Noir" and item1 != "Noir":
                self.directionsfusionner.append(item1)
            else:
                self.directionsfusionner.append(item1 if item1 != "Noir" else item2)
         print("Après fusion")
         self.marty.celebrate()
         self.my_marty.celebrate()
         print(self.directionsfusionner)

    def afficher_pattern_couleurs(self):
        for item in self.directionsfusionner:
            if item == 'Jaune':
                self.reculer()
            elif item == 'Blue':
                self.my_marty.get_ready()
                self.my_marty.walk(6, 'auto', 0, -35, 1500, None)
            elif item == 'Blue Marin':
                self.my_marty.sidestep('right', 6, 35, 1000, None)
            elif item == 'Rose':
                self.my_marty.sidestep('left', 6, 35, 1000, None)
            elif item == 'Vert':
                 self.my_marty.walk(6, 'auto', 0, -35, 1500, None)
            elif item == 'Rouge':
                self.my_marty.get_ready()
                self.my_marty.celebrate()
            else:
                print(f"Couleur '{item}' non reconnue, aucun pattern affiché.")
            
            print()  


    

def main():
    app = QApplication(sys.argv)

    login = LoginWindow()
    if login.exec() == QDialog.DialogCode.Accepted:
        ip_address1 = login.ip_input1.text()
        ip_address2 = login.ip_input2.text()
        window = RobotInterface(ip_address1,ip_address2)
        window.show()
        sys.exit(app.exec())

if __name__ == '__main__':
    main()
