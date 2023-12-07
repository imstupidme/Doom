from logger import logger
from wadData import WADData

class DoomEngine:
    def __init__(self, wad_path = "./wad/DOOM1.WAD"):
        logger.info("")
        logger.info("STARTED GAME ENGINE!")
        self.wad_path = wad_path
        self.wad_data = WADData(self, map_name = "E1M1")
        logger.info("READ WAD FILE SUCCESSFULLY!")


if __name__ == "__main__":
    doom = DoomEngine()