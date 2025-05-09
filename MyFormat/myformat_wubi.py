import os

class MyFormat:
    def entries_to_txt(self, entries, my_format_filename):
        with open(my_format_filename, 'w', encoding='utf-8') as file:
            for entry in entries:
                line = f"code={entry['code']}, rank={entry['rank']}, word={entry['word']}\n"
                file.write(line)

    def txt_to_entries(self, my_format_filename):
        entries = []
        with open(my_format_filename, 'r', encoding='utf-8') as file:
            for line in file:
                if line:  # 确保行不为空
                    parts = line.split(', ')  # 按', '分割
                    if len(parts) == 3:  # 确保每行有三个部分
                        entry = {}
                        for part in parts:
                            # 分割每个部分的键和值
                            key, value = part.split('=')
                            key = key.strip().lower()
                            # 只去掉换行符
                            value = value.replace('\n', '')  # 保留空格，但去掉换行符
                            # 如果是 rank 则转换为整数
                            if key == 'rank':
                                entry[key] = int(value)
                            else:
                                entry[key] = value
                        exists = any(
                            e['code'] == entry['code'] and e['rank'] == entry['rank'] and e['word'] == entry['word'] for
                            e in entries)
                        if not exists:
                            entries.append(entry)
        return entries
