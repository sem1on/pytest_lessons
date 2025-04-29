from enum import Enum

class GlobalErrorsMessages(Enum):
    WRONG_STATUS_CODE = "The received code does not match the expected one."
    WRONG_ELEMENTS_COUNT = "Invalid number of elements"