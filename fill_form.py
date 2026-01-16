import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

from download_xlsx import download_excel # Importa a função de download do arquivo Excel

def fill_form_from_excel(download_url: str, form_url: str):

    #Baixar o arquivo Excel
    excel_filename = download_excel(download_url)
    if not excel_filename or not os.path.exists(excel_filename):
        print("Download do arquivo Excel falhou. Abortando o processo.")
        return


    #Iniciar o Driver
    driver = webdriver.Chrome()     

    #Ler o arquivo Excel
    df = pd.read_excel(excel_filename)
    df.columns = df.columns.str.strip()  # Remover espaços em branco (Last Name)
    driver.get(form_url)

    # Inicia o desafio 
    start_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Start']")))
    start_button.click()

    for index, row in df.iterrows():            
        # Obter dados da linha
        first_name = str(row.get("First Name", ""))
        last_name = str(row.get("Last Name", ""))
        company_name = str(row.get("Company Name", ""))
        role_in_company = str(row.get("Role in Company", ""))
        address = str(row.get("Address", ""))
        email = str(row.get("Email", ""))
        phone_number = str(row.get("Phone Number", ""))

        # First Name
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name='labelFirstName']"))).send_keys(first_name)

        # Last Name
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name='labelLastName']"))).send_keys(last_name)

        # Phone Number
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name='labelPhone']"))).send_keys(phone_number)

        # Address
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name='labelAddress']"))).send_keys(address) 

        # Company Name
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name='labelCompanyName']"))).send_keys(company_name)

        # Role in Company
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name='labelRole']"))).send_keys(role_in_company)

        # Email
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name='labelEmail']"))).send_keys(email)

        # Clicar em Submit
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Submit']"))).click()

    time.sleep(15)  # Conferir resultados antes de fechar
    driver.quit()

