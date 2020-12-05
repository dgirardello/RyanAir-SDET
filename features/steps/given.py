from behave import given
from features.steps.utils import calculate_date
from features.pages.MainPageClass import MainPage


@given("I'm on the RyanAir homepage")
def step_impl(context):
    context.main_page = MainPage(context.driver)
    context.main_page.load_page()


@given("I accept all the cookies if the Cookies Popup is shown")
def step_impl(context):
    context.main_page.accept_all_cookies()


@given("I check {trip}")
def step_impl(context, trip):
    if 'SINGLE' in str(trip).upper():
        context.main_page.select_trip_type(round_trip=False)
    elif 'RETURN' in str(trip).upper():
        context.main_page.select_trip_type(round_trip=True)


@given("I type \"{city}\" as the {selector}")
def step_impl(context, city, selector):
    origin = 'ORIGIN' in str(selector).upper()
    context.main_page.type_city(city, origin=origin)


@given("I the flight's {selector} using")
def step_impl(context, selector):
    country = ''
    airport = ''
    for row in context.table:
        if 'COUNTRY' in str(row[0]).upper():
            country = str(row[1])
        elif 'AIRPORT' in str(row[0]).upper():
            airport = str(row[1])

    origin = 'ORIGIN' in str(selector).upper()
    context.main_page.show_destinations(origin=origin)
    context.main_page.select_country(country=country, origin=origin)
    context.main_page.select_airport(airport=airport, origin=origin)
    #
    # context.main_page.set_country_and_airport(country=country, airport=airport, origin=origin)


@given("I select a departure date {days:d} days from now")
def step_impl(context, days):
    departure_date = calculate_date(days)
    context.main_page.set_date(departure_date)