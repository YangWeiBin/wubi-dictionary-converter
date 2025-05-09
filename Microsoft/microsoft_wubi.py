import sys
import struct
import time

# convert_dat_to_entries：将MS的dat文件转化为entries
# convert_entries_to_dat：将entries转化为MS的dat文件

class MSwubi:
    def read_bytes_until_null(self, r):
        bytes_data = bytearray()
        while True:
            tmp = r.read(2)
            if tmp == b'\x00\x00':
                break
            bytes_data.extend(tmp)
        return bytes_data

    def to_bytes(self, value, length=4):
        return value.to_bytes(length, byteorder='little')

    # convert dat to entries
    def dat_to_entries(self, r):
        r.seek(0x10)
        offset_start = struct.unpack('<i', r.read(4))[0]    # 偏移表开始
        entry_start = struct.unpack('<I', r.read(4))[0]     # 词条开始
        entry_end = struct.unpack('<I', r.read(4))[0]       # 词条结束
        count = struct.unpack('<i', r.read(4))[0]           # 词条数
        entries = []
        export_stamp = struct.unpack('<I', r.read(4))[0]    # 导出的时间戳
        export_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(export_stamp))
        for i in range(count):
            r.seek(offset_start + 4 * i)
            offset = struct.unpack('<I', r.read(4))[0]
            r.seek(entry_start + offset)
            r.seek(6, 1)
            rank = struct.unpack('<B', r.read(1))[0]        # 顺序 1-9
            r.read(1)       # 0x06 不明
            r.seek(4, 1)    # 4 个空字节
            insert_stamp = struct.unpack('<I', r.read(4))[0] # 时间戳
            code_bytes = self.read_bytes_until_null(r)
            word_bytes = self.read_bytes_until_null(r)
            code = code_bytes.decode('utf-16le')
            word = word_bytes.decode('utf-16le')
            entries.append({
                'word': word,
                'code': code,
                'rank': rank,
            })
        return entries

    def gen_rank(self, entries):
        code_map = {}
        for entry in entries:
            if entry['code'] not in code_map:
                code_map[entry['code']] = 0
            code_map[entry['code']] += 1
            entry['rank'] = code_map[entry['code']]
        return entries

    # 将 datetime 对象转换为 4 字节表示
    def ms_time_to(self, t):
        # 减去 30 年并转换为 Unix 时间戳
        adjusted_timestamp = int(t - 946684800)
        return adjusted_timestamp.to_bytes(4, byteorder='big')

    def entries_to_bytes(self, entries):
        now = int(time.time())
        export_stamp = self.to_bytes(now)
        insert_stamp = self.ms_time_to(time.time())
        entries = [e for e in entries if e['code'] != '']
        entries = self.gen_rank(entries)  # 假设这个函数存在
        b = bytearray()
        b.extend(bytes([0x6D, 0x73, 0x63, 0x68, 0x78, 0x75, 0x64, 0x70,
                    0x02, 0x00, 0x60, 0x00, 0x01, 0x00, 0x00, 0x00]))
        # b.extend(struct.pack('<HHHH', 2, 96, 1, 0))
        b.extend(self.to_bytes(0x40))
        b.extend(self.to_bytes(0x40 + 4 * len(entries)))
        b.extend(b'\x00\x00\x00\x00')  # 待定 文件总长
        b.extend(self.to_bytes(len(entries)))
        b.extend(export_stamp)
        b.extend(b'\x00' * 28)
        # 偏移表
        b.extend(bytearray(4 * len(entries)))
        offset = 0
        for i, entry in enumerate(entries):
            struct.pack_into('<I', b, 0x40 + 4 * i, offset)
            b.extend(bytes([0x10, 0, 0x10, 0]))
            word_bytes = entry['word'].encode('utf-16le')
            code_bytes = entry['code'].encode('utf-16le')
            b.extend(self.to_bytes(len(code_bytes) + 18, 2))
            rank = entry['rank']
            if rank < 1:
                rank = 1
            b.append(rank)
            b.extend(b'\x06\x00\x00\x00\x00')
            b.extend(insert_stamp)
            b.extend(code_bytes)
            b.extend(b'\x00\x00')
            b.extend(word_bytes)
            b.extend(b'\x00\x00')
            offset += len(word_bytes) + len(code_bytes) + 20
        struct.pack_into('<I', b, 0x18, len(b))
        return bytes(b)

    def convert_entries_to_dat(self, entries, ms_dat_filename):
        marshaled_data = self.entries_to_bytes(entries)
        with open(ms_dat_filename, 'wb') as output_file:
            output_file.write(marshaled_data)


    def convert_dat_to_entries(self, dat_file_name):
        with open(dat_file_name, 'rb') as file:
            # 使用 dat_to_entries 方法读取数据
            return self.dat_to_entries(file)
