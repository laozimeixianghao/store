# import time
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()

# driver.get(r"D:\python自动化测试\pythonProject\练习的html\上传文件和下拉列表\autotest.html")
# driver.maximize_window()
#
# driver.find_element_by_id("accountID").send_keys("2314373129")
# driver.find_element_by_id("passwordID").send_keys("CXCX1767121")
# driver.find_element_by_id("areaID").send_keys("北京市")
# driver.find_element_by_id("sexID2").click()
# driver.find_element_by_xpath("//*[@value='winter']").click()
# driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"C:\preview.gif")


# driver.get(r'D:\python自动化测试\pythonProject\练习的html\弹框的验证\dialogs.html')
# driver.maximize_window()
#
# # driver.find_element_by_id('alert').click()
# # driver.switch_to.alert.accept()
# # driver.switch_to.alert.dismiss()
# driver.find_element_by_id('confirm').click()
# driver.switch_to.alert.accept()
# time.sleep(3)

# driver.get("https://www.jd.com/?cu=true&utm_source=haosou-search&utm_medium=cpc&utm_campaign=t_262767352_haosousearch&utm_term=5512151796_0_dc01e6d647784c77bb916a41431785ee")
# driver.maximize_window()
#
# driver.find_element_by_id("key").send_keys("iphone13")
# driver.find_element_by_xpath("//*[@class='button']").click()
# time.sleep(5)
# driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[3]/a/em").click()
# time.sleep(3)
# driver.quit()


# driver.get(r'D:\python自动化测试\pythonProject\练习的html\跳转页面\pop.html')
#
# driver.maximize_window()
# driver.find_element_by_id('goo').click()