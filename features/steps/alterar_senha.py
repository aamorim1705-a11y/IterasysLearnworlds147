# 1 - Bibliotecas / Imports
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# ===================================
# ALTERAR SENHA COM DADOS VÁLIDOS
# ===================================   
@when(u'clico no botao Editar na secçao Segurança da conta')
def step_impl(context):
    elemento = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#security button.learnworlds-button-small"))); elemento.click()

@when(u'preencho os campos senha atual, nova senha e confirmação da nova senha')
def step_impl(context):

    senha_atual = os.getenv("ITERASYS_CURRENT_PASSWORD")
    nova_senha = os.getenv("ITERASYS_NEW_PASSWORD")

    campos = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "#security input[type='password']")
        )
    )

    campos[0].click()
    campos[0].send_keys(senha_atual)

    campos[1].click()
    campos[1].send_keys(nova_senha)

    campos[2].click()
    campos[2].send_keys(nova_senha)

@when(u'clico no botao Salvar da Segurança da conta')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#security button.lw-brand-text").click()

# ===================================
# ALTERAR SENHA COM DADOS INVÁLIDOS
# ===================================   
# ====================
# SENHA ATUAL VAZIA
# =====================
@when(u'preencho os campos senha atual , nova senha VALIDA e confirmação da nova senha VALIDA')
def step_impl(context):

    nova_senha = os.getenv("ITERASYS_NEW_PASSWORD")

    campos = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "#security input[type='password']")
        )
    )

    campos[0].click()

    campos[1].click()
    campos[1].send_keys(nova_senha)

    campos[2].click()
    campos[2].send_keys(nova_senha)

# ==================
# NOVA SENHA VAZIA
# ==================
@when(u'preencho os campos senha atual VALIDA, nova senha  e confirmação da nova senha VALIDA')
def step_impl(context):

    senha_atual = os.getenv("ITERASYS_CURRENT_PASSWORD")
    nova_senha = os.getenv("ITERASYS_NEW_PASSWORD")

    campos = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "#security input[type='password']")
        )
    )

    campos[0].click()
    campos[0].send_keys(senha_atual)

    campos[1].click()

    campos[2].click()
    campos[2].send_keys(nova_senha)

# ==================================
# CONFIRMAÇÃO DA NOVA SENHA VAZIA
# ==================================
@when(u'preencho os campos senha atual VALIDA, nova senha VALIDA e confirmação da nova senha ')
def step_impl(context):

    senha_atual = os.getenv("ITERASYS_CURRENT_PASSWORD")
    nova_senha = os.getenv("ITERASYS_NEW_PASSWORD")

    campos = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "#security input[type='password']")
        )
    )

    campos[0].click()
    campos[0].send_keys(senha_atual)

    campos[1].click()
    campos[1].send_keys(nova_senha)

    campos[2].click()

# =================
# VALIDAR DADOS
# =================   
@then(u'senha é atualizada com sucesso')
def step_impl(context):
    erros = context.driver.find_elements(
        By.CSS_SELECTOR,
        "#security .lw-red-text"
    )

    assert len(erros) == 0, f"Erro encontrado: {[erro.text for erro in erros]}"

@then(u'exibe a {mensagem} com erro') 
def step_impl(context, mensagem): 
    assert context.driver.find_element(By.CSS_SELECTOR,"#security span.lw-red-text").text == mensagem

# =====================================
# TEARDOWN
# =====================================
def after_scenario(context, scenario):
    context.driver.quit()