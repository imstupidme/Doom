from wadData import WADData

class DoomEngine:
    def __init__(self, wad_path = "./wad/DOOM1.WAD"):
        self.wad_path = wad_path
        self.wad_file = WADData(self)

if __name__ == "__main__":
    doom = DoomEngine()