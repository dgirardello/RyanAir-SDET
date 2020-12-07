from behave import when
from features.pages.TripPageClass import TripPage


@when("I click on the Search button")
def step_impl(conetxt):
    conetxt.current_page.search_flight()


@when("I wait until the Trip page is loaded")
def step_impl(context):
    context.current_page = TripPage(context.driver)
    context.current_page.wait_for_page_load(timeout=180)


@when("I select the first flight available")
def step_impl(context):
    context.current_page.select_first_flight()


@when("I select the \"{fare}\" fare")
def step_impl(context, fare):
    context.current_page.select_flight_fare(fare=fare)
