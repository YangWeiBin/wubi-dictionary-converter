import sys

import xml.etree.ElementTree as ET
import plistlib

# convert_plist_to_entries：将Mac的plist文件转化为entries
# convert_entries_to_plist：将entries转化为Mac的plist文件

class Macwubi:
    def plist_to_entries(self, plist_file_name):
        print("plist_to_entries")
        entries = []
        # 读取plist文件
        with open(plist_file_name, 'rb') as fp:
            plist_data = plistlib.load(fp)
        # 遍历plist数据并打印每个dict中的key和value
        for item in plist_data:
            if isinstance(item, dict):  # 确保item是一个字典
                items_list = list(item.items())
                first_key, word = items_list[0]
                second_key, code = items_list[1]
                entry = {
                    'code': code,
                    'rank': 1,
                    'word': word,
                }
                print(f'entry = {entry}')
                entries.append(entry)
        return entries

    def entries_to_plist(self, entries):
        # 创建 plist 数据结构
        plist_data = []

        # 遍历 entries 列表，生成 plist 数据
        for entry in entries:
            plist_data.append({
                'phrase': entry['word'],
                'shortcut': entry['code']
            })

        # 写入到 test.plist 文件
        return plist_data


    def convert_entries_to_plist(self, entries, mac_plist_filename):
        plist_data = self.entries_to_plist(entries)
        with open(mac_plist_filename, 'wb') as fp:
            plistlib.dump(plist_data, fp)

    def convert_plist_to_entries(self, plist_file_path):
        return self.plist_to_entries(plist_file_path)





