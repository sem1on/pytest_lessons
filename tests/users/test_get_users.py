import pytest

from src.baseclasses.response import Response
from src.paidentic_schema.users import User


def test_getting_users_list(get_users):
    """
    Получение списка пользователей
    """
    Response(get_users) \
        .assert_status_code(200) \
        .validate_data(User)

@pytest.mark.parametrize("balance", {
    100,
    -21,
    0,
    "33"
})
def test_generate_palyer(balance, get_generator_player):
    print(get_generator_player.set_balanse(balance).build())


@pytest.mark.parametrize("delete_key", {
    'account_status',
    'balance',
    'avatar',
    'localization'
})
def test_delet_item(delete_key, get_generator_player):
    object_del = get_generator_player.build()
    del object_del[delete_key]
    print(object_del)