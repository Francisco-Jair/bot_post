import os
import time

# import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

desired = DesiredCapabilities.CHROME

# Configurações
username = "nobug_404"
password = "NOBUG#20_23"
email = "nobug404cj@gmail.com"
password_email = "nobug#2022"
video_path = "./video/INDICADOR7.mp4"
caption = "Melhor futebol do mundo"
hashtags = ["#tiktok", "#futebol", "#soccer"]

video_path = os.path.abspath(video_path)  # caminho absoluto do video

# options = uc.ChromeOptions()
options = Options()
options.add_argument("--disable-notifications")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-popup-blocking")
# options.add_argument("--profile-directory=Default")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--disable-plugins-discovery")
# options.add_argument("--incognito")
# options.add_argument("user_agent=DN")
# options.add_argument('--no-sandbox')

service = Service(ChromeDriverManager().install())

# Inicializa o navegador
driver = webdriver.Chrome(service=service, options=options)
# driver = uc.Chrome(service=service, options=options, use_subprocess=True, desired_capabilities=desired)
# driver.implicitly_wait(5)

# Maximiza a janela do navegador
driver.maximize_window()
# driver.fullscreen_window()

# Abre o TikTok
driver.get("https://www.tiktok.com/")

# time.sleep(2)
# driver.find_element(By.ID, 'header-login-button').click()

# Espera até que o botão de login apareça
time.sleep(6)
login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "loginContainer"))
)
# login_button.find_element(By.XPATH, '//*[@id="loginContainer"]/div/div/div[1]/div[4]/div[2]').click()

time.sleep(2)

# ir para nova janela
# nova_janela = driver.window_handles[1]  # assume-se que a nova janela é a segunda na lista de identificadores de janelas
# driver.switch_to.window(nova_janela)

# time.sleep(6)
# driver.delete_all_cookies() # limpa os cookies

# driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(email)
# driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()

# logar com email
login_button.find_element(
    By.XPATH, '//*[@id="loginContainer"]/div/div/div[1]/div[2]'
).click()
login_button.find_element(
    By.XPATH, '//*[@id="loginContainer"]/div/form/div[1]/a'
).click()

time.sleep(2)

login_button.find_element(
    By.XPATH, '//*[@id="loginContainer"]/div/form/div[1]/input'
).send_keys(username)
login_button.find_element(
    By.XPATH, '//*[@id="loginContainer"]/div/form/div[2]/div/input'
).send_keys(password)
login_button.find_element(By.XPATH, '//*[@id="loginContainer"]/div/form/button').click()

print("fazendo o desafio de segurança")
input("Pressione Enter para continuar...")
time.sleep(4)

# Continuar daqui, postar o video
driver.find_element(By.XPATH, '//*[@id="app-header"]/div/div[3]/div[1]/a').click()
time.sleep(2)

# selecionando o input do video
# video_input = driver.find_element(By.CLASS_NAME, 'upload-container')
# video_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)
video_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
video_input.send_keys(video_path)  # tem que ser o caminho absoluto

time.sleep(5)

driver.find_element(
    By.XPATH,
    '//*[@id="tux-portal-container"]/div[2]/div/div/div/div/div[2]/div[2]/div[2]/button[2]',
).click()
time.sleep(2)

# escrever a legenda
driver.find_element(
    By.XPATH,
    '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div',
).clear()
driver.find_element(
    By.XPATH,
    '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div',
).send_keys(caption)
time.sleep(2)

# publicar video
driver.find_element(
    By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[8]/div[2]/button'
).click()
time.sleep(10)
print("Video Publicado com sucesso!")

# ele da a opcoes de carregar mais videos, implementar isso
