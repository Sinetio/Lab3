import price_info as pi

price_list = {"apple": 1.20,"orange": 2.0}
quantity_list = {"apple": 5, "orange": 2}
def test_total_cost_shopping():
    result = pi.total_cost_shopping()
    assert result == 46.75

def test_cost_of_fruits():
    result =  pi.cost_of_fruits('apple',10)
    assert result == 12.0