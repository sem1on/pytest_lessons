import requests


from configuration import SERVICE_URL
from src.paidentic_schema.post import Post
from src.baseclasses.response import Response


def test_getting_posts():
    r = requests.get(SERVICE_URL)
    response = Response(r)

    response.assert_status_code(200).validate_data(Post)

