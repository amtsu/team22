import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.history_api import HistoryApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.HISTORY: HistoryApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.HISTORY: HistoryApi,
    }
)
