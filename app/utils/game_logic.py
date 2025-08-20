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
        self.opened_cells_count = 0
        self.board = [[Cell(r, c) for c in range(self.cols)] for r in range(self.rows)]

        # Методы
        self._place_mines(self.mines)
        self._calculate_neighbours()
        self._game_over = False
        self.first_move = True

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

    def open_clear_cell(self, row: int, col: int) -> bool | str:
        """Открывает клетку и рекурсивно соседние пустые."""
        cell = self.board[row][col]

        # Защита от первой мины
        if self.first_move:
            self.first_move = False
            if cell.mine:
                cell.mine = False
                while True:
                    r = random.randint(0, self.rows - 1)
                    c = random.randint(0, self.cols - 1)
                    if not self.board[r][c].mine and (r, c) != (row, col):
                        self.board[r][c].mine = True
                        break

                self._calculate_neighbours()

        if cell.opened:
            return 'opened'  # Уже открыта
        cell.opened = True

        if cell.mine:
            self._game_over = True
            return 'blow'

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

        self.opened_cells_count += 1

        return True

    def check_victory(self) -> bool:
        """
        Проверяет, выиграл ли игрок.
        """
        count_closed = 0
        for row in self.board:
            for cell in row:
                if not cell.opened:
                    count_closed += 1
        if count_closed == self.mines:
            return True
        return False
