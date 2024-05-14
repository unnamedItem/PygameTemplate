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