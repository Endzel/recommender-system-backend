import requests
import logging

from django.conf import settings

from rest_framework.response import Response


def add_query_params(url, params):
    for key, value in params.items():
        if url[:-2] == "&&":
            url = url + '' + key + "=" + str(value)
        else:
            url = url + "&&" + key + "=" + str(value)
    return url


class RequestUtils(object):

    @staticmethod
    def getRequest(url):
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": "Bearer " + settings.RECOMMENDER_API_TOKEN}
        try:
            response = requests.get(url, "", headers=headers, timeout=60)
            return response
        except Exception as e:
            logging.error(str(e) + " : Get response")
            return Response({"error": "[ERROR IN GET]" + str(e)}, status=400)

    @staticmethod
    def postRequest(url, param):
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": "Bearer " + settings.RECOMMENDER_API_TOKEN}
        try:
            response = requests.post(url, param, headers=headers)
            return response
        except Exception as e:
            logging.error(str(e) + " : Post response")
            return Response({"error": "[ERROR IN POST]" + str(e)}, status=400)
