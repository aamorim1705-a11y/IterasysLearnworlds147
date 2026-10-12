from selenium import webdriver
import time

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        time.sleep(2)
        context.driver.quit()