from app.shopping import calculate_total, apply_discount

def test_total():
    assert calculate_total(100, 2) == 200

def test_discount():
    assert apply_discount(200, 10) == 180

def test_negative_quantity():
    try:
        calculate_total(100, -1)
        assert False
    except ValueError:
        assert True
