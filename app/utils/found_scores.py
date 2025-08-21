def calculate_rating(cells_opened: int, victory: bool) -> int:
    """
    Вычисляет количество очков за игру с учётом победы или поражения.
    """
    points = int(cells_opened * 0.2)  # 0.2 очко за каждую безопасную клетку

    if victory:
        points += 25  # бонус за победу
    else:
        points -= 20  # штраф за проигрыш

    return points
