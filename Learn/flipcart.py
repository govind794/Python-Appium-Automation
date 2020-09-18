from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

# Desired Capabilities

desired_cap = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "app": "/Users/govind794/PycharmProjects/AppiumSandbox/app/com.flipkart.android.apk",
    "appPackage": "com.flipkart.android",
    "appWaitActivity": "com.flipkart.android.activity.MSignupActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(20)

driver.find_element_by_id("com.flipkart.android:id/btn_skip").click()

driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Drawer"]').click()

driver.find_element_by_xpath('//android.widget.TextView[@text="Electronics"]').click()
driver.find_element_by_xpath('//android.widget.TextView[@text="Laptops"]').click()

# driver.find_element_by_id('com.flipkart.android:id/not_now_button').click()

# Touch Actions
# TouchAction(driver)   .press(x=538, y=1425)   .move_to(x=577, y=840)   .release()   .perform()

for i in range(3):
    touch = TouchAction(driver)
    touch.press(x=550, y=1514).move_to(x=573, y=855).release().perform()
    time.sleep(3)

# driver.find_element_by_xpath(
#     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[2]').click()

driver.quit()
