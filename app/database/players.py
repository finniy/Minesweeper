import sqlite3
import threading
import os

from app.utils.found_scores import calculate_rating


class PlayerDB:
    def __init__(self):
        """
        Создает базу данных и таблицу игроков, если нет.
        """
        root_dir = os.path.abspath(os.getcwd())
        self.db_path = os.path.join(root_dir, 'database.db')
        self.lock = threading.Lock()
        self.create_table()

    def get_connection(self):
        """
        Возвращает новое соединение с базой данных.
        """
        return sqlite3.connect(self.db_path, check_same_thread=False)

    def create_table(self):
        """
        Создает таблицу игроков, если её ещё нет.
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS players (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    games_played INTEGER DEFAULT 0,
                    wins INTEGER DEFAULT 0,
                    losses INTEGER DEFAULT 0,
                    rating INTEGER DEFAULT 1000
                )
            ''')
            conn.commit()

    def add_or_update_player(self, user_id: int, username: str):
        """
        Добавляет игрока или обновляет его имя пользователя.
        """
        with self.lock:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM players WHERE user_id = ?', (user_id,))
                if cursor.fetchone() is None:
                    cursor.execute(
                        'INSERT INTO players (user_id, username, rating) VALUES (?, ?, ?)',
                        (user_id, username, 1000)
                    )
                else:
                    cursor.execute('UPDATE players SET username = ? WHERE user_id = ?', (username, user_id))
                conn.commit()

    def update_after_game(self, user_id: int, cells_opened: int, victory: bool):
        """
        Обновляет статистику и рейтинг игрока после игры.
        """
        points = calculate_rating(cells_opened, victory)
        with self.lock:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT games_played, wins, losses, rating FROM players WHERE user_id = ?', (user_id,))
                data = cursor.fetchone()
                games_played, wins, losses, rating = data
                games_played += 1
                wins += 1 if victory else 0
                losses += 0 if victory else 1
                rating += points
                cursor.execute('''
                    UPDATE players 
                    SET games_played = ?, wins = ?, losses = ?, rating = ? 
                    WHERE user_id = ?
                ''', (games_played, wins, losses, rating, user_id))
                conn.commit()

    def get_top_players(self, limit=10):
        """
        Возвращает топ игроков по рейтингу, ограничение задаётся параметром limit.
        """
        with self.lock:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT user_id, username, games_played, wins, losses, rating
                    FROM players
                    ORDER BY rating DESC
                    LIMIT ?
                ''', (limit,))
                return cursor.fetchall()

    def get_player_profile(self, user_id: int):
        """
        Возвращает статистику и рейтинг одного игрока.
        """
        with self.lock:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT username, games_played, wins, losses, rating 
                    FROM players 
                    WHERE user_id = ?
                ''', (user_id,))
                data = cursor.fetchone()
                if data:
                    username, games_played, wins, losses, rating = data
                    return {
                        "games_played": games_played,
                        "wins": wins,
                        "losses": losses,
                        "rating": rating
                    }
                return None
