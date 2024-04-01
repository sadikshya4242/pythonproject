from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.appium_options import AppiumOptions
from appium import webdriver
import time

# Set desired capabilities
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',  # Replace with your device/emulator ID
    'appPackage': 'com.android.calculator2',  # Calculator app package
    'appActivity': '.Calculator',  # Calculator app activity
}

# Set Appium server address
server_address = 'http://localhost:4723/wd/hub'

# Initialize AppiumOptions object
options = AppiumOptions()

# Start the Appium driver
driver = webdriver.Remote(server_address, desired_caps, options=options)

# Wait for the app to load
time.sleep(3)

# Perform a simple calculation
driver.find_element(MobileBy.ID, 'digit_2').click()
driver.find_element(MobileBy.ID, 'op_add').click()
driver.find_element(MobileBy.ID, 'digit_3').click()
driver.find_element(MobileBy.ID, 'eq').click()

# Wait for the result
time.sleep(2)

# Close the app
driver.quit()

print("Test completed successfully!")

