import allure
import requests
import os


def add_bstack_video(session_id):
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(os.getenv('USER_NAME'), os.getenv('ACCESS_KEY')),
    ).json()
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='Video recording',
        attachment_type=allure.attachment_type.HTML,
    )


def add_bstack_screenshot(browser):
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='Screenshot',
        attachment_type=allure.attachment_type.PNG,
    )


def add_bstack_xml_dump(browser):
    allure.attach(
        browser.driver.page_source,
        name='Screen XML dump',
        attachment_type=allure.attachment_type.XML,
    )
