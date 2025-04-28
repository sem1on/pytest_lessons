import requests

from configuration import SERVICE_URL_2
from src.baseclasses.response import Response
from src.paidentic_schema.users import User

def test_getting_users_list():
    response = requests.get(SERVICE_URL_2)
    test_data = Response(response)
    test_data.assert_status_code(200).validate_data(User)

