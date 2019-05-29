from SeamlessPy.constants import *
from SeamlessPy.utilities import *
import requests
import json


class Seamless(object):

    @lazy_property
    def oauth_token(self):
        auth_response = requests.post(AUTH_BASE_URL, data=AUTH_PAYLOAD, headers=AUTH_REQUEST_HEADERS)
        auth_json = auth_response.json()
        bearer_token = auth_json['session_handle']['access_token']
        return bearer_token

    def get_location_search_results(self, long: float, lat: float, pageSize = 0, pageNum=1):
        method = 'search'
        location = 'POINT({}%20{})'.format(long, lat)
        url_parameters = {
            'orderMethod': 'delivery',
            'locationMode': 'DELIVERY',
            'facetSet': 'umamiV2',
            'pageSize': '',
            'hideHateos': 'true',
            'searchMetrics': 'true',
            'location': '',
            'pageNum': '',
            'preciseLocation': 'true',
            'facet': 'open_now%3atrue',
            'sortSetId': 'umamiV2',
            'sponsoredSize': '3',
            'countOmittingTimes': 'true'
        }
        qry_params = url_parameters
        qry_params['location'] = location
        qry_params['pageSize'] = pageSize
        qry_params['pageNum'] = pageNum
        qry_url = REST_BASE_URL + method + '?' + '&'.join(["{}={}".format(k, v) for k, v in qry_params.items()])
        headers = {'Authorization': 'Bearer {}'.format(self.oauth_token)}
        r = requests.get(qry_url, headers=headers)
        return r.json()

    def get_restaurant_details(self, restaurant_id: int):
        url_parameters = {
            'hideChoiceCategories': 'true',
            'orderType': 'standard',
            'hideUnavailableMenuItems': 'true',
            'hideMenuItems': 'false',
            'showMenuItemCoupons': 'true',
            'includePromos': 'true'
        }
        qry_params = url_parameters
        qry_url = REST_BASE_URL + str(restaurant_id) + '?' + '&'.join(["{}={}".format(k, v) for k, v in qry_params.items()])
        headers = {'Authorization': 'Bearer {}'.format(self.oauth_token)}
        r = requests.get(qry_url, headers=headers)
        str_json = r.text
        rest = Restaurant(str_json)
        return rest


class Restaurant(object):
    def __init__(self, json_str: str):
        self._json = json_str
        self._dict_rest = json.loads(self._json)

    def _get_address(self):
        return self._dict_rest['restaurant']['address']

    def _get_menu_groups(self):
        return MenuCategories(self._dict_rest['restaurant']['menu_category_list'])

    address = property(_get_address)
    menu_groups = property(_get_menu_groups)


class MenuCategories(object):
    def __init__(self, lst_menu_cat):
        self._lst_menu_cat = lst_menu_cat

    def __iter__(self):
        return MenuCategory(iter(self._lst_menu_cats))


class MenuCategory(object):
    def __init__(self, dict_menu_cat):
        self._dict_menu_cat = dict_menu_cat

    def __iter__(self):
        return MenuItem(iter(self._dict_menu_cat['menu_item_list']))

    def get_id(self):
        return self._dict_menu_cat['id']

    def get_name(self):
        return self._dict_menu_cat['name']

    def get_seq(self):
        return self._dict_menu_cat['sequence']

    def get_available(self):
        return self._dict_menu_cat['available']

    id = property(fget=get_id)
    name = property(fget=get_name)
    sequence = property(fget=get_seq)
    available = property(fget=get_available)


class MenuItem(object):
    def __init__(self, dict_item):
        self._dict_item = dict_item