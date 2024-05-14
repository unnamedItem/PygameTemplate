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
            postion: tuple = (0, 0),
            color: Union[str, None] = commons.Colors.WHITE,
            border_width: int = 0,
            border_radius: int = 10,
            margin: Union[int, tuple] = 0,
            inner_margin: Union[int, tuple] = 10,
            font: str = None,
            font_size: int = 20,
            font_color: str = commons.Colors.BLACK,
            ) -> None:
        super().__init__()

        # Label properties --------------------------------------------------------
        self.label = label
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self._font_color = font_color
        self.Font = Font(self.font, self.font_size)
        self.rendered_label = self.Font.render(self.label, True, self.font_color)

        # Button properties -------------------------------------------------------
        self.event = event
        self.hover = False
        self.color = color
        self._color = color
        self.border_width = border_width
        self.border_radius = border_radius
        self.button_surface = None

        # Margin properties ---------------------------------------------------------  
        self.margin = margin if isinstance(margin, tuple) else tuple(margin for _ in range(4))
        self.inner_margin = inner_margin if isinstance(inner_margin, tuple) else tuple(inner_margin for _ in range(4))

        # Set display --------------------------------------------------------------
        self.position = postion
        self.set_display(self.position)


    def update(self) -> None:
        self.hover_handler()


    def events(self, event:Event) -> None:
        if event.type == MOUSEBUTTONDOWN:
            if commons.MouseEvents.mouse_pressed[0]:
                if rect.Rect.collidepoint(self.screen_rect, commons.MouseEvents.mouse_pos):
                    self.event()                         
        
        if event.type == MOUSEMOTION:
                if rect.Rect.collidepoint(self.screen_rect, commons.MouseEvents.mouse_pos):
                    self.hover = True
                else:
                    self.hover = False


    def render(self, display:Surface) -> None:
        # Render label
        self.rendered_label = self.Font.render(self.label, True, self.font_color)

        # Draw button rect
        if self.color is not None:
            pygame.draw.rect(self.button_surface, self.color, self.button_surface.get_rect(), border_radius=self.border_radius)
            
        # Draw button
        self.button_surface.blit(self.rendered_label, self.inner_margin, self.button_surface.get_rect())
        self.surface.blit(self.button_surface, (self.margin[0], self.margin[1]))
        display.blit(self.surface, self.position)

    def set_display(self, position: tuple = (0,0)) -> None:
        # Set rect
        self.rect = self.rendered_label.get_rect()
        self.rect.width += self.inner_margin[0] + self.inner_margin[2]
        self.rect.height += self.inner_margin[1] + self.inner_margin[3]

        # Set button surface
        self.button_surface = Surface(self.rect.size, SRCALPHA).convert_alpha()

        # Set screen rect
        self.screen_rect = self.button_surface.get_rect()
        super().set_display(position)

        # Set surface with margin
        self.rect.x, self.rect.y = self.margin[0], self.margin[1]
        width = self.rect.width + self.margin[0] + self.margin[2]
        height = self.rect.height + self.margin[1] + self.margin[3]
        self.surface = Surface((width, height), SRCALPHA).convert_alpha()

    def hover_handler(self) -> None:
        if self.hover:
            if self.color is not None:
                self.color = pygame.Vector3(self._color) * 0.8
            self.font_color = pygame.Vector3(self._font_color) * 0.8
        else:
            self.color = self._color
            self.font_color = self._font_color