from src.paidentic_schema.post import Post
from src.baseclasses.response import Response


def test_getting_posts(get_posts):
    """
    Получение списка постов
    """
    Response(get_posts) \
        .assert_status_code(200) \
        .validate_data(Post)
