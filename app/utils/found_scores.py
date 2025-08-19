def calculate_rating(cells_opened: int, victory: bool) -> int:
    """
    Вычисляет количество очков за игру с учётом победы или поражения.
    """

    if victory:
        points = cells_opened  # 1 очко за каждую безопасную клетку
        points += 10  # бонус за победу
    else:
        points = -15  # штраф за проигрыш

    return points
