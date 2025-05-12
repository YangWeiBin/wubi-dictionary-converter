import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PyQtLib.ui.about_dialog import Ui_AboutDialog

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
from PyQt6.QtGui import QIcon

class AboutDlg(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AboutDialog()  # 创建 UI 实例
        self.ui.setupUi(self)  # 设置 UI
        self.setWindowIcon(QIcon("./resources/qss/icon/wubi-converter.ico"))
        self.ui.okPbn.clicked.connect(self.close)
