from settings import *

class BSP:
    SUB_SECTOR_IDENTIFIER = 0x8000
    def __init__(self, engine):
        self.engine = engine
        self.PLAYER = engine.PLAYER
        self.nodes = engine.wad_data.nodes
        self.sub_sectors = engine.wad_data.sub_sectors
        self.segs = engine.wad_data.segments
        self.root_node_id = len(self.nodes) - 1

    def update(self):
        self.render_nodes(self.root_node_id)
    
    def render_sub_sector(self, sub_sector_id):
        sub_sector = self.sub_sectors[sub_sector_id]
        for i in range(sub_sector.seg_count):
            seg = self.segs[sub_sector.first_seg_id + i]
            self.engine.map_renderer.draw_seg(seg, sub_sector_id)

    def render_nodes(self, node_id):
        if node_id>= self.SUB_SECTOR_IDENTIFIER:
            sub_sector_id = node_id - self.SUB_SECTOR_IDENTIFIER
            self.render_sub_sector(sub_sector_id)
            return None
        
        node = self.nodes[node_id]
        is_on_back = self.is_on_back_side(node)
        if is_on_back:
            self.render_nodes(node.back_child_id)
            self.render_nodes(node.front_child_id)
        else:
            self.render_nodes(node.front_child_id)
            self.render_nodes(node.back_child_id)

    def is_on_back_side(self, node):
        dx = self.PLAYER.pos.x - node.x_partition
        dy = self.PLAYER.pos.y - node.y_partition
        return dx * node.dy_partition - dy * node.dx_partition <= 0