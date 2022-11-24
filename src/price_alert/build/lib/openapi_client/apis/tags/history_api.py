# coding: utf-8

"""
    Your Project API

    Your project description  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.history_.post import HistoryCreate
from openapi_client.paths.history_id_.delete import HistoryDestroy
from openapi_client.paths.history_.get import HistoryList
from openapi_client.paths.history_id_.patch import HistoryPartialUpdate
from openapi_client.paths.history_id_.get import HistoryRetrieve
from openapi_client.paths.history_id_.put import HistoryUpdate


class HistoryApi(
    HistoryCreate,
    HistoryDestroy,
    HistoryList,
    HistoryPartialUpdate,
    HistoryRetrieve,
    HistoryUpdate,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
