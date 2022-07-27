from os import path as osp

from bs4 import BeautifulSoup
import requests

from transfer.utils import read_text_from_file
from transfer.mapping import (
    file_type2lexer,
    file_extension2file_type,
    expires_desc2time,
)

_PASTE_CONFIG = {
    "url": "https://pastebin.mozilla.org/",
}


def paste_file_to_pastebin(file, expires="21d", file_type=None):
    text = read_text_from_file(file)

    if file_type is None:
        file_type = file_extension2file_type.get(osp.splitext(file)[-1], "txt")
    lexer = file_type2lexer.get(file_type, "_text")

    expires = expires_desc2time.get(expires, "21d")

    response = requests.get(_PASTE_CONFIG["url"])
    if response.status_code != 200:
        raise Exception("Failed to get Pastebin URL")

    # get cookies
    cookie_key, cookie_value = response.headers["Set-Cookie"].split(";")[0].split("=")
    cookies = {cookie_key: cookie_value}

    # get headers
    headers = {
        "Referer": "https://pastebin.mozilla.org/",
    }

    # get body
    soup = BeautifulSoup(response.text, "html.parser")
    token = soup.find("input", {"name": "csrfmiddlewaretoken"})
    if token is None:
        raise RuntimeError(
            "An unexpected error occurred while getting the CSRF token,"
            "please create an issue in https://github.com/wyg1997/transfer/issues.\n"
            "I will fix it as soon as possible."
        )
    body = {
        "csrfmiddlewaretoken": token["value"],
        "lexer": lexer,
        "expires": expires,
        "rtl": "",
        "content": text,
    }

    # post form
    response = requests.post(
        _PASTE_CONFIG["url"], headers=headers, cookies=cookies, data=body
    )
    if response.status_code != 200:
        raise Exception(
            "Failed to paste to Pastebin, please check your internet connection."
        )

    # parse redirect history for result url
    result_url = None
    for history_response in response.history:
        if "location" in history_response.headers:
            result_url = history_response.headers["location"]
    assert result_url is not None, "Failed to get pasting result url"
    return _PASTE_CONFIG["url"][:-1] + result_url
