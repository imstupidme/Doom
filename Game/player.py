from settings import *
from pygame.math import Vector2
import pygame

class Player:
    def __init__(self, engine):
        self.engine = engine
        self.thing = engine.wad_data.things[0]
        self.pos = self.thing.pos
        self.angle = self.thing.angle
    
    def update(self):
        self.control()

    def control(self):
        speed = PLAYER_SPEED * self.engine.dT
        rot_speed = PLAYER_ROT_SPEED * self.engine.dT

        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.angle += rot_speed
        elif key_state[pygame.K_RIGHT]:
            self.angle -= rot_speed
        
        inc = Vector2(0)
        if key_state[pygame.K_a]:
            inc += Vector2(0, speed).rotate(self.angle)
        elif key_state[pygame.K_d]:
            inc += Vector2(0, -speed).rotate(self.angle)
        elif key_state[pygame.K_w]:
            inc += Vector2(speed, 0).rotate(self.angle)
        elif key_state[pygame.K_s]:
            inc += Vector2(-speed, 0).rotate(self.angle)
        
        if inc.x and inc.y:
            inc *= 1 / math.sqrt(2)

        self.pos += inc