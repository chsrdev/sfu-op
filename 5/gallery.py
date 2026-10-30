from image import Image

class Gallery:
    """Контейнер изображений"""
    def __init__(self):
        """Инициализирует пустой список изображений для галереи"""
        self._images: list[Image] = []

    def add(self, image: Image) -> None:
        """Добавляет в галерею новое изображение"""
        self._images.append(image)

    def pop(self, idx: int) -> Image:
        """Удаляет из галереии изображение по индексу"""
        return self._images.pop(idx)

    def __getitem__(self, index: int) -> Image:
        """Возвращает из галереии изображение по индексу"""
        return self._images[index]

    def __len__(self) -> int:
        """Возвращает количество элементов в изображении"""
        return len(self._images)
