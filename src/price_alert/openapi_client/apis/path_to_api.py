import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.history_ import History
from openapi_client.apis.paths.history_id_ import HistoryId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.HISTORY_: History,
        PathValues.HISTORY_ID_: HistoryId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.HISTORY_: History,
        PathValues.HISTORY_ID_: HistoryId,
    }
)
