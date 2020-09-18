__author__ = 'Aditya Roy'

from Src.TestBase.Environment import EnvironmentSetup
from Src.PageObject.Pages.OpenPage import OpenPage
from Test.TestUtility.ScreenShot import ScreenShot
import unittest


class Flipcart_OpenPage(EnvironmentSetup):

    def test_Open_Page(self):

        # Screenshots relative paths
        ss_path = "/Test_Flipcart_OpenPage/"

        # Using the driver instances created in EnvironmentSetup
        driver = self.driver
        # self.driver.get("http://newtours.demoaut.com/")
        self.driver.set_page_load_timeout(20)

        # Creating object of SS screenshots utility
        # ss = SS(driver)
        ss = ScreenShot(driver)
        # expected_title = "Welcome: Mercury Tours"
        # Validating Page title with the expected one through catching exception
        try:
            if driver.title == expected_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title, expected_title)
        except Exception as e:
            print(e + "WebPage Failed to load")

        # verifying if the logo present or not in homepage
        # creating an instance of class and passing the current driver instance

        m = Home(driver)
        if m.getLogo().is_displayed():
            print(m.getLogo().get_attribute('alt') + " Logo Successfully Displayed")
        else:
            print("Mercury Logo not Displayed")
        # asserting other elements in the home page
        try:
            print("SignOn Link " + m.getSignOn().get_attribute('href'))
            print("Contact Link " + m.getContact().get_attribute('href'))
            print("Register Link " + m.getRegister().get_attribute('href'))
            print("Support Link " + m.getSupport().get_attribute('href'))
        except Exception as e:
            print(e)
            print("Element not present")

        ss.AllScreenShot(ss_path + "home.png")


if __name__ == '__main__':
    unittest.main()
