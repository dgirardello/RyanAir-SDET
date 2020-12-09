from selenium import webdriver
from features.steps.constants import PAGE_MAIN
from features.pages.PageFactory import get_page_object
from selenium.webdriver.support.ui import WebDriverWait


def before_all(context):
    if 'CHROME' in str(context.config.userdata['browser']).upper():
        context.driver = webdriver.Chrome()
    else:
        context.driver = webdriver.Firefox()
    context.driver.maximize_window()


def before_step(context, step):
    if 'YES' in str(context.config.userdata['slow_connection']).upper():
        WebDriverWait(context.driver,
                      int(context.config.userdata['slow_connection_wait_seconds']))


def before_scenario(context, scenario):
    page_tag = next((tag for tag in scenario.tags if 'Page' in tag), 'Page:{}'.format(PAGE_MAIN))
    context.page = page_tag.split('.')[1].upper()

    section_tag = next((tag for tag in scenario.tags if 'Section' in tag), None)
    context.section = section_tag.split('.')[1].upper() if section_tag is not None else None

    context.current_page = get_page_object(page=context.page, section=context.section, driver=context.driver)


def after_all(context):
    context.driver.quit()