import pygame
from pygame.surface import Surface
from pygame.font import Font
from pygame.locals import *
from pygame.event import Event

from core.stage import Stage
from core.button import Button
from core.dialogBoxes import DialogBox
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


class Stage2(Stage):
    def __init__(self, manager):
        super().__init__(manager)
        self.font_title:Font = Font(None, 80)
        self.font_options:Font = Font(None, 40)
        self.title:list = [('STAGE 2', True, commons.Colors.WHITE), (60,60), pygame.rect.Rect(0,0,0,0)]
        self.options:list[Button] = [
            CustomButton(self.event_end, "End", (60, 400), None, font_size=40, inner_margin=0, font_color=commons.Colors.WHITE),
            CustomButton(self.event_dialog, "Dialog", (60, 440), None, font_size=40, inner_margin=0, font_color=commons.Colors.WHITE),
        ]
        self.dialog_box = DialogBox()


    def update(self) -> None:
        for option in self.options:
            option.update()
        self.dialog_box.update(commons.System.dt)

    def events(self, event:Event) -> None:
        for option in self.options:
            option.events(event)
        self.dialog_box.process_event(event)

    def render(self, display: Surface) -> None:
        self.title[2] = display.blit(self.font_title.render(*self.title[0]), self.title[1])
        for option in self.options:
            option.render(display)
        self.dialog_box.render(display)

    def event_end(self):
        self.manager.deactivate_stage(stages.StagesName.Stage2)
        self.manager.activate_stage(stages.StagesName.MainMenu)

    def event_dialog(self):
        text = f'''\
            Esto es un cuadro de dialogo de prueba\n
            Algunas lineas extas...\n
            Fin del dialogo.
        '''
        self.dialog_box.new_dialog(text, border_radius=10)
