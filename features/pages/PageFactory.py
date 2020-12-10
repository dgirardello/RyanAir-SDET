from features.pages import MainPageClass, PaymentPageClass, TripPageClass, \
    TripPageFlightSelectionClass, TripPageSeatSelectionClass, TripPageBagsClass, TripPageExtras, TripPageOverview
from features.steps.constants import *


def get_page_object(page, section=None, driver=None):
    page = str(page).upper()
    return_page_obj = None
    if PAGE_MAIN in page: return_page_obj = MainPageClass.MainPage(driver)
    elif PAGE_TRIP in page:
        if section is not None:
            section = str(section).upper()
            if PAGE_TRIP_SECTION_FLIGHTS in section: return_page_obj = TripPageFlightSelectionClass.FlightSelection(driver)
            if PAGE_TRIP_SECTION_SEATS in section: return_page_obj = TripPageSeatSelectionClass.SeatSelection(driver)
            if PAGE_TRIP_SECTION_BAGS in section: return_page_obj = TripPageBagsClass.Bags(driver)
            if PAGE_TRIP_SECTION_EXTRAS in section: return_page_obj = TripPageExtras.Extras(driver)
            if PAGE_TRIP_SECTION_OVERVIEW in section: return_page_obj = TripPageOverview.OverviewSection(driver)
        else:
            return TripPageClass.TripPage(driver)
    elif PAGE_PAYMENT in page: return_page_obj = PaymentPageClass.PaymentPage(driver)
    else:
        raise Exception('Unknown Page: {} Section: {}'.format(page, section))
    return return_page_obj
