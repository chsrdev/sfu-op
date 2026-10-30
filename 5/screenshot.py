"""Модуль класса скриншота"""
from image import Image

class Screenshot(Image):
    """Класс скриншота"""
    def __init__(self,
                 title: str,
                 width: int,
                 height: int,
                 size_kb: int,
                 app_name: str):
        super().__init__(title, width, height)
        self._size = size_kb
        self._app_name = app_name

    def __str__(self):
        return (f"Скриншот: {self._title}, {self._width}x{self._height}, "
                f"{self._size}КБ.\nИз приложения: {self._app_name}")
