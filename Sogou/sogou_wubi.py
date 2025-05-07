# convert_sougou_udf_to_entries：将QQ的自定义文件转化为entries
# convert_entries_to_udf：将entries转化为QQ的自定义

class SOUGOUwubi:

    def convert_sougou_udf_to_entries(self, ini_sougou_udf_file_name):
        entries = []
        # 打开并读取文件
        with open(ini_sougou_udf_file_name, 'r', encoding='utf-8') as file:
            for line in file:
                # 分割每一行  iisg,1=水杯
                parts = line.split(',')
                if len(parts) == 2:
                    code = parts[0].strip()
                    rank, word = parts[1].split('=')
                    word = word.replace('\n', '')
                    # 将条目添加到列表中
                    entries.append({
                        'code': code,
                        'rank': rank,
                        'word': word
                    })
        return entries

    def convert_entries_to_udf(self, entries, sougou_definition_filename):
        with open(sougou_definition_filename, 'w', encoding='utf-8') as file:
            for entry in entries:
                # tuud,1=奇瑞QQ
                line = f"{entry['code']},{entry['rank']}={entry['word']}\n"
                file.write(line)


