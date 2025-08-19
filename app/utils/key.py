import string
import random


def generate_game_key(length: int = 6) -> str:
    """Генерирует уникальный ключ из заглавных букв и цифр заданной длины."""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))
