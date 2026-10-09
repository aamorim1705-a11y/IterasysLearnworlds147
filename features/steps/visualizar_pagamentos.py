# 1 - Bibliotecas / Imports
from behave import when, then
from selenium.webdriver.common.by import By

# ===================================
# VISUALIZAR HISTÓTICO DE PAGAMENTOS
# =================================== 
@when(u'clico no botao Pagamentos')
def step_impl(context):  
    context.driver.find_element(By.CSS_SELECTOR, "a[href='#payments']").click()

@then(u'o histórico de pagamentos é apresentado para consulta')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "[data-testid='payment-history-table']").is_displayed()

# =====================================
# TEARDOWN
# =====================================
def after_scenario(context, scenario):
    context.driver.quit()

