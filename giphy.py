#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import requests
import time

api_endpoint = "http://api.giphy.com/v1/gifs/" \
                "random?api_key=dc6zaTOxFJmzC&rating=y"


def focus_to_browser(browser):
    browser.execute_script("alert('Have Fun !')")
    alert = browser.switch_to_alert()
    alert.accept()


def random_gif_url():
    is_gif_optimal = False
    data = None

    while not is_gif_optimal:
        response = requests.get(api_endpoint)
        data = response.json()

        is_gif_optimal = (
            int(data["data"]["image_frames"]) < 250 and
            int(data["data"]["image_width"]) >= 250 and
            int(data["data"]["image_height"]) >= 250)

    url = data["data"]["url"]
    url += "/tile"

    return url


def setup_browser():
    options = Options()
    options.add_argument('--kiosk')
    driver = webdriver.Chrome(desired_capabilities=options.to_capabilities())

    return driver


def run():
    browser = setup_browser()

    while True:
        browser.get(random_gif_url())
        focus_to_browser(browser)
        time.sleep(300)


run()
