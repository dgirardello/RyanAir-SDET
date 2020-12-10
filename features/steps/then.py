from behave import then, step
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


@then("The Profile Name is shown in the top bar with the name \"{name}\"")
def step_impl(context, name):
    assert_that(context.current_page.get_profile_name(), contains_string(name))


@then("The selected seat location matches the seat shown in the right panel")
def step_impl(context):
    selected_seat_tooltip_text = context.current_page.get_selected_seat_location()
    selected_seat_panel_text = context.current_page.get_panel_seat_text()
    assert_that(selected_seat_panel_text, equal_to_ignoring_case(selected_seat_tooltip_text))


@then("In the Payment form an error is sown")
def step_impl(context):
    assert_that(context.current_page.is_error_present(), equal_to(True), "No error message is present")


@then("In the payment form the error message reads \"{message}\"")
def step_impl(context, message):
    assert_that(context.current_page.get_error_message(), contains_string(message))