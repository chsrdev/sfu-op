"""Модуль управления базой данных"""
import csv
from copy import deepcopy


cities: list[dict] = []


def exists_by_city(filter_city: str) -> bool:
    """Возвращает True, если город с заданным именем существует, иначе False"""
    for city in cities:
        if city["city"] == filter_city:
            return True
    return False


def add(city: str,
        foundation_year: int,
        population_thousands: int,
        country: str) -> dict:
    """Добавляет в список городов новый город"""
    stripped_city = city.strip()
    stripped_country = country.strip()

    if not stripped_city:
        raise ValueError("Пустое название города")
    if not stripped_country:
        raise ValueError("Пустое название страны")
    if exists_by_city(stripped_city):
        raise ValueError("Такой город уже есть в списке")
    if foundation_year < 0:
        raise ValueError("Отрицательный год основания не может быть")
    if population_thousands < 0:
        raise ValueError("Отрицательное население не может быть")

    new_city = {
        "city": stripped_city,
        "foundation_year": foundation_year,
        "population": population_thousands,
        "country": stripped_country
    }
    cities.append(new_city)

    return new_city


def remove(city_name: str) -> dict:
    """Удаляет из списка городов город по названию, если он существует"""
    for city in cities:
        if city['city'] == city_name:
            cities.remove(city)
            return city

    raise KeyError("Заданный город не найден в базе")


def get_all() -> list[dict]:
    """Возвращает список всех городов в списке"""
    return deepcopy(cities)


def find_by_city(city_name: str) -> dict | None:
    """Ищет в списке городов город по названию и возвращает его,
    иначе возвращает None"""
    for city in cities:
        if city['city'] == city_name:
            return city

    return None


def find_by_population(population: int) -> list[dict]:
    """Ищет в списке городов города по популяции и возвращает их"""
    found = []

    for city in cities:
        if city['population'] == population:
            found.append(city)

    return found


def find_by_country(country: str) -> list[dict]:
    """Ищет в списке городов города по названию страны и возвращает их"""
    found = []

    for city in cities:
        if city['country'] == country:
            found.append(city)

    return found


def sort_by_population(ascending: bool = True) -> list[dict]:
    """Возвращает список городов, отсортированный по популяции"""
    return sorted(cities, key=lambda c: c['population'], reverse=not ascending)


def sort_by_country(ascending: bool = True) -> list[dict]:
    """Возвращает список городов,
    отсортированный по названию страны"""
    return sorted(cities,
                  key=lambda c: c['country'].casefold(), reverse=not ascending)


def save(file: str = 'cities.csv') -> None:
    """Сохраняет список городов в csv файл"""
    field_names = ['city', 'foundation_year', 'population', 'country']
    with open(file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(cities)


def load(file: str = 'cities.csv') -> None:
    """Загружает список городов из csv файла"""
    global cities

    with open(file, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        cities = [
            {
                "city": row["city"],
                "foundation_year": int(row["foundation_year"]),
                "population": int(row["population"]),
                "country": row["country"]
            }
            for row in reader
        ]
