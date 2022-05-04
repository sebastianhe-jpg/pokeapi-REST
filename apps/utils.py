"""
requests lib util
"""
import requests


def http_get(url: str, headers: dict = {}, timeout: int = 4):
    """
    function that handles generical get http requests
    :param url: string url
    :param headers: headers of the requests (optional)
    :param timeout: timeout value (optional)
    :return: return json
    """
    response = requests.get(url=url, headers=headers, timeout=timeout)
    response_json = None
    try:
        response_json = response.json()
    except Exception as err:
        del err
    return response_json
