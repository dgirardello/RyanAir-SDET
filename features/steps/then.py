from behave import then
from hamcrest import *


@then("The page tile is  \"{title}\"")
def step_impl(context, title):
    assert_that(context.driver.getTitle(), equal_to_ignoring_case(title))


@then("The Trip page show at least {cnt:d} flight listed")
def step_impl(context, cnt):
    assert_that(len(context.current_page.get_flights()), greater_than_or_equal_to(cnt))
