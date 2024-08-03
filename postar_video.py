import time

import undetected_chromedriver as uc
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from botpost import list_all_file_folders, path_abs

desired = DesiredCapabilities.CHROME


# Configurações
username = "nobug_404"
password = "NOBUG#20_23"
email = "nobug404cj@gmail.com"
password_email = "nobug#2022"
video_path = list_all_file_folders("video_processado")
caption = "Melhor futebol do mundo"
hashtags = ["#tiktok", "#futebol", "#soccer"]

# video_path = os.path.abspath(video_path)  # caminho absoluto do video

options = uc.ChromeOptions()
# options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--profile-directory=Default")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--incognito")
options.add_argument("--user_agent=DN")
options.add_argument("--no-sandbox")

service = Service(ChromeDriverManager().install())

# Inicializa o navegador
# driver = webdriver.Chrome(service=service, options=options)
driver = uc.Chrome(
    service=service, options=options, use_subprocess=True, desired_capabilities=desired
)
# driver.implicitly_wait(5)

# Maximiza a janela do navegador
driver.maximize_window()
# driver.fullscreen_window()

# Abre o TikTok
driver.get("https://www.tiktok.com/")

# Espera até que o botão de login apareça
time.sleep(6)
login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "loginContainer"))
)

time.sleep(2)

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
time.sleep(5)

# selecionando o input do video
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

# funcao para postar todos os videos cortados
for video_p in video_path:
    video_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    video_input.send_keys(
        path_abs(f"video_processado/{video_p}")
    )  # tem que ser o caminho absoluto

    time.sleep(8)  # tempo de carregar o video

    # Limpando a legenda
    driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div',
    ).clear()
    time.sleep(2)

    # escrever a legenda

    driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div',
    ).send_keys(caption)
    time.sleep(2)

    # publicar video
    driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[8]/div[2]/button',
    ).click()
    time.sleep(12)  # aumentar temp0
    print("Video Publicado com sucesso!")

    # Clicando em carregar mais videos
    # Colocar tag para clicar so quando carregar
    driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[9]/div/div[2]/div[1]',
    ).click()
    time.sleep(2)


driver.quit()

# # clicar em gerenciar suas publicacoes
# # driver.find_element(
# #     By.XPATH,
# #     '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[9]/div/div[2]/div[2]',
# # ).click()
