from datadog import initialize, api
from .keys import datadog_api_key, datadog_app_key
from time import time


class DataDog:
    def __init__(self):
        initialize(api_key=datadog_api_key, app_key=datadog_app_key)

    @staticmethod
    def send_metric(name, value):
        """Send a metric value to DataDog

        This is a blocking function.
        """
        try:
            value = value if value else 0
            name = name
            metric = api.Metric.send(metric=name, points=[(time(), value)])
        except Exception as e:
            print(e)
