import sys
sys.path.append('D:/IT/pytest_lessons')  # Добавить корень проекта
from src.enums.user_enam import Status
from src.generators.palyer_localization import PlayerLocalization

class Player:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_status(self, status=Status.active.value):
        self.result['account_status'] = status
        return self
    
    def set_balanse(self, balance=0):
        self.result['balance'] = balance
        return self
    
    def set_avatar(self, avatar='https://www.google.ru/'):
        self.result['avatar'] = avatar
        return self
    
    def  reset(self):
        self.set_avatar()
        self.set_balanse()
        self.set_status()
        self.result["localization"] = {
                "en": PlayerLocalization("en_UK").build(),
                "ru": PlayerLocalization("ru_RU").build()
            }    
        return self

    def build(self):
        return self.result
    

z = Player().set_balanse(20).build()
print(z)