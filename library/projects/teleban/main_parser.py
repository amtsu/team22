from config import DB_NAME
from src_sports_ru.parser import SportsRuParser
from src_trial_sport_ru.parser import TrialSportRuParser

SOURCE_LIST = [
    SportsRuParser,
    TrialSportRuParser,
]

for parser in SOURCE_LIST:
    parser(DB_NAME).get_new_content()
