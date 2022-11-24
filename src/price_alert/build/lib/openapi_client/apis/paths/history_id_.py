from openapi_client.paths.history_id_.get import ApiForget
from openapi_client.paths.history_id_.put import ApiForput
from openapi_client.paths.history_id_.delete import ApiFordelete
from openapi_client.paths.history_id_.patch import ApiForpatch


class HistoryId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
