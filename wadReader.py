import struct

class WADReader:
    def __init__(self, wad_path):
        self.wad_path = wad_path
        self.wad_file = open(self.wad_path, "rb")
        self.header = self.read_header()
        print(list(self.header.items()), sep = "\n")
    
    def read_header(self):
        return {
            'wad_type': self.read_string(0, 4),  # TYPE OF WAD
            'lump_count': self.read_4_bytes(4),  # NUMBER OF ASSETS
            'init_offset': self.read_4_bytes(8), # START POINTER FOR ASSETS
        }

    def read_4_bytes(self, offset, byte_format = 'i'):
        '''
        byte_format = "i" for int32, "I" for uint32
        '''
        return self.read_bytes(offset, 4, byte_format)[0]
    
    def read_string(self, offset, num_bytes):
        return "".join(b.decode('ascii') for b in 
                       self.read_bytes(offset, num_bytes, "c" * num_bytes)
                       if ord(b) != 0).upper()

    def read_bytes(self, offset, num_bytes, byte_format):
        self.wad_file.seek(offset)
        buffer = self.wad_file.read(num_bytes)
        return struct.unpack(byte_format, buffer)
    
    def close(self):
        self.wad_file.close()