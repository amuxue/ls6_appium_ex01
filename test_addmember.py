from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestAddMemeber:

    def setup(self):
        caps={}
        caps["platformName"]="Android"
        caps["platformVersion"] = "6.0"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = "true"
        caps["automationName"] = "uiautomator2"
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()

    def test_open(self):
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"通讯录")]').click()

        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]/parent::*/parent::*/parent::*/parent::*').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/cth"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/parent::*//*[@class="android.widget.EditText"]').send_keys("啊紫")
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"手机")]/parent::*//*[@class="android.widget.EditText"]').send_keys("14444444443")
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@resource-id="com.tencent.wework:id/aj_"]').click()
        sleep(3)
       # result=self.driver.find_element(MobileBy.XPATH,
       #                           '//*[@class="android.widget.Toast"]').text
        # 获取toast提示框内容
        # toast_element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('//*[@text="添加成功"]'))
        # print(toast_element.text)
        # assert toast_element.text == "添加成功"
        # sleep(3)
