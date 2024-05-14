import os
import sys
import importlib.util
from pathlib import Path

from core.baseClasses import BaseClass
import commons


class Stage(BaseClass):
    def __init__(self, Manager) -> None:
        self.manager:StageManager = Manager
        self.active = False
        self.priority = 0

    def start_stage(self) -> None:
        pass
    
    def end_stage(self) -> None:
        pass


class StageManager:
    def __init__(self, path:str) -> None:
        self.dirpath = os.path.join(commons.System.ROOT_DIR, path)
        self.dirfiles = os.listdir(self.dirpath)
        self.stages:list[Stage] = []
        self.load_stages()
    
    def load_stages(self) -> None:
        files = filter(lambda f: commons.Extensions.PY in f and f != '__init__.py', self.dirfiles)
        for file in files:
            filepath = os.path.join(self.dirpath, file)
            filename = Path(filepath).stem
            spec = importlib.util.spec_from_file_location(filename, filepath)
            module = importlib.util.module_from_spec(spec)
            sys.modules[filename] = module
            spec.loader.exec_module(module)
            Stage = module.__getattribute__(filename)
            self.stages.append(Stage(self))
        self.register_stages()

    @property
    def active_stages(self) -> 'list[Stage]':
        return list(sorted(filter(lambda stage: stage.active, self.stages), key=lambda x: x.priority, reverse=True))
    
    def get_stage(self, name:str) -> Stage:
        stage = list(filter(lambda st: st.__module__ == name, self.stages))
        if stage:
            return stage[0]
        print(f'Stage "{name}" not in: "{self.dirpath}"')
        return None
    
    def register_stages(self):
        filepath = os.path.join(self.dirpath, '__init__.py')
        with open(filepath, 'w') as f:
            f.write('class StagesName(object):\n')
            for stage in self.stages:
                f.write(f'\t{stage.__module__} = "{stage.__module__}"\n')

    def activate_stage(self, name:str) -> Stage:
        stage = self.get_stage(name)
        stage.active = True
        stage.start_stage()
    
    def deactivate_stage(self, name:str) -> Stage:
        stage = self.get_stage(name)
        stage.active = False
        stage.end_stage()