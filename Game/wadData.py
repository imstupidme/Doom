from wadReader import WADReader

class WADData:
    LUMP_INDICES = {
        "THINGS": 1, "LINEDEFS": 2, "SIDEDEFS": 3, "VERTEXES": 4, "SEGS": 5, 
        "SSECTORS": 6, "NODES": 7, "SECTORS": 8, "REJECT": 9, "BLOCKMAP": 10
    }

    def __init__(self, engine, map_name) -> None:
        self.reader = WADReader(engine.wad_path)
        self.map_index = self.get_lump_index(map_name)
        self.vertexes = self.get_lump_data(
            self.reader.read_vertex, 
            self.map_index + self.LUMP_INDICES["VERTEXES"],
            4
        )
        self.linedefs = self.get_lump_data(
            self.reader.read_linedef, 
            self.map_index + self.LUMP_INDICES["LINEDEFS"],
            14
        )

        self.nodes = self.get_lump_data(
            self.reader.read_node,
            self.map_index + self.LUMP_INDICES["NODES"],
            28
        )
        
        self.sub_sectors = self.get_lump_data(
            self.reader.read_sub_sector,
            self.map_index + self.LUMP_INDICES["SSECTORS"],
            4
        )
        self.segments = self.get_lump_data(
            self.reader.read_segment,
            self.map_index + self.LUMP_INDICES["SEGS"],
            12
        )
        self.things = self.get_lump_data(
            self.reader.read_things,
            self.map_index + self.LUMP_INDICES["THINGS"],
            10
        )
        
        self.reader.close()
    
    @staticmethod
    def print_attrs(obj):
        print()
        for attr in obj.__slots__:
            print(eval(f"obj.{attr}"), end = " ")

    def get_lump_data(self, reader_func, lump_index, num_bytes, header_length = 0):
        lump_info = self.reader.directory[lump_index]
        count = lump_info["lump_size"] // num_bytes
        data = []
        for i in range(count):
            offset = lump_info["lump_offset"] + header_length + i*num_bytes
            data.append(reader_func(offset))
        return data

    def get_lump_index(self, lump_name):
        for i, lump_info in enumerate(self.reader.directory):
            if lump_name in lump_info.values():
                return i