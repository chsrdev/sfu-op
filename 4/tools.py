"""Модуль вспомогательных инструментов"""
def city_to_str(city: dict) -> str:
    """Преобразует запись о городе в строку"""
    city, foundation_year, population, country = city.values()
    return (f"Город: {city}, "
            f"Год основания: {foundation_year}, "
            f"Население: {population} т.ч., "
            f"Страна: {country}")


def cities_to_str(cities: list[dict]) -> list[str]:
    """Преобразует список записей городов в список строк"""
    return [city_to_str(city) for city in cities]
