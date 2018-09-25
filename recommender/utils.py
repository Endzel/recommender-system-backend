import requests
from rest_framework.response import Response
from django.conf import settings
import logging
import json


class Utils(object):

    @staticmethod
    def getRequest(url):
        headers = {"Content-Type": "application/json", "Authorization": "Token " + settings.RECOMMENDER_API_TOKEN}
        try:
            response = requests.get(url, "", headers=headers, timeout=60)
            return response
        except Exception as e:
            logging.error(str(e) + " : Get response")
            return Response({"error": "GET"}, status=400)

    @staticmethod
    def postRequest(url, param):
        headers = {"Content-Type": "application/json", "Authorization": "Token " + settings.RECOMMENDER_API_TOKEN}
        try:
            response = requests.post(url, param, headers=headers)
            return response
        except Exception as e:
            logging.error(str(e) + " : Post response")
            return Response({"error": "POST "}, status=400)

    @staticmethod
    def patchResponse(url, param):
        headers = {"Content-Type": "application/json", "Authorization": "Token " + settings.RECOMMENDER_API_TOKEN}
        try:
            response = requests.patch(url, param, headers=headers)
            return response
        except Exception as e:
            logging.error(str(e) + " : Patch response")
            return Response({"error": "PATCH "}, status=400)


class RequestUtils(object):

    @staticmethod
    def get_request(item, request):
        url = settings.RECOMMENDER_API_URL + item
        response = Utils.getResponse(url)
        if response.status_code != 200:
            logging.error("Error from the Recommender API" + " : get_list_request")
            return Response({"error": item}, response.status_code)
        response = response.json()
        return Response(response, status=200)
