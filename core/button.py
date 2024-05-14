from typing import Callable, Union

from pygame.surface import Surface
from pygame.font import Font
from pygame.locals import *
from pygame.event import Event
from pygame import rect
import pygame

from core.baseClasses import BaseDisplay
import commons


class Button(BaseDisplay):
    def __init__(
            self,
            event: Callable,
            label: str,
            position: tuple = (0, 0),
            color: Union[str, None] = commons.Colors.WHITE,
            border_width: int = 0,
            border_radius: int = 10, 
            font: str = None,
            font_size: int = 20,
            font_color: str = commons.Colors.BLACK,
            margin: Union[int, tuple] = 0,
            inner_margin: Union[int, tuple] = 10,
            ) -> None:

        # Label properties --------------------------------------------------------
        self.label = label
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self._font_color = font_color
        self.Font = Font(self.font, self.font_size)
        self.rendered_label = None

        # Button properties -------------------------------------------------------
        self.event = event
        self.hover = False
        self.button_rect = rect.Rect(0, 0, 0, 0)
        self.button_surface = None
        self.color = color
        self._color = color
        self.border_width = border_width
        self.border_radius = border_radius

        # Margin properties ---------------------------------------------------------  
        self.margin = margin if isinstance(margin, tuple) else tuple(margin for _ in range(4))
        self.inner_margin = inner_margin if isinstance(inner_margin, tuple) else tuple(inner_margin for _ in range(4))

        # Surface properties --------------------------------------------------------
        self._position = position
        self.surface = None


    def update(self) -> None:
        self.rendered_label = self.Font.render(self.label, True, self.font_color)
        self.button_rect = self.rendered_label.get_rect()
        self.button_rect.width += self.inner_margin[0] + self.inner_margin[2]
        self.button_rect.height += self.inner_margin[1] + self.inner_margin[3]
        self.button_surface = Surface(self.button_rect.size, SRCALPHA).convert_alpha()
        self.button_rect.x, self.button_rect.y = self._position[0] + self.margin[0], self._position[1] + self.margin[1]

        width = self.button_rect.width + self.margin[0] + self.margin[2]
        height = self.button_rect.height + self.margin[1] + self.margin[3]
        self.surface = Surface((width, height), SRCALPHA).convert_alpha()

        self.hover_handler()


    def events(self, event:Event) -> None:
        if event.type == MOUSEBUTTONDOWN:
            if commons.MouseEvents.mouse_pressed[0]:
                if rect.Rect.collidepoint(self.button_rect, commons.MouseEvents.mouse_pos):
                    self.event()                         
        
        if event.type == MOUSEMOTION:
                if rect.Rect.collidepoint(self.button_rect, commons.MouseEvents.mouse_pos):
                    self.hover = True
                else:
                    self.hover = False


    def render(self, display:Surface) -> None:
        if self.color is not None:
            pygame.draw.rect(self.button_surface, self.color, self.button_surface.get_rect(), border_radius=self.border_radius)
        self.button_surface.blit(self.rendered_label, self.inner_margin, self.button_surface.get_rect())
        self.surface.blit(self.button_surface, (self.margin[0], self.margin[1]))
        display.blit(self.surface, self.position)


    @property
    def position(self) -> tuple:
        return self._position
    
    @position.setter
    def position(self, position:tuple) -> None:
        self._position = position
        self.button_rect.x = self._position[0]
        self.button_rect.y = self._position[1]

    def hover_handler(self) -> None:
        if self.hover:
            if self.color is not None:
                self.color = pygame.Vector3(self._color) * 0.8
            self.font_color = pygame.Vector3(self._font_color) * 0.8
        else:
            self.color = self._color
            self.font_color = self._font_color