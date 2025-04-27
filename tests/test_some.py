import requests

from src.enums.globalenums.enums import GlobalErrorsMessages
from configuration import SERVICE_URL

# SERVICE_URL = "https://my-json-server.typicode.com/typicode/demo/posts"

def test_getting_posts():
    response = requests.get(SERVICE_URL)
    received_posts = response.json()

    assert response.status_code == 200, GlobalErrorsMessages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 3, GlobalErrorsMessages.WRONG_ELEMENTS_COUNT.value
