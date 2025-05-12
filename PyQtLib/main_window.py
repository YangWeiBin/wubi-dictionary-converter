import sys
import os
import subprocess
import platform


import Microsoft.microsoft_wubi as mswubi
import Mac.mac_wubi as macwubi
import MyFormat.myformat_wubi as myformat
import QQ.qq_wubi as qqwubi
import Sogou.sogou_wubi as sougouwubi
import PyQtLib.update_word as updateword
import PyQtLib.about_dlg as aboutdlg

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PyQtLib.ui.main_window import Ui_MainWindow

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
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPalette, QColor


class MainWindow(QMainWindow):
    def __init__(self, cur_font):
        super().__init__()
        # 加载 .ui 文件
        # uic.loadUi("./resources/main_window.ui", self)
        self.ui = Ui_MainWindow()  # 创建 UI 实例
        self.ui.setupUi(self)  # 设置 UI
        self.setWindowStyle()
        self.setFont(cur_font)  # 设置传入的字体
        self.ui.centralwidget.setFont(cur_font)
        self.set_menu_font(self.ui.menubar, cur_font)
        self.ms_wubi_obj = mswubi.MSwubi()
        self.mac_wubi_obj = macwubi.Macwubi()
        self.my_format_obj = myformat.MyFormat()
        self.qq_wubi_obj = qqwubi.QQwubi()
        self.sougou_wubi_obj = sougouwubi.SOUGOUwubi()
        self.entries = []
        self.ui.wordList.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.entries.clear()
        # self.cur_word_path = os.getcwd() + "\\data\\conf.myfmt"
        self.cur_word_path = os.getcwd() + "\\resources\\conf.myfmt"
        self.read_word_lib_to_entries(self.cur_word_path)
        self.ui.SearchLineEditor.setFocus()
        self.setWindowTitle(f"Wubi Word Converter - {self.cur_word_path}")
        self.setWindowIcon(QIcon("./resources/qss/icon/wubi-converter.ico"))
        # set button Icon
        self.ui.mergeWordPbn.setIcon(QIcon("./resources/qss/psblack/download.svg"))
        self.ui.addWordPbn.setIcon(QIcon("./resources/qss/psblack/plus.svg"))
        self.ui.delWordPbn.setIcon(QIcon("./resources/qss/psblack/trash.svg"))
        self.ui.searchPbn.setIcon(QIcon("./resources/qss/psblack/search.svg"))
        # connect signal-slot
        self.ui.wordList.itemDoubleClicked.connect(self.show_modify_word_ui)
        self.ui.addWordPbn.clicked.connect(self.show_add_word_ui)
        self.ui.delWordPbn.clicked.connect(self.del_word)
        self.ui.mergeWordPbn.clicked.connect(self.merge_word)
        self.ui.SearchLineEditor.textChanged.connect(self.search_word)
        self.ui.searchPbn.clicked.connect(self.search_word)
        # connect action
        self.ui.actionAbout.triggered.connect(self.show_about_dlg)
        self.ui.actionOpen.triggered.connect(self.import_word_lib)
        self.ui.actionClearLog.triggered.connect(lambda: self.ui.logText.clear())
        self.ui.actionAddWord.triggered.connect(self.show_add_word_ui)
        self.ui.actionDelWord.triggered.connect(self.del_word)
        self.ui.actionSaveAs.triggered.connect(self.export_word_lib)
        self.ui.actionSave.triggered.connect(lambda: self.export_entries_to_word_lib(self.cur_word_path))
        self.ui.actionMergeConf.triggered.connect(self.merge_conf_word_lib)
        self.ui.actionOpenLocalLib.triggered.connect(lambda: self.open_directory(os.path.dirname(self.cur_word_path)))

    def set_menu_font(self, menu_bar, font):
        menu_bar.setFont(font)
        # 遍历菜单栏中的所有菜单
        for i in range(menu_bar.actions().__len__()):
            menu_action = menu_bar.actions()[i]
            menu = menu_action.menu()

            # 如果是菜单，设置其字体
            if menu:
                menu.setFont(font)
                # 遍历菜单中的所有动作，设置其字体
                for action in menu.actions():
                    action.setFont(font)

            # 设置菜单动作的字体
            menu_action.setFont(font)

    def merge_conf_word_lib(self):
        conf_path = os.getcwd() + "\\data\\conf.myfmt"
        self.read_word_lib_to_entries(conf_path)
        self.export_entries_to_word_lib(conf_path)
        self.ui.logText.append(f"合并到 {conf_path} 完成!")

    def open_directory(self, directory):
        self.ui.logText.append(f"打开 {directory} !")
        if os.path.exists(directory):
            subprocess.Popen(f'explorer "{directory}"')
        else:
            self.ui.logText.append(f"Directory {directory} does not exist.!")

        # 获取当前操作系统
        current_os = platform.system()
        if current_os == "Windows":subprocess.Popen(f'explorer "{directory}"')

        elif current_os == "Darwin":  # macOS
            subprocess.Popen(["open", directory])
        elif current_os == "Linux":
            # 这里假设使用的是 GNOME 的 Nautilus 文件管理器，可以根据需要调整
            subprocess.Popen(["xdg-open", directory])
        else:
            self.ui.logText.append(f"不支持在{current_os}上打开：{directory}!")
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
        selected_items = self.ui.wordList.selectedItems()
        selected_rows = set()  # 使用集合存储行号，避免重复
        if selected_items:
            for item in selected_items:
                selected_rows.add(item.row())
            for index in sorted(selected_rows, reverse=True):
                entry = self.entries.pop(index)
                self.ui.logText.append(f"Delete entry = {entry}.")
            self.update_entries_to_list()
        else:
            self.ui.logText.append("No row is selected!")

    def merge_word(self):
        # 弹出文件选择对话框
        word_lib_paths, _ = QFileDialog.getOpenFileNames(self, "选择文件", "",
                                                       "所有格式 (*.myfmt *.dat *.plist *.ini);;"
                                                       "自定义格式 (*.myfmt);;"
                                                       "微软五笔格式 (*.dat);;"
                                                       "Mac五笔格式 (*.plist);;"
                                                       "搜狗和QQ五笔格式 (*.ini)")
        for word_lib_path in word_lib_paths:
            if word_lib_path:
                self.ui.logText.append(f"合并的文件: {word_lib_path}")
                self.read_word_lib_to_entries(word_lib_path)

    def search_word(self, search_str):
        if search_str == "":
            # 如果搜索字符串为空，显示所有行
            for row in range(self.ui.wordList.rowCount()):
                self.ui.wordList.setRowHidden(row, False)
        else:
            search_str = search_str.lower()  # 转为小写以实现不区分大小写
            for row in range(self.ui.wordList.rowCount()):
                row_found = False
                for col in range(self.ui.wordList.columnCount()):
                    item = self.ui.wordList.item(row, col)
                    if item and search_str in item.text().lower():  # 查找字符串
                        row_found = True
                        break
                self.ui.wordList.setRowHidden(row, not row_found)  # 根据查找结果隐藏或显示行

    def show_add_word_ui(self):
        update_word_dlg = updateword.UpdateWordDlg(entry_modify=None, row_modify=-1)
        update_word_dlg.entry_added_dlg.connect(self.add_word_by_dlg)
        update_word_dlg.exec()

    def show_modify_word_ui(self, item):
        entry = self.entries[item.row()]
        update_word_dlg = updateword.UpdateWordDlg(entry_modify=entry, row_modify=item.row())
        update_word_dlg.entry_modify_dlg.connect(self.modify_word_entry)
        update_word_dlg.exec()

    def modify_word_entry(self, old_entry, new_entry, row):
        self.entries[row] = new_entry
        self.update_entries_to_list()
        self.ui.logText.append(f"Modify entry:{old_entry} to entry = {new_entry}.")

    def add_word_by_dlg(self, entry):
        self.ui.logText.append(f"Added entry={entry}.")
        self.entries.append(entry)
        self.update_entries_to_list()

    def setWindowStyle(self):
        with open("./resources/qss/psblack.css", "r") as file:
            qss = file.read()
        palette_color = qss[20:27]  # 这里假设颜色是一个字符串，比如 "#FFFFFF"
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(palette_color))
        QApplication.instance().setPalette(palette)
        QApplication.instance().setStyleSheet(qss)


    def add_word(self, entry):
        row_count = self.ui.wordList.rowCount()
        self.ui.wordList.setRowCount(row_count + 1)
        item_code = QTableWidgetItem(entry['code'])
        item_code.setFlags(item_code.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.ui.wordList.setItem(row_count, 0, item_code)
        item_rank = QTableWidgetItem(str(entry['rank']))
        item_rank.setFlags(item_rank.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.ui.wordList.setItem(row_count, 1, item_rank)
        item_word = QTableWidgetItem(str(entry['word']))
        item_word.setFlags(item_word.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.ui.wordList.setItem(row_count, 2, item_word)

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
        self.remove_entries_duplicates()
        self.entries.sort(key=lambda x: x['code'])
        self.ui.wordList.setRowCount(0)  # 清空表格
        for entry in self.entries:
            self.add_word(entry)
        self.ui.logText.append(f"更新词库成功!")

    def remove_entries_duplicates(self):
        unique_entries = []
        seen = set()
        for entry in self.entries:
            # 创建一个元组，表示 entry 的唯一标识
            identifier = (entry['code'], entry['rank'], entry['word'])
            # 检查此标识是否已经存在于 seen 集合中
            if identifier not in seen:
                seen.add(identifier)  # 如果没有，添加到集合
                unique_entries.append(entry)  # 并将 entry 添加到 unique_entries
            else:
                self.ui.logText.append(f"entry = {entry} 已存在!")
        self.entries = unique_entries

    def read_word_lib_to_entries(self, word_lib_path):
        extension = self.get_file_extension(word_lib_path)
        if extension == '.myfmt':
            self.entries += self.my_format_obj.txt_to_entries(word_lib_path)
        elif extension == '.dat':
            self.entries += self.ms_wubi_obj.convert_dat_to_entries(word_lib_path)
        elif extension == '.plist':
            self.entries += self.mac_wubi_obj.convert_plist_to_entries(word_lib_path)
        elif extension == '.ini':
            is_sougou_ini = None
            with open(word_lib_path, 'r', encoding='utf-8') as file:
                first_line = file.readline()
                is_sougou_ini = self.is_sougou_ini_file(first_line)
            if is_sougou_ini is True:
                self.entries += self.sougou_wubi_obj.convert_sougou_udf_to_entries(word_lib_path)
            elif is_sougou_ini is False:
                self.entries += self.qq_wubi_obj.convert_qq_udf_to_entries(word_lib_path)
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
            self.ui.logText.append(f"选择的文件: {word_lib_path}")
            self.cur_word_path = word_lib_path
            self.setWindowTitle(f"Wubi Word Converter - {word_lib_path}")
            self.entries.clear()
            self.read_word_lib_to_entries(word_lib_path)

    def export_entries_to_word_lib(self, word_lib_path):
        extension = self.get_file_extension(word_lib_path)
        is_succeed = True
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
        else:
            is_succeed = False
            self.ui.logText.append(f"不支持的格式:  {extension}, 导出文件失败!")
        if is_succeed:
            self.ui.logText.append(f"导出: {word_lib_path} 成功!")


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
            self.ui.logText.append(f"导出的文件: {word_lib_path}")
            self.export_entries_to_word_lib(word_lib_path)
        else:
            self.ui.logText.append(f"导出的文件: {word_lib_path}， 为空 !")
