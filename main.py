import pygame, sys, time
from pygame.locals import *

pygame.init()

import commons
import stages
from core.stage import StageManager


class Game:
    def __init__(self) -> None:
        self.isRunning:bool = True

        self.display:pygame.Surface = pygame.display.set_mode(commons.Display.display_size, DOUBLEBUF)

        self.main_clock:pygame.time.Clock = pygame.time.Clock()
        self.last_time:float = time.time()
        self.fps_max:float = commons.System.MAX_TICKS
        self.fps:float = self.main_clock.get_fps()

        self.stage_manager = StageManager(commons.System.STAGES_DIR)
        self.stage_manager.activate_stage(stages.StagesName.MainMenu)


    def run(self) -> None:
        while self.isRunning:
            self.events()
            self.update()
            self.render()


    def events(self) -> None:
        for event in pygame.event.get():            
            if event.type == QUIT:
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                commons.MouseEvents.mouse_pressed = pygame.mouse.get_pressed()

            if event.type == MOUSEBUTTONUP:
                commons.MouseEvents.mouse_pressed = pygame.mouse.get_pressed()

            if event.type == MOUSEMOTION:
                commons.MouseEvents.mouse_pos = pygame.mouse.get_pos()

            for stage in self.stage_manager.active_stages:
                stage.events(event)


    def update(self) -> None:
        commons.System.dt = self.delta_time()
        for stage in self.stage_manager.active_stages:
            stage.update()


    def render(self) -> None:
        self.display.fill(commons.Colors.BACKGROUND_COLOR)
        fps = pygame.font.Font(None, 40).render(str(int(self.fps)), True, commons.Colors.WHITE)
        self.display.blit(fps, (commons.Display.display_w - fps.get_size()[0] - 20,20))

        for stage in self.stage_manager.active_stages:
            stage.render(self.display)   

        pygame.display.flip()

    
    def delta_time(self) -> float:
        self.main_clock.tick(self.fps_max)
        self.fps = self.main_clock.get_fps()
        dt = time.time() - self.last_time
        self.last_time = time.time()
        return dt


Game().run()