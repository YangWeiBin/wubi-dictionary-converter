import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

sys.path.append('./MS')
sys.path.append('./MyFormat')
sys.path.append('./QQ')
sys.path.append('./Sougou')
sys.path.append('./Util')
sys.path.append('./PyQtUi')

import MS.MSwubi as mswubi
import Util.util as util
import MyFormat.MyFormatTxt as myformat
import QQ.QQwubi as qqwubi
import Sougou.SOUGOUwubi as sougouwubi


class Convertor:
    def __init__(self):
        self.ms_wubi_obj = mswubi.MSwubi()  # 类的属性
        self.my_format_obj = myformat.MyFormat()  # 类的属性
        self.qq_wubi_obj = qqwubi.QQwubi()
        self.sougou_wubi_obj = sougouwubi.SOUGOUwubi()

    def file_name_num_plus_1_current_time(self, filepath):
        filename = os.path.basename(filepath)
        parts = filename.split('-')
        number = int(parts[0]) + 1  # 将编号部分转换为整数并加1
        formatted_date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # 格式化为 YYYYMMDD-HHMMSS
        # 组合新的字符串
        return f"{number:02d}-", formatted_date_time

    # my_format_to_ms_dat
    def my_format_to_ms_dat(self, txt_file_name, special_entries=None):
        if special_entries is None:
            special_entries = []
        entries = self.my_format_obj.txt_to_entries(txt_file_name)
        entries = entries + special_entries
        util.print_entries(entries)
        num, formatted_date_time = self.file_name_num_plus_1_current_time(txt_file_name)
        dat_filename = num + 'MS_' + formatted_date_time + '.dat'
        self.ms_wubi_obj.convert_entries_to_dat(dat_filename, entries)
        print(f"成功将 [{txt_file_name}] 转成 [{dat_filename}] 文件。")

    def ms_dat_to_my_format(self, dat_file_name, special_entries=None):
        if special_entries is None:
            special_entries = []
        entries = self.ms_wubi_obj.convert_dat_to_entries(dat_file_name)
        entries = entries + special_entries
        util.print_entries(entries)
        num, formatted_date_time = self.file_name_num_plus_1_current_time(dat_file_name)
        my_txt_filename = num + 'My_Format_' + formatted_date_time + '-by_MS.txt'
        self.my_format_obj.entries_to_txt(entries, my_txt_filename)
        print(f"成功将 [{dat_file_name}] 转成 [{my_txt_filename}] 文件。")

    def my_format_to_qq_udf_ini(self, txt_file_name, special_entries=None):
        if special_entries is None:
            special_entries = []
        entries = self.my_format_obj.txt_to_entries(txt_file_name)
        entries = entries + special_entries
        util.print_entries(entries)
        num, formatted_date_time = self.file_name_num_plus_1_current_time(txt_file_name)
        qq_udf_filename = num + 'QQ_Udf_' + formatted_date_time + '.ini'
        self.qq_wubi_obj.convert_entries_to_udf(qq_udf_filename, entries)
        print(f"成功将 [{txt_file_name}] 转成 [{qq_udf_filename}] 文件。")

    def qq_udf_ini_to_my_format(self, ini_qq_udf_file_name, special_entries=None):
        if special_entries is None:
            special_entries = []
        entries = self.qq_wubi_obj.convert_qq_udf_to_entries(ini_qq_udf_file_name)
        entries = entries + special_entries
        util.print_entries(entries)
        num, formatted_date_time = self.file_name_num_plus_1_current_time(ini_qq_udf_file_name)
        my_txt_filename = num + 'My_Format_' + formatted_date_time + '-by_QQ.txt'
        self.my_format_obj.entries_to_txt(entries, my_txt_filename)
        print(f"成功将 [{ini_qq_udf_file_name}] 转成 [{my_txt_filename}] 文件。")

    def my_format_to_sougou_udf_ini(self, txt_file_name, special_entries):
        entries = self.my_format_obj.txt_to_entries(txt_file_name)
        entries = entries + special_entries
        util.print_entries(entries)
        num, formatted_date_time = self.file_name_num_plus_1_current_time(txt_file_name)
        sougou_udf_filename = num + 'Sougou_Udf_' + formatted_date_time + '.ini'
        self.sougou_wubi_obj.convert_entries_to_udf(sougou_udf_filename, entries)
        print(f"成功将 [{txt_file_name}] 转成 [{sougou_udf_filename}] 文件。")

    def sougou_udf_ini_to_my_format(self, ini_sougou_udf_file_name, special_entries=None):
        if special_entries is None:
            special_entries = []
        entries = self.sougou_wubi_obj.convert_sougou_udf_to_entries(ini_sougou_udf_file_name)
        entries = entries + special_entries
        util.print_entries(entries)
        num, formatted_date_time = self.file_name_num_plus_1_current_time(ini_sougou_udf_file_name)
        my_txt_filename = num + 'My_Format_' + formatted_date_time + 'by-Sougou.txt'
        self.my_format_obj.entries_to_txt(entries, my_txt_filename)
        print(f"成功将 [{ini_sougou_udf_file_name}] 转成 [{my_txt_filename}] 文件。")




# def main():
#     convertor = Convertor()
#     special_entries = [
#         # {
#         #     'code': 'tuud',
#         #     'rank': 1,
#         #     'word': ' + →  ',
#         # }
#     ]
#     #
#     # convertor.my_format_to_ms_dat('07-My_Format_2024-12-29_19-55-31.txt', special_entries)
#     # convertor.my_format_to_qq_udf_ini('07-My_Format_2024-12-29_19-55-31.txt', special_entries)
#     # convertor.my_format_to_sougou_udf_ini('07-My_Format_2024-12-29_19-55-31.txt', special_entries)
#
#     convertor.ms_dat_to_my_format('08-MS_2024-12-29_19-56-39.dat', special_entries)
#     convertor.qq_udf_ini_to_my_format('08-QQ_Udf_2024-12-29_19-56-39.ini', special_entries)
#     convertor.sougou_udf_ini_to_my_format('08-Sougou_Udf_2024-12-29_19-56-39.ini')

# if __name__ == "__main__":
#     # 检查参数数量
#     main()





# sys.path.append('D:/00-YangWeiBin/software/Python311/Scripts')
# sys.path.append('D:/00-YangWeiBin/software/Python311/site-packages/PySide6')
# sys.path.append('D:/00-YangWeiBin/software/Python311/qt6_tools')
# sys.path.append('D:/00-YangWeiBin/software/Python311/site-packages')
#
#
# from PyQt6.QtWidgets import QMainWindow, QApplication
#
# import PyQtUi.main_window as MainWindow
#
#
# class Window(QMainWindow, MainWindow.Ui_MainWindow):
#     def __init__(self):
#         super(QMainWindow, self).__init__()
#         self.setupUi(self)
#
# def main():
#     app = QApplication(sys.argv)
#     mywindow = Window()
#     mywindow.show()
#     sys.exit(app.exec())
#
#
# if __name__ == "__main__":
#     main()

