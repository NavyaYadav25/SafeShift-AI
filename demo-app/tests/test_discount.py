from services.discount import calculate_discount

def test_normal_case():
    assert calculate_discount(100, 10) == 0.1
