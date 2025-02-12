import requests
from temporalio import activity

from params.params import APIParams


@activity.defn
def say_hello(name: str) -> str:
    return f"Hello, {name}!"


@activity.defn
def get_ip_address(api_params: APIParams) -> str:
    url = "https://gita-api.vercel.app/odi/verse/{0}/{1}".format(
        api_params.chapter, api_params.verse
    )
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers,verify=False)
    return response.text
