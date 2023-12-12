import pygame
from settings import *

class MapRenderer:
    def __init__(self, engine):
        self.engine = engine
        self.wad_data = self.engine.wad_data
        self.vertexes = self.wad_data.vertexes
        self.linedefs = self.wad_data.linedefs
        self.x_min, self.x_max, self.y_min, self.y_max = self.get_map_bounds()
        self.vertexes = [pygame.math.Vector2(self.remap_x(v.x), self.remap_y(v.y)) for v in self.vertexes]
    
    def draw(self):
        self.draw_vertexes()
        self.draw_linedefs()
        self.draw_player_pos()

    def draw_player_pos(self):
        pos = self.engine.PLAYER.pos
        x = self.remap_x(pos.x)
        y = self.remap_y(pos.y)
        pygame.draw.circle(self.engine.SCREEN, 'blue', (x, y), 4)
    
    def remap_x(self, n, out_min = 10, out_max = WIN_W - 10):
        return (max(self.x_min, min(n, self.x_max)) - self.x_min) * (out_max - out_min) / (self.x_max - self.x_min) + out_min
    
    def remap_y(self, n, out_min = 10, out_max = WIN_H - 10):
        return WIN_H - (max(self.y_min, min(n, self.y_max)) - self.y_min) * (out_max - out_min) / (self.y_max - self.y_min) + out_min
    
    def get_map_bounds(self):
        x_sorted = sorted(self.vertexes, key = lambda v: v.x)
        x_min, x_max = x_sorted[0].x, x_sorted[-1].x

        y_sorted = sorted(self.vertexes, key = lambda v: v.y)
        y_min, y_max = y_sorted[0].y, y_sorted[-1].y

        return x_min, x_max, y_min, y_max
    
    def draw_vertexes(self):
        for v in self.vertexes:
            pygame.draw.circle(self.engine.SCREEN, 'white', (v.x, v.y), 4)
    
    def draw_linedefs(self):
        for line in self.linedefs:
            p1 = self.vertexes[line.start_vertex_id]
            p2 = self.vertexes[line.end_vertex_id]
            pygame.draw.line(self.engine.SCREEN, 'orange', p1, p2, 3)