"""Модуль управления меню программы"""
import cities
from tools import cities_to_str, city_to_str

def add() -> None:
    """Запрашивает у пользователя нужные данные 
    и пробует добавить город в список"""
    try:
        cities.add(
            city=input("Название нового города: "),
            foundation_year=int(input("Год основания города: ")),
            population_thousands=int(input("Население города в тыс. чел.: ")),
            country=input("Название страны: ")
        )
    except ValueError as e:
        print(f"Ошибка: {e}")


def remove() -> None:
    """Запрашивает у пользователя нужные данные 
    и пробует удалить город из списка"""
    try:
        city = cities.remove(input("Название города для удаления: "))
        print(f'Удален {city_to_str(city)}')
    except KeyError as e:
        print(e)


def find() -> None:
    """Запрашивает у пользователя название города 
    и пробует найти его в списке"""
    city = cities.find_by_city(input("Название города: "))
    if city:
        print(f'Найден {city_to_str(city)}')
    else:
        print("Город не найден в списке")


def print_cities(cities: list[dict]) -> None:
    """Выводит список заданных городов"""
    if not cities:
        print("Не найдено подходящих городов")
        return

    print('\n- - - - - - - - - - - - - - - - -')
    print('\n'.join(cities_to_str(cities)))
    print('- - - - - - - - - - - - - - - - - -\n')


def print_cities_menu() -> None:
    """Меню для выбора способа выборки списка городов для вывода"""
    while True:
        try:
            action = int(input("Посмотреть:\n"
                            "1. Список городов\n"
                            "2. Список городов, отфильтрованный по населению\n"
                            "3. Список городов, отфильтрованный по стране\n"
                            "4. Список городов, отсортированный по населению\n"
                            "5. Список городов, "
                            "отсортированный по названию страны\n"
                            ">>> "))
        except ValueError:
            print("Выбрано недопустимое действие")
            continue

        match (action):
            case 1:
                print_cities(cities.get_all())
                break
            case 2:
                try:
                    population = int(input("Население: "))
                    print_cities(cities.find_by_population(population))
                    break
                except ValueError:
                    print("Введено не число\n")
            case 3:
                country = input("Страна: ")
                print_cities(cities.find_by_country(country))
                break
            case 4:
                query = "Сортировать по возрастанию? (Y/n): "
                ascending = not input(query).lower() == 'n'
                print_cities(cities.sort_by_population(ascending))
                break
            case 5:
                query = "Сортировать по возрастанию? (Y/n): "
                ascending = not input(query).lower() == 'n'
                print_cities(cities.sort_by_country(ascending))
                break
            case _:
                print("Выбрано недопустимое действие")


def save() -> None:
    """Пробует сохранить список городов в csv файл"""
    try:
        cities.save()
        print("Список городов сохранен в csv файл")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")


def menu() -> None:
    """Выводит главное меню на экран"""
    try:
        cities.load()
        print("Список городов загружен из csv файла")
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")

    while True:
        try:
            action = int(input("\nВыберите действие:\n"
                            "1. Добавить город\n"
                            "2. Удалить город\n"
                            "3. Поиск по имени города\n"
                            "4. Посмотреть список городов\n"
                            "5. Сохранить\n"
                            "6. Сохранить и выйти\n"
                            "7. Выйти без сохранения\n"
                            ">>> "))
        except ValueError:
            print("Выбрано недопустимое действие")
            continue

        match (action):
            case 1: add()
            case 2: remove()
            case 3: find()
            case 4: print_cities_menu()
            case 5: save()
            case 6:
                save()
                break
            case 7:
                break
            case _:
                print("Выбрано недопустимое действие")
