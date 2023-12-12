import sys
import pygame
from logger import logger
from wadData import WADData
from settings import *
from map_renderer import MapRenderer
from player import Player
from bsp import BSP

class DoomEngine:
    def __init__(self, wad_path = "../wad/DOOM1.WAD"):
        logger.info("--------------------")
        logger.info("STARTED GAME ENGINE!")
        self.SCREEN = pygame.display.set_mode((WIN_RES))
        self.CLOCK = pygame.time.Clock()
        self.RUNNING = True
        self.dT = 1 / 60

        self.wad_path = wad_path
        self.wad_data = WADData(self, map_name = "E1M1")
        self.map_renderer = MapRenderer(self)
        self.PLAYER = Player(self)
        self.BSP = BSP(self)

        logger.info("READ WAD FILE SUCCESSFULLY!")
    
    def update(self):
        self.PLAYER.update()
        self.BSP.update()
        self.dT = self.CLOCK.tick()
        pygame.display.set_caption(f"FPS: {int(self.CLOCK.get_fps())}")
    
    def draw(self):
        pygame.display.flip()
        self.SCREEN.fill("black")
        self.map_renderer.draw()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False
    
    def run(self):
        logger.info("RUNNING GAME...")
        while self.RUNNING:
            self.check_events()
            self.update()
            self.draw()
        logger.info("EXITING...")
        pygame.quit()
        logger.info("QUIT!")
        logger.info("--------------------")
        sys.exit()


if __name__ == "__main__":
    doom = DoomEngine()
    doom.run()