from clothing.validation import *
from clothing.constants import HAT, PANTS, SHIRT, SHOES, SOCKS, LEAVE, clothing_output


def test_valid_hat_after_shirt():
    clothes = [SOCKS, SHIRT, HAT]
    validator = PantsValidator() 
    assert validator.validate(clothes)

def test_invalid_hat_before_shirt():
    clothes = [SOCKS, HAT]
    validator = HatValidator()
    assert not validator.validate(clothes)

def test_valid_pants_before_any():
    clothes = [SHOES,PANTS]
    validator = PantsValidator()
    assert validator.validate(clothes)

def test_valid_shirt_before_any():
    clothes = [SHOES,SOCKS]
    validator = ShirtValidator()
    assert validator.validate(clothes)

def test_valid_shoes_after_socks_and_pants():
    clothes = [SOCKS,PANTS]
    validator = ShoesValidator()
    assert validator.validate(clothes)

def test_invalid_shoes_before_socks():
    clothes = [HAT, PANTS]
    validator = ShoesValidator()
    assert not validator.validate(clothes)

def test_invalid_shoes_before_pants():
    clothes = [HAT, SOCKS]
    validator = ShoesValidator()
    assert not validator.validate(clothes)

def test_valid_leave():
    clothes = [SOCKS, SHOES, PANTS, SHIRT]
    validator = LeaveValidator()
    assert validator.validate(clothes)

def test_invalid_leave_no_shirt():
    clothes = [SOCKS, SHOES, PANTS]
    validator = LeaveValidator()
    assert not validator.validate(clothes)

def test_invalid_leave_no_clothes():
    clothes = []
    validator = LeaveValidator()
    assert not validator.validate(clothes)

def test_factory_get_hat_validator():
    assert validation_factory[HAT] == HatValidator

def test_factory_get_pants_validator():
    assert validation_factory[PANTS] == PantsValidator

def test_factory_get_shirt_validator():
    assert validation_factory[SHIRT] == ShirtValidator

def test_factory_get_shoes_validator():
    assert validation_factory[SHOES] == ShoesValidator
    
def test_factory_get_socks_validator():
    assert validation_factory[SOCKS] == SocksValidator

def test_factory_get_leave_validator():
    assert validation_factory[LEAVE] == LeaveValidator