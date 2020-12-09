from behave import when
from features.steps.constants import *
from features.pages.PageFactory import get_page_object


@when("I click on the Search button")
def step_impl(conetxt):
    conetxt.current_page.search_flight()


@when("I wait until the Trip page is loaded")
def step_impl(context):
    context.current_page = get_page_object(page=PAGE_TRIP, section=PAGE_TRIP_SECTION_FLIGHTS, driver=context.driver)
    context.current_page.wait_for_page_load(timeout=180)


@when("I select the first flight available")
def step_impl(context):
    context.current_page.select_first_flight()


@when("I select the \"{fare}\" fare")
def step_impl(context, fare):
    context.current_page.select_flight_fare(fare=fare)


@when("I input a valid credentials and click on Login")
def step_impl(context):
    context.current_page.do_login(email=context.config.userdata['ryanair_user'],
                                  password=context.config.userdata['ryanair_pass'])


@when("I click on the first Saved Companion")
def step_impl(context):
    context.current_page.select_first_companion()


@when("I click on the first sear available in the \"{category}\" section")
def step_impl(context, category):
    priority = 'PRIORITY' in str(category).upper()
    context.current_page.select_first_available_seat(priority=priority)


@when("I click on the Seat Selection \"{button}\" button")
def step_impl(context, button):
    if 'CONTINUE' in str(button).upper():
        context.current_page.continue_to_bags()
        context.current_page = get_page_object(page=PAGE_TRIP, section=PAGE_TRIP_SECTION_BAGS, driver=context.driver)


@when("I click on the Bags \"{button}\" button")
def step_impl(context, button):
    if 'CONTINUE' in str(button).upper():
        context.current_page.continue_to_extras()
        context.current_page = get_page_object(page=PAGE_TRIP, section=PAGE_TRIP_SECTION_EXTRAS, driver=context.driver)


@when("I click on the Extras \"{button}\" button")
def step_impl(context, button):
    if 'CONTINUE' in str(button).upper():
        context.current_page.finish_booking()
        context.current_page = get_page_object(page=PAGE_TRIP, section=PAGE_TRIP_SECTION_OVERVIEW, driver=context.driver)


@when("I click on the Shopping cart icon")
def step_impl(context):
    context.current_page.show_cart_details()


@when("I Click on the Checkout button")
def step_impl(context):
    context.current_page.show_cart_details()
