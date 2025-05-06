
# convert_qq_udf_to_entries：将QQ的自定义文件转化为entries
# convert_entries_to_udf：将entries转化为QQ的自定义
# convert_entries_to_usr：将entries转化为QQ的用户

class QQwubi:
    def convert_qq_udf_to_entries(self, ini_qq_udf_file_name):
        entries = []
        # 打开并读取文件
        with open(ini_qq_udf_file_name, 'r', encoding='utf-8') as file:
            for line in file:
                # 分割每一行  wgtf=1,全选
                parts = line.split(',')
                if len(parts) == 2:
                    code, rank = parts[0].split('=')
                    word = parts[1].replace('\n', '')
                    # 将条目添加到列表中
                    entries.append({
                        'code': code,
                        'rank': rank,
                        'word': word
                    })
        return entries

    def convert_entries_to_udf(self, entries, qq_definition_filename):
        with open(qq_definition_filename, 'w', encoding='utf-8') as file:
            for entry in entries:
                # dgqq=2,奇瑞QQ
                line = f"{entry['code']}={entry['rank']},{entry['word']}\n"
                file.write(line)

    def convert_entries_to_usr(self, entries, qq_usr_filename):
        with open(qq_usr_filename, 'w', encoding='utf-8') as file:
            for entry in entries:
                # dgqq 奇瑞
                line = f"{entry['code']} {entry['word']}\n"
                file.write(line)