# H: uint16, h: int16, I: uint32, i: int32, c: char

class Thing:
    # 10 bytes = 4h + 2H * 3
    __slots__ = [
        'pos',
        'angle',
        'type',
        'flags'
    ]

class Seg:
    # 12 bytes = 2h * 6
    __slots__ = [
        'start_vertex_id',
        'end_vertex_id',
        'angle',
        'linedef_id',
        'direction',
        'offset'
    ]

class SubSector:
    # 4 bytes = 2h + 2h
    __slots__ = [
        'seg_count', 
        'first_seg_id'
    ]


class Node:
    # 28 bytes = 2h * 12 + 2H * 2
    class BBox:
        __slots__ = ['top', 'bottom', 'left', 'right']

    __slots__ = [
        "x_partition",
        "y_partition",
        "dx_partition",
        "dy_partition",
        'bbox',
        'front_child_id',
        'back_child_id'
    ]

    def __init__(self) -> None:
        self.bbox = {'front': self.BBox(), 'back': self.BBox()}

class LineDef:
    __slots__ = [
        'start_vertex_id',
        'end_vertex_id',
        'flags',
        'line_type',
        'sector_tag',
        'front_sidedef_id',
        'back_sidedef_id'
    ]