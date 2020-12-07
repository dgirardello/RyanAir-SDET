class BasePageLocators:
    COOKIE_POPUP = "div[id='cookie-popup-with-overlay']"
    COOKIE_POPUP_ID = "cookie-popup"
    ACCEPT_ALL_COOKIES = "button[data-ref='cookie.accept-all']"

class MainPageLocators:
    RETURN_TRIP = "fsw-trip-type-button[data-ref='flight-search-trip-type__return-trip']"
    SINGLE_TRIP = "fsw-trip-type-button[data-ref='flight-search-trip-type__one-way-trip']"
    TEXTBOX_DEPARTURE_ID = "input-button__departure"
    TEXTBOX_DESTINATION_ID = "input-button__destination"
    BUTTON_CLEAR_DESTINATION = "button.list__clear-selection.ry-button--anchor-blue.ry-button--anchor"
    FLIGHT_COUNTRIES_TITLE = "div.h4.countries__title"
    FLIGHT_COUNTRIES_CONTAINER = "div.countries__group.ng-star-inserted"
    FLIGHT_COUNTRIES = "span.countries__country-inner"
    FLIGHT_AIRPORTS_TITLE = "div.list__header-title"
    FLIGHT_AIRPORTS_CONTAINER = "div.list__airports-scrollable-container"
    FLIGHT_AIRPORTS = "span[data-ref='airport-item__name']"
    TEXTBOX_DEPARTURE_CALENDAR = "div.input-button__content[data-ref='input-button__dates-from']"
    TEXTBOX_DESTINATION_CALENDAR = "div.input-button__content[data-ref='input-button__dates-to']"
    DEPARTURE_CALENDAR_DATE = "div.calendar-body__cell:not(calendar-body__cell--disabled)[data-id=\'{}\']"
    SEARCH_BUTTON = "button.flight-search-widget__start-search.ng-tns-c74-3.ng-trigger.ng-trigger-collapseExpandCta.ry-button--gradient-yellow"


class TripPageLocators:
    DATE_CAROUSEL_CONTAINER = "div.header__carousel.ng-trigger.ng-trigger-flightCardAnimate"
    FLIGHT_LIST_CONTAINER = "flight-list"
    FLIGHT_LIST_ITEMS = "flight-card"
    FARE_TABLE_CONTAINER = "fare-table-container"
    FARE_CARD_STANDARD = "div-fare-card[data-e2e='fare-card--standard']"
    FARE_CARD_REGULAR = "div-fare-card[data-e2e='fare-card--regular']"
    FARE_CARD_PLUS = "div-fare-card[data-e2e='fare-card--plus']"
    FARE_CARD_FLEXI = "div-fare-card[data-e2e='fare-card--flexi']"
