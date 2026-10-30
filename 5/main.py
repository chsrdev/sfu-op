"""Основной модуль"""
from menu import main_menu
from gallery import Gallery

def main():
    """Точка входа программы"""
    gallery = Gallery()
    main_menu(gallery)

if __name__ == "__main__":
    main()
