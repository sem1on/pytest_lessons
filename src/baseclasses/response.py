from jsonschema import validate

from src.enums.globalenums.enums import GlobalErrorsMessages


class Response:

    def __init__(self, response):
        self.response = response
        json_data = response.json()
        
        # Обрабатываем оба случая: когда данные приходят сразу списком 
        # и когда они обернуты в словарь с ключом 'data'
        if isinstance(json_data, dict) and 'data' in json_data:
            self.response_json = json_data['data']  # данные из поля 'data'
        elif isinstance(json_data, (list, dict)):
            self.response_json = json_data          # данные пришли сразу списком/словарем
        else:
            raise ValueError("Unexpected response format")
        
        self.response_status = response.status_code

    def validate_data(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.model_validate(item)
        else:
            schema.model_validate(self.response_json)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_statuse in status_code, GlobalErrorsMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorsMessages.WRONG_STATUS_CODE.value
        return self