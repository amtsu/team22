import openapi_client
from pprint import pprint
from openapi_client.apis.tags import history_api
from openapi_client.model.history import History
from openapi_client.model.paginated_history_list import PaginatedHistoryList
from openapi_client.model.patched_history import PatchedHistory

class APIProcessing:

#     def send_in_api(self):
#         configuration = openapi_client.Configuration(host="http://absrent.ru:8000")

#         with openapi_client.ApiClient(configuration) as api_client:
#             api_instance = history_api.HistoryApi(api_client)
#             for e in self.__list_dict:
#                 # print(e)
#                 history = History(
#                     pk=1,
#                     title=e["title"],
#                     quantity=1,
#                     price=str(e["price"]),
#                     price_sale=str(e["price_sale"]),
#                     datetime_create="1970-01-01T00:00:00.00Z",
#                     # score="-807",
#                     # count_comments=1,
#                     # count_likes=1,
#                     # count_stars_all=1,
#                     # count_stars_1=1,
#                     # count_stars_2=1,
#                     # count_stars_3=1,
#                     # count_stars_4=1,
#                     # count_stars_5=1,
#                     # count_how_much_buy=1,
#                     # count_questions=1,
#                     # count_photo=1,
#                     category=e["category"],
#                     # category_url="category_url_example",
#                     brand=e["brand"],
#                     brand_url=e["brand_url"],
#                     # day_to_delivery=1,
#                     # sku="sku_example",
#                     url=e["url"],
#                     # canonical_url="canonical_url_example",
#                     img_url=e["image_url"],
#                     description=e["description"],
#                     # params="params_example",
#                     # seller="seller_example",
#                     # seller_url="seller_url_example",
#                     source_url=e["source_url"],
#                     apartment_area=e["apartment_area"],
#                     apartment_completion_quarter=e["apartment_completion_quarter"],
#                     apartment_completion_year=e["apartment_completion_year"],
#                     apartment_floor=e["apartment_floor"],
#                     apartment_floors_total=e["apartment_floors_total"],
#                     apartment_ceilingheight=e["apartment_ceilingheight"],
#                     apartment_room=e["apartment_room"],
#                     apartment_ppm=e["apartment_ppm"],
#                     apartment_address=e["apartment_address"],
#                     apartment_location=e["apartment_location"],
#                     apartment_location_lat=e["apartment_location_lat"],
#                     apartment_location_lon=e["apartment_location_lon"],
                    
#                     # urls_other_products_on_the_page="urls_other_products_on_the_page_example",
#                     # worker="worker_example",
#                     # task="task_example",
#                 )  # History |  (optional)

#                 try:
#                     api_response = api_instance.history_create(body=history)
#                     # pprint(api_response)
#                 except openapi_client.ApiException as e:
#                     print("Exception when calling HistoryApi->history_create: %s\n" % e)
#             print("Count load object =", len(self.__list_dict))