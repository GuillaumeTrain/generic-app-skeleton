import asyncio
import sys

from PySide6.QtCore import QThread, Signal, Slot, Qt
from PySide6.QtWidgets import QSplashScreen, QProgressBar, QMainWindow, QApplication
from PySide6.QtGui import QPixmap
import requests
import importlib
import os

class SplashScreen(QSplashScreen):
    def __init__(self):
        #init qpixmap
        qpix = QPixmap("splash.png")
        super().__init__(qpix)
        self.setStyleSheet("background-color: black;")
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(10, self.height() - 30, self.width() - 20, 20)

    def update_progress(self, value):
        self.progressBar.setValue(value)


class AsyncWorker(QThread):
    result_ready = Signal(object)

    def __init__(self, coro):
        super().__init__()
        self.coro = coro

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(self.coro)
        self.result_ready.emit(result)
        loop.close()

async def long_running_task():
    await asyncio.sleep(5)  # Simule une tâche longue
    return "Tâche terminée"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SimplExe")
        self.setGeometry(100, 100, 800, 600)
        self.start_async_task()

    def start_async_task(self):
        self.worker = AsyncWorker(long_running_task())
        self.worker.result_ready.connect(self.on_task_complete)
        self.worker.start()

    @Slot(object)
    def on_task_complete(self, result):
        print(result)



class PluginBase:
    def __init__(self, name):
        self.name = name

    def start(self):
        raise NotImplementedError

def load_plugins(plugin_folder="plugins"):
    plugins = []
    for filename in os.listdir(plugin_folder):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            module = importlib.import_module(f"{plugin_folder}.{module_name}")
            plugin_class = getattr(module, "Plugin")
            plugin_instance = plugin_class()
            plugins.append(plugin_instance)
    return plugins
class Plugin(PluginBase):
    def __init__(self):
        super().__init__("Sample Plugin")

    def start(self):
        print(f"{self.name} démarré")

from main import PluginBase
class UpdateManager:
    def __init__(self, update_url):
        self.update_url = update_url

    def check_for_updates(self):
        response = requests.get(self.update_url)
        if response.status_code == 200:
            # Logique de mise à jour à implémenter
            pass

def main():
    app = QApplication(sys.argv)

    splash = SplashScreen()
    splash.show()

    plugins = load_plugins()
    total_plugins = len(plugins)


    window = MainWindow()
    window.show()

    splash.finish(window)
    for i, plugin in enumerate(plugins):
        plugin.start(window.layout())
        splash.update_progress((i + 1) / total_plugins * 100)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
