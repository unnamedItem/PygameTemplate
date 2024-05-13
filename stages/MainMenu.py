import sys
import pygame
from pygame.surface import Surface
from pygame.font import Font
from pygame.locals import *
from pygame.event import Event

from core.stage import Stage
from core.button import Button
import commons
import stages

class CustomButton(Button):
    def hover_handler(self) -> None:
        if self.hover:
            if self.color is not None:
                self.color = commons.Colors.WHITE
            self.font_color = commons.Colors.GREEN
        else:
            self.color = self._color
            self.font_color = self._font_color


class MainMenu(Stage):
    def __init__(self, manager):
        super().__init__(manager)
        self.font_title:Font = Font(None, 80)
        self.title:list = [('MENU', True, commons.Colors.WHITE), (60,60), pygame.rect.Rect(0,0,0,0)]
        self.options:list[Button] = [
            CustomButton(self.event_start, "Start", (60, 400), None, font_size=40, inner_margin=0, font_color=commons.Colors.WHITE),
            CustomButton(self.event_exit, "Exit", (60, 440), None, font_size=40, inner_margin=0, font_color=commons.Colors.WHITE),
        ]

    def update(self) -> None:
        for option in self.options:
            option.update()

    def events(self, event:Event) -> None:
        for option in self.options:
            option.events(event)

    def render(self, display: Surface) -> None:
        self.title[2] = display.blit(self.font_title.render(*self.title[0]), self.title[1])
        for option in self.options:
            option.render(display)

    def event_start(self):
        self.manager.deactivate_stage(stages.StagesName.MainMenu)
        self.manager.activate_stage(stages.StagesName.Stage1)

    def event_exit(self):
        sys.exit()