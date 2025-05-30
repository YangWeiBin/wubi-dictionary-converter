import sys
import os

import PyQtLib.main_window as mainwindow

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

lenove_env_path_script = 'D:/Anaconda3-2023.09/Lib/site-packages'
lenove_env_path_packages = 'D:/Anaconda3-2023.09/Lib/site-packages'

hp_env_path_packages = 'D:/00-YangWeiBin/software/Python311/site-packages'
hp_env_path_script = 'D:/00-YangWeiBin/software/Python311/Scripts'

path_packages = lenove_env_path_packages
path_script = lenove_env_path_script

sys.path.append(path_script)
sys.path.append(path_packages + '/PySide6')
sys.path.append(path_packages + '/qt6_tools')

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont

if __name__ == "__main__":
    app = QApplication(sys.argv)
    font = QFont("Arial", 12)  # 设置字体为 Arial，大小为 12
    app.setFont(font)
    window = mainwindow.MainWindow(font)
    window.show()
    sys.exit(app.exec())
