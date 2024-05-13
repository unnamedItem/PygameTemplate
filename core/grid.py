from pygame.surface import Surface

class Flex():
    def __init__(self) -> None:
        pass

class Col():
    def __init__(self, surface: Surface, n_cols: int) -> None:
        self.surface = surface
        self.width = surface.get_width()
        self.height = surface.get_height()
        self.n_cols = n_cols

    def render(self, display: Surface) -> None:
        for col in range(self.n_cols):
            display.blit(self.surface, (self.get_col(col), 0))

    def get_col(self, col: int) -> float:
        return self.surface.get_width() * col / self.n_cols

class Row():
    def __init__(self, *cols: list[Col]) -> None:
        self.cols = cols

    def render(self, display: Surface) -> None:
        for col in self.cols:
            col.render(display)

class Grid():
    def __init__(self, *rows: list[Row]) -> None:
        self.rows = rows

    def render(self, display: Surface) -> None:
        for row in self.rows:
            row.render(display)