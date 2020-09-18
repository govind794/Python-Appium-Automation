__author__ = 'Govind Patidar'


class ScreenShot(object):

    def __init__(self, driver):
        self.driver = driver

    def AllScreenShot(self, path):
        directory = "/Users/govind794/PycharmProjects/AppiumSandbox/ScreenShots"
        self.driver.get_screenshot_as_file(directory + path)
