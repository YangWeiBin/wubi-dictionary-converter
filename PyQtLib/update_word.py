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
        self.ui.wordEdit.textChanged.connect(self.on_word_changed)
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
        result, char = self.is_legal_code()
        if result is None:
            self.ui.yesPbn.setEnabled(False)
            self.ui.label.setText('编码非法: 字符串长度不在1到4之间!')
        elif result is True:
            self.ui.yesPbn.setEnabled(True)
            self.ui.label.setText('编码合法!')
        elif result is False:
            self.ui.yesPbn.setEnabled(False)
            self.ui.label.setText(f"字符串无效，错误的字符: {char}!")

    def is_legal_word(self):
        word = self.entry['word']
        if word == '':
            self.ui.yesPbn.setEnabled(False)
            self.ui.label.setText('词组不能是为空！')
            return False
        else:
            self.ui.yesPbn.setEnabled(True)
            self.ui.label.setText('编码合法!')
            return True

    def on_word_changed(self, text):
        self.entry['word'] = text
        self.is_legal_word()

    def is_legal_code(self):
        allowed_characters = set("abcdefghijklmnopqrstuvwxyz,./';[]\\\\-`")
        code = self.entry.get('code')
        if self.entry is None or code is None or len(code) < 1 or len(code) > 4:
            return None, ''
        for char in code:
            if char not in allowed_characters:
                return False, char
        return True, ''

    def update_new_word(self):
        self.entry = {
            'code': self.ui.codeEdit.text(),
            'rank': int(self.ui.rankCombo.currentText()),
            'word': self.ui.wordEdit.text(),
        }
        if self.is_legal_code() and self.is_legal_word():  # 确保输入不为空
            if self.is_add_new_entry:
                self.entry_added_dlg.emit(self.entry)  # 发出信号并传递输入的值
            else:
                if self.entry_modify != self.entry:
                    self.entry_modify_dlg.emit(self.entry_modify, self.entry, self.row)  # 发出信号并传递输入的值
            self.accept()  # 关闭对话框
