from time import sleep

from data import session_factory, ContentRepository
from src_habr_com.parser import HabrComParser
from src_rbc_ru.parser import RbcRuParser
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
                result = source_parser().get_new_content()
                with session_factory() as session:
                    ContentRepository(session).add_all_content(result)
                sleep(10)
            sleep(60)


# Список источников
SOURCE_LIST = [
    SportsRuParser,
    TrialSportRuParser,
    RbcRuParser,
    HabrComParser,
]

if __name__ == '__main__':
    MainParser(SOURCE_LIST).fill_db()
