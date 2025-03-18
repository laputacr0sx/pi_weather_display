import logging
import time

from PIL import Image, ImageDraw

from lib.waveshare_epd import epd7in3e

logging.basicConfig(level=logging.DEBUG)
logging.info("epd7in3f Demo")


class Renderer:
    def __init__(self):
        self.epd = epd7in3e.EPD()
        self.epd.init()
        self.epd.Clear()

    def render(self):
        pass

    def display(self, image: Image.ImageFile):
        pass

    def clear_and_sleep(self):
        logging.info("Clear...")
        self.epd.Clear()
        logging.info("Goto Sleep...")
        self.epd.sleep()


class TestRunner(Renderer):
    def render(self):
        # Drawing on the image
        logging.info("1.Drawing on the image...")
        test_background_image = Image.new('RGB', (self.epd.width, self.epd.height), self.epd.WHITE)  # 255: clear the frame
        draw = ImageDraw.Draw(test_background_image)

        draw.line((5, 170, 80, 245), fill=self.epd.BLUE)
        draw.line((80, 170, 5, 245), fill=self.epd.YELLOW)
        draw.rectangle((5, 170, 80, 245), outline=self.epd.BLACK)
        draw.rectangle((90, 170, 165, 245), fill=self.epd.GREEN)
        draw.arc((5, 250, 80, 325), 0, 360, fill=self.epd.RED)
        draw.chord((90, 250, 165, 325), 0, 360, fill=self.epd.YELLOW)
        self.epd.display(self.epd.getbuffer(test_background_image))
        time.sleep(3)


class WeatherDisplay(Renderer):
    def display(self, image: Image.ImageFile):
        self.epd.init()
        self.epd.Clear()
        self.epd.display(self.epd.getbuffer(image))
        time.sleep(3)
