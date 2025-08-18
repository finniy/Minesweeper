import random


class Cell:
    """Клетка игрового поля."""

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.mine = False
        self.neighbours = 0
        self.opened = False


class Game:
    def __init__(self, mines: int):
        # Атрибуты
        self.rows = 8
        self.cols = 8
        self.mines = mines
        self.board = [[Cell(r, c) for c in range(self.cols)] for r in range(self.rows)]

        # Методы
        self._place_mines(self.mines)
        self._calculate_neighbours()
        self._game_over = False

    def _place_mines(self, count_bombs: int) -> None:
        """Случайно расставляет мины на поле."""
        all_positions = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        mine_positions = random.sample(all_positions, count_bombs)
        for r, c in mine_positions:
            self.board[r][c].mine = True

    def _calculate_neighbours(self) -> None:
        """Считает количество мин вокруг каждой клетки."""
        for r in range(self.rows):
            for c in range(self.cols):
                neighbours = [
                    (r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                    (r, c - 1), (r, c + 1),
                    (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)
                ]
                if not self.board[r][c].mine:
                    count = 0
                    for x, y in neighbours:
                        if 0 <= x < self.rows and 0 <= y < self.cols:
                            if self.board[x][y].mine:
                                count += 1
                    self.board[r][c].neighbours = count

    def open_clear_cell(self, row: int, col: int) -> bool:
        """Открывает клетку и рекурсивно соседние пустые."""
        # Перед вызовом проверка не бомба!
        cell = self.board[row][col]
        if cell.opened:
            return False  # Уже открыта
        cell.opened = True

        if cell.mine:
            self._game_over = True
            return False

        # Если это пустая клетка, открываем соседей
        if cell.neighbours == 0:
            neighbours = [
                (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                (row, col - 1), (row, col + 1),
                (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
            ]
            for nr, nc in neighbours:
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    neighbour_cell = self.board[nr][nc]
                    if not neighbour_cell.opened and not neighbour_cell.mine:
                        self.open_clear_cell(nr, nc)  # рекурсивно открываем

        return True
