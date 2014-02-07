# -*- coding: cp936 -*-
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, re
 
class Ffppunits(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.0.2.13:9090/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ffpp_untis(self):
        #u"""工单录入"""
        driver = self.driver
        driver.get(self.base_url + "/hwatop-ffpp-server/")
        driver.find_element_by_id("loginname").clear()
        driver.find_element_by_id("loginname").send_keys("hn")
        driver.find_element_by_id("loginpwd").clear()
        driver.find_element_by_id("loginpwd").send_keys("1")
        driver.find_element_by_id("btnlogin").click()
        driver.maximize_window()
        #driver.find_element_by_link_text(u"火情").click()
        element=WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_link_text(u"火情"))
        element.click()
        #添加智能等待
        driver.implicitly_wait(30)
        #查找应急值守模块
        driver.find_element_by_link_text(u"应急值守").click()
        time.sleep(3)
        #弹出录入工单界面
        #定位iframe
        driver.switch_to_frame("mainalarm")
        #print len(dr.find_elements_by_class_name("button"))
        driver.find_element_by_xpath(u"//input[@value='工单录入']").click()
        time.sleep(1)
        #切换到另一个iframe
        driver.switch_to_frame("fancybox-frame")
        sj=driver.find_element_by_id("alarm_input_city")
        sj.find_element_by_xpath("//option[@value='410100']").click()
        driver.find_element_by_id("alarm_input_county").find_element_by_xpath("//option[@value='410101']").click()
        driver.find_element_by_id("alarm_messas_form_crimeReportBean_reportman").clear()
        aa=driver.find_element_by_id("alarm_messas_form_crimeReportBean_reportman").get_attribute('type')
        #接警来源
        driver.find_element_by_id("alarmFrom").find_element_by_xpath("//option[@value='0']").click()
        #报警人
        driver.find_element_by_id("alarm_messas_form_crimeReportBean_reportman").send_keys(u"王小汪")
        driver.find_element_by_id("telOrMPhone").clear()
        driver.find_element_by_id("telOrMPhone").send_keys("13655555555")
        driver.find_element_by_id('alarm_data_messes').send_keys('2013-12-21')
        #设置火灾类型
        firetype=driver.find_element_by_id("alarm_messas_form_crimeReportBean_firecategory")
        firetype.find_element_by_xpath("//option[@value='2']").click()
        #设置火灾级别
        #driver.find_element_by_id("alarm_messas_form_crimeReportBean_degree").find_element_by_xpath("//option[@value='2']").click()
        #设置火点环境
        #driver.find_element_by_id("alarm_messas_form_crimeReportBean_environment").find_element_by_xpath("//option[@value='1']").click()
        print "33"
        #driver.find_element_by_name('crimeReportBean.location').send_keys('qqq')
        driver.find_element_by_name('crimeReportBean.x').send_keys('106')
        driver.find_element_by_name('crimeReportBean.y').send_keys('30')
        print len(driver.find_elements_by_class_name("checkbox"))
        driver.find_element_by_id("alarm_messas_firecheck").click()
        driver.find_element_by_id("alarm_messas_createFire").click()
        driver.find_element_by_name("fireName").send_keys(u"河南777大火")
        driver.find_element_by_xpath(u"//input[@value='添加']").click()
        time.sleep(2)
        print "ww"
        #获取网页上的警告信息
        alert=driver.switch_to_alert()
        #接收警告信息
        alert.accept()
        #self.assertEqual(u"添加成功!", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame('mainalarm')
        print "cc"
        driver.find_element_by_id("fancybox-close").click()
        print "11"
        driver.switch_to_default_content()
        driver.find_element_by_link_text(u"退出登录").click()
        time.sleep(2)
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
