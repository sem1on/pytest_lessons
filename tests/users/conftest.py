import pytest
import requests
from src.generators.player import Player

from configuration import SERVICE_URL_2

@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL_2)
    return response

@pytest.fixture
def get_generator_player():
    return Player()