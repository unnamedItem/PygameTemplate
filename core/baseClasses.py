from pygame.surface import Surface
from pygame.rect import Rect
from pygame.event import Event

class BaseClass:
    def events(self, event: Event) -> None:
        pass

    def render(self, display: Surface) -> None:
        pass

    def update(self) -> None:
        pass

class BaseDisplay(BaseClass):
    def __init__(self) -> None:
        self.surface:Surface
        self.rect:Rect
        self.screen_pos:tuple = (0,0)
        self.screen_rect = Rect(0,0,0,0)

    def set_display(self, position: tuple = (0,0)) -> None:
        '''Set display position and rect on the screen'''
        self.screen_pos = position
        self.screen_rect.x, self.screen_rect.y = self.screen_pos