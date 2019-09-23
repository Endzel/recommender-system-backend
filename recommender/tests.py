import requests

from django.test import TestCase
from django.conf import settings

from recommender.utils import RequestUtils


# This function will update the bearer token for the API
def obtain_login_token():

    url = settings.RECOMMENDER_API + "auth-recommender/login?password=angeltfg7455&system=tfgangel&username=angel"
    headers = {"Accept": "application/json"}
    response = requests.post(url, {}, headers=headers)

    if response.status_code != 200:
        return False

    settings.RECOMMENDER_API_TOKEN = response

    return True


class TestItemsSet(TestCase):

    url_items = "recommender/getItems?system=tfgangel"

    def setUp(self):
        obtain_login_token()

    def test_get_items_registered(self):
        result = RequestUtils.getRequest(self.url_items)
        result_json = result.json()

        self.assertNotEqual(result_json, {})


class TestAttributesSet(TestCase):

    url_item_attributes = "recommender/getDistinctProfileAttributes?system=tfgangel"

    def setUp(self):
        obtain_login_token()

    def test_get_item_attributes_registered(self):
        result = RequestUtils.getRequest(self.url_item_attributes)
        result_json = result.json()

        self.assertNotEqual(result_json, {})


class TestRulesSet(TestCase):

    url_rules = "recommender/getDistinctRules?rulesset=Tipo grupal&system=tfgangel"

    def setUp(self):
        obtain_login_token()

    def test_get_implicatinons_registered(self):
        result = RequestUtils.getRequest(self.url_rules)
        result_json = result.json()

        self.assertNotEqual(result_json, {})


class TestRecommendationList(TestCase):

    url = "recommender/getRecommendations?itemsset=Barcelona&rulesset=Tipo grupal&system=tfgangel&userdesc=angel jimenez"

    def setUp(self):
        obtain_login_token()

    def test_get_recommendation(self):
        result = RequestUtils.getRequest(self.url)
        result_json = result.json()

        self.assertNotEqual(result_json, {})
