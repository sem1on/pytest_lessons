from src.baseclasses.response import Response
from src.paidentic_schema.users import User


def test_getting_users_list(get_users):
    """
    Получение списка пользователей
    """
    Response(get_users) \
        .assert_status_code(200) \
        .validate_data(User)

def test_generate_palyer(get_generator_player):
    print(get_generator_player.build())