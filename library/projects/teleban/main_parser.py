from time import sleep

from data import session_factory, ContentRepository
from src_habr_com.parser import HabrComParser
from src_overclockers_ru.parser import OverclockersRuParser
from src_rbc_ru.parser import RbcRuParser
from src_sports_ru.parser import SportsRuParser
from src_trial_sport_ru.parser import TrialSportRuParser


class MainParser:
    def __init__(self, source_list: list) -> None:
        self.source_list = source_list

    def fill_db(self):
        while True:
            for source_parser in self.source_list:
                result = source_parser().get_new_content()
                with session_factory() as session:
                    db = ContentRepository(session)
                    db.add_all_content(result)
                    db.remove_old_content()

                sleep(10)


# Список источников
SOURCE_LIST = [
    SportsRuParser,
    TrialSportRuParser,
    RbcRuParser,
    HabrComParser,
    OverclockersRuParser,
]

if __name__ == '__main__':
    try:
        MainParser(SOURCE_LIST).fill_db()
    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем.")
