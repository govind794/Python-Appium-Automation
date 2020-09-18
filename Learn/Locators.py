from appium import webdriver
import time
import unittest


class LocatorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_cap = {
            "deviceName": "emulator-5554",
            "platformName": "Android",
            "app": "/Users/govind794/Downloads/com.aefyr.sai_2020-06-19.apk",
            # "appPackage": "com.google.android.apps.nexuslauncher",
            # "appWaitActivity": "com.google.android.apps.nexuslauncher.NexusLauncherActivity",
        }
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        cls.driver.implicitly_wait(20)

    @classmethod
    def tearDownClass(cls):
        print("Complate Test Case.")

    def test_find_element_help(self):
        # print(self.driver.title)
        # print(self.driver.capabilities)

        self.driver.find_element_by_id('com.aefyr.sai:id/ib_help').click()

        element_text = self.driver.find_element_by_id('com.aefyr.sai:id/alertTitle')
        print(element_text.text)
        self.assertEqual('Help', element_text.text)

        element_ok = self.driver.find_element_by_id('android:id/button1')
        print(element_ok.text)
        self.assertEqual('OK', element_ok.text)
        element_ok.click()

    def test_find_element_theme(self):
        self.driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Select theme"]').click()
        theme = self.driver.find_element_by_id('com.aefyr.sai:id/tv_bottom_sheet_dialog_base_title')
        print(theme.text)
        self.assertEqual('Select theme', theme.text)

        get_theme_text = self.driver.find_elements_by_class_name('android.widget.TextView')
        for i in get_theme_text:
            if i.text == 'Mint':
                self.assertEqual('Mint', i.text)

        theme_items = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[11]')
        theme_items.click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LocatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
