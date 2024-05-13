from pygame.surface import Surface
from pygame.event import Event

class BaseClass:
    def __init__(self) -> None:
        self.surface:Surface

    def events(self, event: Event) -> None:
        pass

    def render(self, display: Surface) -> None:
        pass

    def update(self) -> None:
        pass