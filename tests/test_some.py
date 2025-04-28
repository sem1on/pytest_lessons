import requests

from src.baseclasses.response import Response

from configuration import SERVICE_URL
from src.schemas.posts import POST_SCHEMA
from src.paidentic_schema.post import Post


def test_getting_posts():
    r = requests.get(SERVICE_URL)
    response = Response(r)

    response.assert_status_code(200)
    response.validate_data(Post)

