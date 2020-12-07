from behave import then
from hamcrest import *


@then("The page tile is  \"{title}\"")
def step_impl(context, title):
    assert_that(context.driver.getTitle(), equal_to_ignoring_case(title))


@then("The Trip page show at least {cnt:d} flight listed")
def step_impl(context, cnt):
    assert_that(len(context.current_page.get_flights()), greater_than_or_equal_to(cnt))


@then("The total amount beside the shopping cart is {comparator} than {value:d}")
def step_impl(context, comparator, value):
    shopping_amount = context.current_page.get_shopping_amount()
    if 'GREATER OR EQUAL' in str(comparator).upper():
        assert_that(shopping_amount, greater_than_or_equal_to(value))
    elif 'GREATER' in str(comparator).upper():
        assert_that(shopping_amount, greater_than(value))
    elif 'LESS OR EQAL' in str(comparator).upper():
        assert_that(shopping_amount, less_than_or_equal_to(value))
    elif 'LESS' in str(comparator).upper():
        assert_that(shopping_amount, less_than(value))


@then("The Login sub-section is shown")
def step_impl(context):
    assert_that(context.current_page.is_login_shown(timeout=90), equal_to(True))
