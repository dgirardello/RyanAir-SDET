class BasePageLocators:
    LOGIN_POPUP = "div.dialog.signup-dialog"
    LOGIN_POPUP_EMAIL = "input[name='email']"
    LOGIN_POPUP_PASSWORD = "input[name='password']"
    LOGIN_POPUP_LOGIN_BUTTON = "button.auth-submit__button[type='submit']"
    PROFILE_AREA = "div.profile-area.ng-star-inserted"


class MainPageLocators:
    COOKIE_POPUP = "div[id='cookie-popup-with-overlay']"
    ACCEPT_ALL_COOKIES = "button[data-ref='cookie.accept-all']"
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
    COOKIE_POPUP_ID = "cookie-popup"
    COOKIE_POPUP = "div.cookie-popup"
    ACCEPT_ALL_COOKIES = "button[data-ref='cookie.accept-all']"
    SHOPPING_CART_AMOUNT = "ry-price"
    SHOPPING_CART_AMOUNT_SYMBOL = "span.price__symbol"
    SHOPPING_CART_AMOUNT_INT = "span.price__integers"
    SHOPPING_CART_AMOUNT_DEC = "span.price__decimals"
    SHOPPING_CART_BUTTON = "div.basket-total-icon"
    SHOPPING_CART_DETAILS_CONTAINER = "ry-price-breakdown-container"
    SHOPPING_CART_DETAILS_CHECKOUT_BUTTON = "button.ry-button--full.ry-button--gradient-yellow[data-ref='basket-continue-flow__check-out']"

    class FlightSelection:
        DATE_CAROUSEL_CONTAINER = "div.header__carousel.ng-trigger.ng-trigger-flightCardAnimate"
        FLIGHT_LIST_CONTAINER = "flight-list"
        FLIGHT_LIST_ITEMS = "flight-card"
        FARE_TABLE_CONTAINER = "fare-table-container"
        FARE_CARD_STANDARD = "div.fare-card[data-e2e='fare-card--standard']"
        FARE_CARD_REGULAR = "div.fare-card[data-e2e='fare-card--regular']"
        FARE_CARD_PLUS = "div.fare-card[data-e2e='fare-card--plus']"
        FARE_CARD_FLEXI = "div.fare-card[data-e2e='fare-card--flexi']"
        LOGIN_BOX = "ry-login-touchpoint-container"
        LOGIN_BOX_LOGIN_LATER_LINK = "span.login-touchpoint__login-later.h3"
        LOGIN_BOX_LOGIN_BUTTON = "button[data-ref='login-touchpoint__log_in_button']"
        PASSENGERS_SECTION_CONTAINER = "div.form-outer-wrapper.ng-star-inserted"
        PASSENGERS_SECTION_CONTAINER_INNER_DIV = "div.form-wrapper"
        PASSENGERS_SECTION_SAVED_COMPANION_BUTTON = "div.bubble[role='button']"
        PASSENGERS_SECTION_TITLE_BOX = "button.dropdown__toggle.b2[type='button']"
        PASSENGERS_SECTION_FIRST_NAME_BOX = "input[id='formState.passengers.ADT-0.name']"
        PASSENGERS_SECTION_LAST_NAME_BOX = "input[id='formState.passengers.ADT-0.surname']"
        PASSENGERS_SECTION_CONTINUE_BUTTON = "button.continue-flow__button.ry-button--gradient-yellow"

    class SeatSelection:
        SEAT_MAP_CONTAINER = "seat-map"
        LIST_BUTTON_SEAT_PRIORITY = "button.ng-star-inserted.seatmap__seat.seatmap__seat--priority"
        LIST_BUTTON_SEAT_STANDARD = "button.ng-star-inserted.seatmap__seat.seatmap__seat--standard"
        BUTTON_SEAT_SELECTED = "button.ng-star-inserted.seatmap__seat.seatmap__seat--selected"
        SEAT_TOOLTIP_DESIGNATOR = "div.seat-tooltip__designator"
        RIGHT_PANEL_SEAT_EMPTY = "div.seat-badge"
        RIGHT_PANEL_SEAT_SELECTED = "div.seat-badge.seat-badge--seat-selected"
        BUTTON_CONTINUE = "button.seats-action__button[data-ref='seats-action__button-continue']"

    class BagsSelection:
        BAGS_CARD_CONTAINER = "bags-bag-card"
        BUTTON_CONTINUE_CONTAINER = "bags-continue-flow-container"
        BUTTON_CONTINUE = "button.ry-button--gradient-yellow"

    class Extras:
        EXTRAS_LIST_CONTAINER = "products-list-container"
        BUTTON_CONTINUE = "button.ry-button--full.ng-tns-c167-1.ry-button--gradient-yellow.ry-button--large"

    class OverviewSection:
        PILLARS_CONTAINER = "div.pillars-container__pillars"


class PaymentPageLocators:
    CONTACT_DETAILS_CONTAINER = "contact-details"
    INSURANCE_CONTAINER = "div.insurance__content-description"
    INSURANCE_PLUS_CHECK = "ry-checkbox.ry-checkbox--rounded[inputid='insurance-opt-in']"
    INSURANCE_NO_CHECK = "ry-checkbox.ry-checkbox--rounded[inputid='insurance-opt-out']"
    PAYMENT_CONTAINER = "payment-methods"
    PAYMENT_INPUT = "input.b2"
    DROPDOWN_CONTAINER = "div.select"
    DROPDOWN_BUTTON = "button.dropdown__toggle.b2"
    DROPDOWN_ITEMS = "ry-dropdown-item"
    PAYMENT_CARD_FORM_CONTAINER = "card-details"
    PAYMENT_CARD_NUMBER_CONTAINER = "ry-input-d.modal__input[data-ref='add-card-modal__account-number']"
    PAYMENT_CARD_EXPIRE_CONTAINER = "expiry-date"
    PAYMENT_CARD_CVV_CONTAINER = "verification-code"
    PAYMENT_CARD_NAME_CONTAINER = "ry-input-d.ng-pristine[formcontrolname='accountName']"
    PAYMENT_CARD_ADDRESS_FORM_CONTAINER = "address-form"
    PAYMENT_CARD_ADDRESS_LINE1_CONTAINER = "ry-input-d.address-form__input[data-ref='add-card-modal__address-line-1']"
    PAYMENT_CARD_ADDRESS_CITY_CONTAINER = "ry-input-d.address-form__input[data-ref='add-card-modal__city']"
    PAYMENT_CARD_ADDRESS_COUNTRY_CONTAINER = "ry-autocomplete.address-form__input[formcontrolname='country']"
    PAYMENT_CARD_ADDRESS_COUNTRY_LABEL = "label._label--dropdown"
    PAYMENT_CARD_ADDRESS_POSTCODE_CONTAINER = "ry-input-d.address-form__shrinked-field[formcontrolname='postcode']"
    PAYMENT_PAY_NOW_BUTTON = "button.pay-button.ry-button--gradient-yellow"
    PAYMENT_ACCEPT_CONDITIONS = "ry-checkbox.terms-and-conditions__checkbox"
    PAYMENT_ERROR_CONTAINER = "div.payment-methods__error-message.ng-star-inserted"





