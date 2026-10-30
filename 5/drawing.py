"""Модуль класса рисунка"""
from image import Image

class Drawing(Image):
    """Класс рисунка"""
    def __init__(self, title: str, width: int, height: int, tool: str):
        super().__init__(title, width, height)
        self._tool = tool

    def __str__(self):
        return (f"Рисунок: {self._title}, {self._width}x{self._height}."
                f"\nНарисовано с помощью: {self._tool}")
