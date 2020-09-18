from appium import webdriver
import time
import unittest
import json
import os.path


class FirstTest(unittest.TestCase):
    def setUp(self):
        path = os.path.dirname(os.path.join(os.path.abspath(''), os.pardir))
        with open('../data/desired_cap.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        desired_cap = {
            "deviceName": data['deviceName'],
            "app": path + data['app'],
            "platformName": data['platformName']
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
