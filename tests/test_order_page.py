import pytest
from pages.order_page import OrderPage
from data import USER_1, USER_2, ExpectedText

@pytest.mark.parametrize("user_data", [USER_1, USER_2])
def test_order_page(order_page, user_data):
    order_page.fill_user_data(user_data)
    order_page.fill_rental_options(user_data)
    order_page.confirm_order()
    assert order_page.check_order_created()