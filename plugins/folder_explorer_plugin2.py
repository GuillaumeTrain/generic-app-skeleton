import time

from PySide6.QtWidgets import QTreeView, QFileSystemModel, QVBoxLayout
from core.plugin_loader import PluginBase

class Plugin(PluginBase):
    def __init__(self,classname ="FolderExplorerPlugin2", name="Folder Explorer Plugin 2", version="0.0.1"):
        super().__init__(classname,name, version)

    def start(self, parent_layout):
        model = QFileSystemModel()
        model.setRootPath('')

        tree = QTreeView()
        tree.setModel(model)
        tree.setRootIndex(model.index(''))

        parent_layout.addWidget(tree)


