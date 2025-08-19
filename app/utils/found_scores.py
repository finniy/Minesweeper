def calculate_rating(cells_opened: int, victory: bool) -> int:
    """
    Вычисляет количество очков за игру с учётом победы или поражения.
    """

    if victory:
        points = int(cells_opened * 0.5)  # 0.5 очко за каждую безопасную клетку
        points += 15  # бонус за победу
    else:
        points = -20  # штраф за проигрыш

    return points
