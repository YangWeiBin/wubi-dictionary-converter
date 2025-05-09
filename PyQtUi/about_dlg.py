import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PyQt6 import uic

lenove_env_path_script = 'D:/Anaconda3-2023.09/Lib/site-packages'
lenove_env_path_packages = 'D:/Anaconda3-2023.09/Lib/site-packages'

hp_env_path_packages = 'D:/00-YangWeiBin/software/Python311/site-packages'
hp_env_path_script = 'D:/00-YangWeiBin/software/Python311/Scripts'

path_packages = hp_env_path_packages
path_script = hp_env_path_script

sys.path.append(path_script)
sys.path.append(path_packages + '/PySide6')
sys.path.append(path_packages + '/qt6_tools')

from PyQt6.QtWidgets import QDialog


class AboutDlg(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("./resources/about_dialog.ui", self)
        self.okPbn.clicked.connect(self.close)