from image import Image

class Photo(Image):
    """Класс фотографии"""
    def __init__(self, title: str, width: int, height: int, size_kb: int, camera_name: str):
        super().__init__(title, width, height)
        self._size = size_kb
        self._camera_name = camera_name

    def __str__(self):
        return (f"Фотография: {self._title}, {self._width}x{self._height}, {self._size}КБ."
                f"\nСнято на: {self._camera_name}")
    