import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PyQtLib.ui.update_word import Ui_update_word

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
from PyQt6.QtGui import QIcon


class UpdateWordDlg(QDialog):
    entry_added_dlg = pyqtSignal(dict)
    entry_modify_dlg = pyqtSignal(dict, dict, int)
    def __init__(self, entry_modify=None, row_modify=-1):
        super().__init__()
        self.ui = Ui_update_word()  # 创建 UI 实例
        self.ui.setupUi(self)  # 设置 UI
        self.setWindowIcon(QIcon("./resources/qss/icon/wubi-converter.ico"))
        self.entry_modify = entry_modify
        self.row = row_modify
        self.is_add_new_entry = True
        # uic.loadUi("./resources/update_word.ui", self)
        self.ui.cancelPbn.clicked.connect(self.close)
        self.ui.yesPbn.clicked.connect(self.update_new_word)
        self.ui.codeEdit.textChanged.connect(self.on_code_changed)
        if entry_modify:
            self.entry = entry_modify.copy()
            self.is_add_new_entry = False
            self.ui.codeEdit.setText(entry_modify['code'])
            self.ui.rankCombo.setCurrentText(str(entry_modify['rank']))
            self.ui.wordEdit.setText(entry_modify['word'])
        else:
            self.entry = {
                'code': '',
                'rank': 1,
                'word': '',
            }
            self.is_add_new_entry = True
            self.ui.codeEdit.setText('')
            self.ui.rankCombo.setCurrentText('1')
            self.ui.wordEdit.setText('')

    def on_code_changed(self, text):
        self.entry['code'] = text
        if self.is_legal_entry():
            self.ui.yesPbn.setEnabled(True)
            self.ui.label.setText('编码合法!')
        else:
            self.ui.yesPbn.setEnabled(False)
            self.ui.label.setText('编码非法!')

    def is_legal_entry(self):
        if self.entry:
            code = self.entry['code']
            if isinstance(code, str) and 0 < len(code) <= 4:
                return True
            else:
                return False
        else:
            self.ui.label.setText('编码为空!')
            return False

    def update_new_word(self):
        self.entry = {
            'code': self.ui.codeEdit.text(),
            'rank': int(self.ui.rankCombo.currentText()),
            'word': self.ui.wordEdit.text(),
        }
        if self.is_legal_entry():  # 确保输入不为空
            if self.is_add_new_entry:
                self.entry_added_dlg.emit(self.entry)  # 发出信号并传递输入的值
            else:
                if self.entry_modify != self.entry:
                    self.entry_modify_dlg.emit(self.entry_modify, self.entry, self.row)  # 发出信号并传递输入的值
            self.accept()  # 关闭对话框
