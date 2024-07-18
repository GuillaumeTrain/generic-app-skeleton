import time

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSplashScreen, QProgressBar, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap


class SplashScreen(QSplashScreen):
    def __init__(self):
        #init qpixmap
        qpix = QPixmap("splash.png")
        super().__init__(qpix)
        self.setStyleSheet("background-color: black;")
        self.progressBar = QProgressBar(self)
        #add self.progress bar to the splash screen layout
        #creer un layout ou la progress bar sera ajoutée en bas

        self.plugin_name = ""
        layout = QVBoxLayout()
        #ajouter un filler au layout pour que la progress bar soit en bas
        layout.addStretch()
        # ajouter un label pour montrer le nom du plugin en cours de chargement
        self.label = QLabel('Loading Plugins ...')
        #definit la couleur du texte en blanc police arrial 12 gras ariere plan transparent
        self.label.setStyleSheet("color: white; font-family: Arial; font-size: 12pt; font-weight: bold; background-color: transparent;")
        layout.addWidget(self.label)
        #centrer le label
        layout.setAlignment(self.label, Qt.AlignmentFlag.AlignCenter)
        #faire en sorte que le label stretch en largeur
        self.label.setFixedWidth(700)

        #ajouter la progress bar au layout
        layout.addWidget(self.progressBar)
        #faire en sorte d'etendre la progress bar
        self.progressBar.setFixedWidth(700)
        #centrer la progress bar
        layout.setAlignment(self.progressBar, Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)


        #faire progresser la progress bar en 10s
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(0)

        #afficher la progress bar
        self.show()

    def restartprogressbar(self):
        self.progressBar.setValue(0)

    def update_progress(self, value, plugin_name=""):
        self.progressBar.setValue(value)
        self.label.setText('Loading Plugin : {}.py'.format(plugin_name))
        #redessiner la progress bar
        self.repaint()
        #redessiner le label
        self.label.repaint()


