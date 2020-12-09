import re
from behave import step
from hamcrest import *
from features.steps.constants import *
from features.pages.PageFactory import get_page_object


@step("The {sub_section} sub-section is shown")
def step_impl(context, sub_section):
    if re.search(r"Login", sub_section, re.IGNORECASE):
        assert_that(context.current_page.is_login_section_shown(timeout=90), equal_to(True),
                    "Sub Section '{}' is not shown".format(sub_section))
    else:
        raise Exception("Unrecognized Sub Section '{}'".format(sub_section))


@step("The {popup} popup is shown")
def step_impl(context, popup):
    if re.search(r"Login", popup, re.IGNORECASE):
        assert_that(context.current_page.is_login_popup_shown(timeout=90), equal_to(True),
                    "Popup '{}' is not shown".format(popup))
    else:
        raise Exception("Unrecognized Popup '{}'".format(popup))


@step("The {sub_section} sub-section is enabled")
def step_impl(context, sub_section):
    if re.search(r"Passengers", sub_section, re.IGNORECASE):
        element = context.current_page.get_passenger_subsection(inner_div=True)
        assert_that(element.get_attribute('class'), not (contains_string('--disabled')),
                    "Sub Section '{}' is DISABLED".format(sub_section))
    else:
        raise Exception("Unrecognized Sub Section '{}'".format(sub_section))


@step("The passenger fields are populated with")
def step_impl(context):
    for row in context.table:
        field_text = context.current_page.get_passenger_field_text(row[0])
        assert_that(field_text, contains_string(row[1]))


@step("I click on the \"{button}\" button within the \"{sub_section}\" sub-section")
def step_impl(context, button, sub_section):
    if context.page == PAGE_TRIP:
        if context.section == PAGE_TRIP_SECTION_FLIGHTS:
            if PAGE_TRIP_SECTION_FLIGHTS_LOGIN in str(sub_section).upper():
                context.current_page.click_login_element(button)
            elif PAGE_TRIP_SECTION_FLIGHTS_PASSENGERS in str(sub_section).upper():
                if 'CONTINUE' in str(button).upper():
                    context.current_page.continue_to_seat_selection()
                    context.current_page = get_page_object(page=PAGE_TRIP,
                                                           section=PAGE_TRIP_SECTION_SEATS,
                                                           driver=context.driver)


@step("The seat is selected")
def step_impl(context):
    assert_that(context.current_page.is_seat_selected(), equal_to(True), "The Seat is not selected")


@step("The {name} page is shown")
def step_impl(context, name):
    assert_that(context.current_page.is_loaded(), equal_to(True), "Unknown Page '{}'".format(name))
