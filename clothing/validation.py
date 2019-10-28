from abc import ABC, abstractmethod

from .constants import HAT, PANTS, SHIRT, SHOES, SOCKS, LEAVE

class BaseValidator(ABC):
    
    def __init__(self):
        super().__init__()

    @abstractmethod
    def validate(self, clothing_list):
        pass

class HatValidator(BaseValidator):

    def __init__(self):
        super().__init__()

    def validate(self, clothing_list):
        return True if SHIRT in clothing_list else False

class PantsValidator(BaseValidator):

    def __init__(self):
        super().__init__()

    def validate(self, clothing_list):
        return True

class ShirtValidator(BaseValidator):

    def __init__(self):
        super().__init__()

    def validate(self, clothing_list):
        return True

class ShoesValidator(BaseValidator):

    def __init__(self):
        super().__init__()

    def validate(self, clothing_list):
        return set([SOCKS, PANTS]).issubset(clothing_list) 

class SocksValidator(BaseValidator):

    def __init__(self):
        super().__init__()

    def validate(self, clothing_list):
        return True 

class LeaveValidator(BaseValidator):

    def __init__(self):
        super().__init__()

    def validate(self, clothing_list):
        return set([SOCKS, SHOES, PANTS, SHIRT]).issubset(clothing_list) 


validation_factory = {
    HAT: HatValidator,
    PANTS: PantsValidator,
    SHIRT: ShirtValidator,
    SHOES: ShoesValidator,
    SOCKS: SocksValidator,
    LEAVE: LeaveValidator
}