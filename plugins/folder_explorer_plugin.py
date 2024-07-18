import time

from PySide6.QtWidgets import QTreeView, QFileSystemModel, QVBoxLayout
from main import PluginBase

class FolderExplorerPlugin(PluginBase):
    def __init__(self):
        super().__init__("Folder Explorer Plugin")

    def start(self, parent_layout):
        model = QFileSystemModel()
        model.setRootPath('')

        tree = QTreeView()
        tree.setModel(model)
        tree.setRootIndex(model.index(''))

        parent_layout.addWidget(tree)

# Rename the class to "Plugin" to ensure it matches the loader's expectation.
Plugin = FolderExplorerPlugin
#wait 10s
time.sleep(10)