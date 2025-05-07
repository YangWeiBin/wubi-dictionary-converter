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
from PyQt6.QtCore import pyqtSignal


class UpdateWordDlg(QDialog):
    entry_added_dlg = pyqtSignal(dict)
    entry_modify_dlg = pyqtSignal(dict)
    def __init__(self, entry_modify=None):
        super().__init__()
        self.entry = entry_modify if entry_modify else {}
        self.is_add_new_entry = True
        uic.loadUi("./PyQtUi/update_word.ui", self)
        self.cancelPbn.clicked.connect(self.close)
        self.yesPbn.clicked.connect(self.update_new_word)
        self.codeEdit.textChanged.connect(self.on_code_changed)
        if entry_modify:
            self.is_add_new_entry = False
            self.codeEdit.setText(entry_modify['code'])
            self.rankCombo.setCurrentText(str(entry_modify['rank']))
            self.wordEdit.setText(entry_modify['word'])
        else:
            self.is_add_new_entry = True
            self.codeEdit.setText('')
            self.rankCombo.setCurrentText('1')
            self.wordEdit.setText('')

    def on_code_changed(self, text):
        self.entry['code'] = text
        if self.is_legal_entry():
            self.yesPbn.setEnabled(True)
            self.label.setText('编码合法!')
        else:
            self.yesPbn.setEnabled(False)
            self.label.setText('编码非法!')

    def is_legal_entry(self):
        if self.entry:
            code = self.entry['code']
            if isinstance(code, str) and 0 < len(code) <= 4:
                return True
            else:
                return False
        else:
            self.label.setText('编码为空!')
            return False

    def update_new_word(self):
        self.entry = {
            'code': self.codeEdit.text(),
            'rank': int(self.rankCombo.currentText()),
            'word': self.wordEdit.text(),
        }
        if self.is_legal_entry():  # 确保输入不为空
            if self.is_add_new_entry:
                self.entry_added_dlg.emit(self.entry)  # 发出信号并传递输入的值
            else:
                self.entry_modify_dlg.emit(self.entry)  # 发出信号并传递输入的值
            self.accept()  # 关闭对话框
