from pygame.surface import Surface
from pygame.event import Event
from pygame import SRCALPHA, DOUBLEBUF

from core.baseClass import BaseClass
import commons

class Flex():
    def __init__(self) -> None:
        pass

class Col():
    def __init__(self, content: BaseClass) -> None:
        self.content = content
        self.width = 0
        self.height = 0
        self.surface = Surface((self.width, self.height), flags=SRCALPHA)

    def events(self, event: Event) -> None:
        self.content.events(event)

    def update(self) -> None:
        self.content.update()
        self.width = self.content.surface.get_width()
        self.height = self.content.surface.get_height()
        self.surface = Surface((self.width, self.height), flags=SRCALPHA)

    def render(self, display: Surface, position: tuple = (0,0)) -> None:
        self.content.render(self.surface)
        display.blit(self.surface, position)

class Row():
    def __init__(self, *cols: 'list[Col]') -> None:
        self.cols: 'list[Col]' = cols
        self.width = commons.Display.display_w
        self.height = max(col.height for col in self.cols)
        self.rsurface = Surface((self.width, self.height), flags=SRCALPHA)

    def events(self, event: Event) -> None:
        for col in self.cols:
            col.events(event)

    def update(self) -> None:
        self.width = commons.Display.display_w
        self.height = max(col.height for col in self.cols)
        self.rsurface = Surface((self.width, self.height), flags=SRCALPHA)
        for col in self.cols:
            col.update()

    def render(self, display: Surface, position: tuple = (0,0)) -> None:
        x = 0
        for col in self.cols:
            col.render(self.rsurface, (x,0))
            x += col.width
        display.blit(self.rsurface, position)
        

class Grid():
    def __init__(self, *rows: 'list[Row]') -> None:
        self.rows: 'list[Row]' = rows
        self.gsurface = Surface(commons.Display.display_size, flags=SRCALPHA)

    def events(self, event: Event) -> None:
        for row in self.rows:
            row.events(event)

    def update(self) -> None:
        for row in self.rows:
            row.update()

    def render(self, display: Surface) -> None:
        y = 0
        for row in self.rows:
            row.render(self.gsurface, (0,y))
            y += row.height
        display.blit(self.gsurface, (0,0))