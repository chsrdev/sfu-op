from gallery import Gallery
from drawing import Drawing
from photo import Photo
from image import Image
from screenshot import Screenshot

def gallery_menu(gallery: Gallery):
    current_idx = 0
    while True:
        if len(gallery) == 0:
            print("Галерея пуста\n"
                  "Добавьте хотя бы одно изображение")
            return
        
        print(gallery[current_idx])
        action = input("\n1. Следующее изображение\n"
                       "2. Предыдущее изображение\n"
                       "3. Удалить\n"
                       "4. Выйти\n"
                       ">>> ")
        match action:
            case "1":
                current_idx = (current_idx + 1) % len(gallery)
            case "2":
                current_idx = (current_idx - 1) % len(gallery)
            case "3":
                print("Удалено:")
                print(gallery.pop(current_idx))
                if len(gallery) > 0:
                    current_idx %= len(gallery)
            case "4":
                break


def image_create_menu() -> Image:
    while True:
        try:
            title = input("\nВведите название изображения: ").strip()
            if not title:
                print("Название не может быть пустым")
                continue

            width = int(input("Введите ширину изображения: "))
            height = int(input("Введите высоту изображения: "))

            if width <= 0 or height <= 0:
                print("Ширина и высота должны быть положительными числами")
                continue

            image_type = int(input("Выберите тип изображения\n"
                            "1. Рисунок\n"
                            "2. Фотография\n"
                            "3. Скриншот\n"
                            ">>> "))
            match image_type:
                case 1:
                    tool = input("Введите инструмент создания рисунка "
                                       "(карандаш, ручка, кисть): ")
                    return Drawing(title, width, height, tool)
                case 2:
                    size = int(input("Введите вес фотографии (КБ.): "))
                    if size <= 0:
                        print("Вес фотографии должен быть положительным числом")
                        continue
                    camera = input("Введите название камеры: ")
                    return Photo(title, width, height, size, camera)
                case 3:
                    size = int(input("Введите вес скриншота (КБ.): "))
                    if size <= 0:
                        print("Вес скриншота должен быть положительным числом")
                        continue
                    app = input("Введите название приложения: ")
                    return Screenshot(title, width, height, size, app)
                case _:
                    print("Выберите число от 1 до 3")
        except ValueError:
            print("Ошибка: нужно вводить число")


def main_menu(gallery: Gallery):
    while True:
        action = input("\n1. Посмотреть галерею\n"
                       "2. Добавить изображение\n"
                       "3. Выйти\n"
                       ">>> ")

        match action:
            case "1":
                gallery_menu(gallery)
            case "2":
                new_image = image_create_menu()
                gallery.add(new_image)
                print("Создано:")
                print(new_image)
            case "3":
                break