import sys

import xml.etree.ElementTree as ET

# convert_plist_to_entries：将Mac的plist文件转化为entries
# convert_entries_to_plist：将entries转化为Mac的plist文件

class Macwubi:
    def plist_to_entries(self, plist_file_name):
        print("plist_to_entries")
        entries = []
        # 读取 test.list 文件
        tree = ET.parse(plist_file_name)
        root = tree.getroot()
        # 确保根元素是 plist
        if root.tag == 'plist':
            # 找到 array 元素
            array = root.find('array')
            # 遍历每个 dict 元素
            for dict_elem in array.findall('dict'):
                entry = {}
                # 提取 phrase 和 shortcut
                phrase_key = dict_elem.find("key[.='phrase']")
                if phrase_key is not None:
                    phrase_value = phrase_key.getnext()  # 获取下一个元素，即 <string>
                    entry['code'] = phrase_value.text if phrase_value is not None else None

                shortcut_key = dict_elem.find("key[.='shortcut']")
                if shortcut_key is not None:
                    shortcut_value = shortcut_key.getnext()  # 获取下一个元素，即 <string>
                    entry['word'] = shortcut_value.text if shortcut_value is not None else None

                entry['rank'] = 1
                # 将条目添加到 entries 列表中
                if entry:
                    entries.append(entry)

        return entries

    def entries_to_plist(self, entries):
        plist_data = ''
        plist = ET.Element('plist', version='1.0')
        array = ET.SubElement(plist, 'array')

        for entry in entries:
            dict_elem = ET.SubElement(array, 'dict')

            # 添加 phrase
            key_elem_phrase = ET.SubElement(dict_elem, 'key')
            key_elem_phrase.text = 'phrase'
            string_elem_phrase = ET.SubElement(dict_elem, 'string')
            string_elem_phrase.text = entry['code']  # 使用 code 作为 phrase

            # 添加 shortcut
            key_elem_shortcut = ET.SubElement(dict_elem, 'key')
            key_elem_shortcut.text = 'shortcut'
            string_elem_shortcut = ET.SubElement(dict_elem, 'string')
            string_elem_shortcut.text = entry['word']  # 使用 word 作为 shortcut

        # 创建树并写入文件
        tree = ET.ElementTree(plist)
        return tree

    def convert_entries_to_plist(self, entries, mac_plist_filename):
        plist_data_tree = self.entries_to_plist(entries)
        with open(mac_plist_filename, 'wb') as file:
            file.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
            file.write(b'<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n')
            plist_data_tree.write(file, encoding='utf-8', xml_declaration=False)

    def convert_plist_to_entries(self, plist_file_path):
        return self.plist_to_entries(plist_file_path)





