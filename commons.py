import os

# --------------------------------------------------------------------------------------
# System
class System(object):
    dt:float = 0.0
    MAX_TICKS = 140
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    STAGES_DIR = "stages"

# --------------------------------------------------------------------------------------
# Extensions
class Extensions(object):
    PY = ".py"

# --------------------------------------------------------------------------------------
# Mouse events
class MouseEvents(object):
    mouse_pos:tuple = (0.0,0.0)
    mouse_pressed:list = (False, False, False)

# --------------------------------------------------------------------------------------
# Display
class Display(object):
    display_w:int = 800
    display_h:int = 600
    display_size:tuple = (display_w, display_h)

class VerticalAlign(object):
    TOP = 0
    CENTER = 1
    DOWN = 2

class HorizontalAlign(object):
    RIGHT = 0
    MIDDLE = 1
    LEFT = 2

# --------------------------------------------------------------------------------------
# Colors
class Colors(object):
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    BACKGROUND_COLOR = (30,20,30)

# --------------------------------------------------------------------------------------
# Misc
