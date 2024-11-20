from time import sleep

from data import session_factory, ContentRepository
from src_sports_ru.parser import SportsRuParser
from src_trial_sport_ru.parser import TrialSportRuParser


class ParsingError(Exception):
    """Ошибка при парсинге данных с сайта."""
    pass


class MainParser:
    def __init__(self, source_list: list) -> None:
        self.source_list = source_list

    def fill_db(self):
        while True:
            for source_parser in self.source_list:
                try:
                    result = source_parser().get_new_content()
                    if len(result) < 5:
                        raise ParsingError(f'Нужно проверить парсер {source_parser.__name__}!')

                    with session_factory() as session:
                        ContentRepository(session).add_all_content(result)
                except Exception as err:
                    print(err)

                sleep(10)
            sleep(60)


SOURCE_LIST = [
    SportsRuParser,
    TrialSportRuParser,
]

if __name__ == '__main__':
    MainParser(SOURCE_LIST).fill_db()
