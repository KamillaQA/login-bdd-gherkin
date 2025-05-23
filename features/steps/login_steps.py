from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

@given('que o usuário está na página de login')
def step_impl(context):
    context.driver = webdriver.Chrome()
    path = os.path.abspath("C:/Users/92006/Desktop/Logica/Projeto_BDD_Cherkin/login.html")
    context.driver.get(f"file:///{path}")
    context.driver.maximize_window()

@when('ele insere o email "{email}" e a senha "{senha}"')
def step_impl(context, email, senha):
    context.driver.find_element(By.ID, 'email').send_keys(email)
    context.driver.find_element(By.ID, 'senha').send_keys(senha)

@when('clica no botão entrar')
def step_impl(context):
    context.driver.find_element(By.ID, 'entrar').click()

@then('ele deve ver o painel inicial')
def step_impl(context):
    time.sleep(2)  # só para esperar a página carregar, usar WebDriverWait é melhor
    assert context.driver.find_element(By.ID, 'painel-inicial')
    context.driver.quit()
