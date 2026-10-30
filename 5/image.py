"""Модуль базового класса изображения"""
class Image:
    """Базовый класс изображения"""
    def __init__(self, title: str, width: int, height: int):
        """Инициализирует изображение с названием и размерами"""
        self._title = title
        self._width = width
        self._height = height

    def __str__(self) -> str:
        """Возвращает текстовое представление изображения"""
        return f"Изображение: {self._title}, {self._width}x{self._height}"
