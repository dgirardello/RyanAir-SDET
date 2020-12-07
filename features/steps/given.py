from behave import given
from datetime import datetime as DT
from features.steps.utils import calculate_date
from features.pages.MainPageClass import MainPage
from features.pages.TripPageClass import TripPage


@given("I'm on the RyanAir homepage")
def step_impl(context):
    context.current_page = MainPage(context.driver)
    context.current_page.load_page()


@given("I accept all the cookies if the Cookies Popup is shown")
def step_impl(context):
    context.current_page.accept_all_cookies()


@given("I check {trip}")
def step_impl(context, trip):
    if 'SINGLE' in str(trip).upper():
        context.current_page.select_trip_type(round_trip=False)
    elif 'RETURN' in str(trip).upper():
        context.current_page.select_trip_type(round_trip=True)


@given("I type \"{city}\" as the {selector}")
def step_impl(context, city, selector):
    origin = 'ORIGIN' in str(selector).upper()
    context.current_page.type_city(city, origin=origin)


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
    context.current_page.show_destinations(origin=origin)
    context.current_page.select_country(country=country, origin=origin)
    context.current_page.select_airport(airport=airport, origin=origin)
    #
    # context.main_page.set_country_and_airport(country=country, airport=airport, origin=origin)


@given("I select a departure date {days:d} days from now")
def step_impl(context, days):
    departure_date = calculate_date(days)
    context.current_page.set_date(departure_date)


@given("I select a departure date for a {week_day} {weeks:d} weeks from now")
def step_impl(context, week_day, weeks):
    days = 7 * weeks
    departure_date = calculate_date(days, weekday=week_day)
    context.current_page.set_date(departure_date)


@given("I'm in the Tip page of a flight search with")
def step_impl(context):

    flight_params = {row[0]: row[1] for row in context.table}

    date_list = str(flight_params['DATE']).split(' ')
    days = 0
    cnt = int(date_list[0])
    if 'DAY' in str(date_list[1]).upper():
        timeframe = 1
    elif 'WEEK' in str(date_list[1]).upper():
        timeframe = 7
    days += cnt * timeframe
    departure_date = calculate_date(days, weekday=flight_params['WEEKDAY'])

    context.current_page = TripPage(context.driver)
    context.current_page.load_page(date_out=departure_date, adults=flight_params['ADULTS'],
                                   origin=flight_params['ORIGIN'], destination=flight_params['DESTINATION'])

@given("I select the \"{fare}\" fare")
def step_impl(context, fare):
    context.current_page.select_flight_fare(fare=fare)
    pass