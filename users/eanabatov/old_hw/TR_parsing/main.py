from team22.users.EANabatov.TR_parsing.web_page_parser import BookStoreParser


def main():
    """Функция для работы с парсером в терминале"""
    start_parsing_code: int = int(input("Введите начальный код товара для парсинга: "))
    end_parsing_code: int = int(input("Введите конечный код товара для парсинга: "))
    object_one = BookStoreParser()
    print(object_one.start_parsing(start_parsing_code, end_parsing_code))


if __name__ == "__main__":
    main()
