import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from core.splash_screen import SplashScreen
from core.plugin_loader import PluginBase, load_plugins
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SimplExe")
        self.setGeometry(100, 100, 800, 600)

def main():
    app = QApplication(sys.argv)
    # lancer le splash screen
    starting = True
    splash = SplashScreen()
    splash.restartprogressbar()
    load_plugins(splash)
    splash.finish(splash)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
