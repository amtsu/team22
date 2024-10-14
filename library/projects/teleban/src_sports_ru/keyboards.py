from functools import wraps

from aiogram.utils.keyboard import InlineKeyboardBuilder

from db_managers.subscription_manager import SubscriptionDatabaseManager
from src_sports_ru.text_data import NBA_TEAMS_DICT, NFL_TEAMS_DICT, NHL_TEAMS_DICT


async def sports_sections_ikb():
    builder = InlineKeyboardBuilder()
    builder.button(text='NBA | National Basketball Association', callback_data='sports_nba')
    builder.button(text='NFL | National Football League', callback_data='sports_nfl')
    builder.button(text='NHL | National Hockey League', callback_data='sports_nhl')
    builder.button(text='⏮ В главное меню', callback_data='sports_main_menu')

    builder.adjust(1)
    return builder.as_markup()


def sports_params(source: str, name_dict: dict[str, str], icon: str):
    """
    Декоратор для создания клавиатур под разные виды спорта.
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            result = fn(source, name_dict, icon, *args, **kwargs)
            return result

        return wrapper

    return decorator


async def sports_subscription_ikb(source: str, name_dict: dict[str, str], icon: str, user_id: int):
    with SubscriptionDatabaseManager() as db:
        user_tags = db.get_user_tags(user_id, source)

    builder = InlineKeyboardBuilder()

    for team_name, tag in name_dict.items():
        if tag in user_tags:
            builder.button(text=f'{icon} {team_name}', callback_data=f'{source}_{tag}')
        else:
            builder.button(text=f'{team_name}', callback_data=f'{source}_{tag}')

    builder.button(text='⏮ В главное меню', callback_data='sports_main_menu')

    builder.adjust(2)
    return builder.as_markup()


sports_nba_ikb = sports_params('sports_nba', NBA_TEAMS_DICT, '🏀')(sports_subscription_ikb)
sports_nfl_ikb = sports_params('sports_nfl', NFL_TEAMS_DICT, '🏈')(sports_subscription_ikb)
sports_nhl_ikb = sports_params('sports_nhl', NHL_TEAMS_DICT, '🏒')(sports_subscription_ikb)
