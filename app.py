#!/usr/bin/python
# -*- coding:utf-8 -*-
import base64
import logging
from io import BytesIO

import requests
from PIL import Image

from lib.render import Renderer, TestRunner, WeatherDisplay
from lib.waveshare_epd import epd7in3e

logging.basicConfig(level=logging.DEBUG)

BASE_URL = "https://hko-flask-ink-display.onrender.com"
END_POINT = f'{BASE_URL}/weather'


def main():
    renderer = Renderer()
    test = TestRunner()
    weather_display = WeatherDisplay()

    try:
        logging.info("epd7in3e Demo")

        # test
        test.render()
        test.clear_and_sleep()

        # fetch from API
        logging.info("Fetching Weather Image")
        res = requests.get(END_POINT)
        res.raise_for_status()

        logging.info("Converting Image to Draw Object")
        image = Image.open(BytesIO(base64.b64decode(res.text)))
        weather_display.display(image)

        # clear and sleep
        renderer.clear_and_sleep()

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd7in3e.epdconfig.module_exit(cleanup=True)
        exit()


if __name__ == '__main__':
    main()
