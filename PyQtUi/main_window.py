import sys
import os


import Microsoft.microsoft_wubi as mswubi
import Mac.mac_wubi as macwubi
import MyFormat.myformat_wubi as myformat
import QQ.qq_wubi as qqwubi
import Sogou.sogou_wubi as sougouwubi
import PyQtUi.update_word as updateword
import PyQtUi.about_dlg as aboutdlg

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

from PyQt6.QtWidgets import (QMainWindow, QApplication, QFileDialog,
                             QTableView, QTableWidgetItem, QMessageBox)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 加载 .ui 文件
        uic.loadUi("./PyQtUi/main_window.ui", self)
        self.setWindowStyle()
        self.ms_wubi_obj = mswubi.MSwubi()
        self.mac_wubi_obj = macwubi.Macwubi()
        self.my_format_obj = myformat.MyFormat()
        self.qq_wubi_obj = qqwubi.QQwubi()
        self.sougou_wubi_obj = sougouwubi.SOUGOUwubi()
        self.entries = []
        self.wordList.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        # connect signal-slot
        self.wordLibPathPbn.clicked.connect(self.import_word_lib)
        self.exportPbn.clicked.connect(self.export_word_lib)
        self.action_about.triggered.connect(self.show_about_dlg)
        self.wordList.itemDoubleClicked.connect(self.show_modify_word_ui)
        self.addWordPbn.clicked.connect(self.show_add_word_ui)
        self.delWordPbn.clicked.connect(self.del_word)


    # @pyqtSlot()
    def show_about_dlg(self):
        about_dlg = aboutdlg.AboutDlg()
        about_dlg.exec()

    def num_to_value(self, n):
        mapping = {
            0: 'code',
            1: 'rank',
            2: 'word'
        }
        return mapping.get(n, None)  # 如果 n 不在字典中，返回 None

    def del_word(self):
        selected_items = self.wordList.selectedItems()
        selected_rows = set()  # 使用集合存储行号，避免重复
        if selected_items:
            for item in selected_items:
                selected_rows.add(item.row())
            for row in selected_rows:
                entry = self.entries.pop(row)
                self.logText.append(f"Delete row:{row}, entry = {entry}.")
            self.update_entries_to_list()
        else:
            self.logText.append("No row is selected!")

    def show_add_word_ui(self):
        update_word_dlg = updateword.UpdateWordDlg()
        update_word_dlg.entry_added_dlg.connect(self.add_word_by_dlg)
        update_word_dlg.exec()

    def show_modify_word_ui(self, item):
        # first delete then add
        row = item.row()
        entry = self.entries.pop(row) ## delete row item
        self.logText.append(f"Modify row:{row}, entry = {entry}.")
        update_word_dlg = updateword.UpdateWordDlg(entry_modify=entry)
        update_word_dlg.entry_modify_dlg.connect(self.add_word_by_dlg)
        update_word_dlg.exec()

    def add_word_by_dlg(self, entry):
        self.logText.append(f"Added entry={entry}.")
        self.entries.append(entry)
        self.update_entries_to_list()

    def setWindowStyle(self):
        with open("./PyQtUi/qss/psblack.css", "r") as file:
            qss = file.read()
        palette_color = qss[20:27]  # 这里假设颜色是一个字符串，比如 "#FFFFFF"
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(palette_color))
        QApplication.instance().setPalette(palette)
        QApplication.instance().setStyleSheet(qss)
        self.searchPbn.setIcon(QIcon.fromTheme('edit-find'))  # 使用内置图标
        self.searchPbn.setIconSize(QSize(16, 16))  # 设置图标大小

    def add_word(self, entry):
        row_count = self.wordList.rowCount()
        self.wordList.setRowCount(row_count + 1)
        item_code = QTableWidgetItem(entry['code'])
        item_code.setFlags(item_code.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.wordList.setItem(row_count, 0, item_code)
        item_rank = QTableWidgetItem(str(entry['rank']))
        item_rank.setFlags(item_rank.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.wordList.setItem(row_count, 1, item_rank)
        item_word = QTableWidgetItem(str(entry['word']))
        item_word.setFlags(item_word.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.wordList.setItem(row_count, 2, item_word)

    def is_sougou_ini_file(self, line):
        equal_pos = line.find('=')
        comma_pos = line.find(',')
        if equal_pos == -1 or comma_pos == -1:
            return None
        if comma_pos < equal_pos:
            return True
        else:
            return False

    def showErrorDialog(self, msg_info, msg_txt):
        # 创建一个信息对话框
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(msg_info)
        msg.setInformativeText(msg_txt)
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        # 显示对话框
        msg.exec()

    def update_entries_to_list(self):
        self.entries.sort(key=lambda x: x['code'])
        self.wordList.setRowCount(0)  # 清空表格
        for entry in self.entries:
            self.add_word(entry)
        self.logText.append(f"更新词库成功!")

    def read_word_lib_to_entries(self, word_lib_path):
        self.entries.clear()
        extension = self.get_file_extension(word_lib_path)
        self.entries = []
        if extension == '.myfmt':
            self.entries = self.my_format_obj.txt_to_entries(word_lib_path)
        elif extension == '.dat':
            self.entries = self.ms_wubi_obj.convert_dat_to_entries(word_lib_path)
        elif extension == '.plist':
            self.entries = self.mac_wubi_obj.convert_plist_to_entries(word_lib_path)
        elif extension == '.ini':
            is_sougou_ini = None
            with open(word_lib_path, 'r', encoding='utf-8') as file:
                first_line = file.readline()
                is_sougou_ini = self.is_sougou_ini_file(first_line)
            if is_sougou_ini is True:
                self.entries = self.sougou_wubi_obj.convert_sougou_udf_to_entries(word_lib_path)
            elif is_sougou_ini is False:
                self.entries = self.qq_wubi_obj.convert_qq_udf_to_entries(word_lib_path)
            else:
                self.showErrorDialog("格式有误", "文件格式有误，请检查格式重新导入 !")
        else:
            self.showErrorDialog("导入为空", "导入的词库文件为空，请检查格式重新导入 !")
        self.update_entries_to_list()

    def get_file_extension(self, file_path):
        # 使用 os.path.splitext 获取文件名和扩展名
        _, extension = os.path.splitext(file_path)
        return extension

    # @pyqtSlot()
    def import_word_lib(self):
        # 弹出文件选择对话框
        word_lib_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "自定义格式 (*.myfmt);;"
                                                                            "微软五笔格式 (*.dat);;"
                                                                            "Mac五笔格式 (*.plist);;"
                                                                            "搜狗和QQ五笔格式 (*.ini)")
        if word_lib_path:
            print(f"选择的文件: {word_lib_path}")
            self.wordLibPathEdit.setText(word_lib_path)
            self.read_word_lib_to_entries(word_lib_path)

    def export_entries_to_word_lib(self, word_lib_path):
        extension = self.get_file_extension(word_lib_path)
        if extension == '.myfmt':
            self.my_format_obj.entries_to_txt(self.entries, word_lib_path)
        elif extension == '.dat':
            self.ms_wubi_obj.convert_entries_to_dat(self.entries, word_lib_path)
        elif extension == '.plist':
            self.mac_wubi_obj.convert_entries_to_plist(self.entries, word_lib_path)
        elif extension == '.ini':
            self.sougou_wubi_obj.convert_entries_to_udf(self.entries, word_lib_path)
            # qq udf ini
            self.qq_wubi_obj.convert_entries_to_udf(self.entries, word_lib_path + 'qq')
        elif extension == '.txt':
            # qq usr txt
            self.qq_wubi_obj.convert_entries_to_usr(self.entries, word_lib_path)


    # @pyqtSlot()
    def export_word_lib(self):
        # 弹出文件保存对话框
        word_lib_path, _ = QFileDialog.getSaveFileName(self, "导出word文件", "",  "自定义格式 (*.myfmt);;"
                                                                            "微软五笔格式 (*.dat);;"
                                                                            "Mac五笔格式 (*.plist);;"
                                                                            "搜狗五笔格式 (*.ini);;"
                                                                            "QQ五笔自定义 (*.ini);;"
                                                                            "QQ五笔词组 (*.txt)")
        if word_lib_path:
            self.logText.append(f"导出的文件: {word_lib_path}")
            self.export_entries_to_word_lib(word_lib_path)
        else:
            self.logText.append(f"导出的文件: {word_lib_path}， 为空 !")
