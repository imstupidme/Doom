from wadReader import WADReader

class WADData:
    def __init__(self, engine) -> None:
        self.reader = WADReader(engine.wad_path)
        self.reader.close()