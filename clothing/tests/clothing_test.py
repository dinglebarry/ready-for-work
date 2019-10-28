from clothing.clothing import validate_values

def test_validate_values_socks_pants_shirt_shoes_leave():
    result = validate_values("5 2 3 4 6")
    assert result == "socks, pants, shirt, shoes, leave"

def test_validate_values_shirt_socks_pants_shoes_leave():
    result = validate_values("3 5 2 4 6")
    assert result == "shirt, socks, pants, shoes, leave"

def test_validate_values_shirt_socks_pants_shoes_hat_leave():
    result = validate_values("3 5 2 4 1 6")
    assert result == "shirt, socks, pants, shoes, hat, leave"

def test_validate_values_socks_hat_fail():
    result = validate_values("5 1")
    assert result == "socks, fail"

def test_validate_values_no_leave():
    result = validate_values("3 5 2 4")
    assert result == "shirt, socks, pants, shoes, fail"

def test_validate_values_double_value():
    result = validate_values("3 5 3")
    assert result == "shirt, socks, fail"

def test_validate_values_no_values():
    result =  validate_values("")
    assert result == "fail"

