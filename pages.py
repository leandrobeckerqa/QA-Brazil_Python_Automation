from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code
import time


class UrbanRoutesPage:

    # De e Para
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    #Escolher tarifa e chamar o carro
    taxi_option_locator = (By.XPATH, "//button[@class='button round']")
    comfort_icon_locator = (By.XPATH, '//img[@alt="Comfort"]')
    comfort_active = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')

    #Telefone
    number_text_locator = (By.CSS_SELECTOR, '.np-button')
    number_enter = (By.ID, 'phone')
    number_confirm = (By.CSS_SELECTOR, '.button.full')
    number_code = (By.ID, 'code')
    code_confirm = (By.XPATH, '//button[contains(text(), "Confirmar") or contains(text(), "Confirm")]')
    number_finish = (By.CSS_SELECTOR, '.np-text')

    #Cartão
    add_metodo_pagamento = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card = (By.CSS_SELECTOR, '.pp-plus')
    number_card = (By.ID, 'number')
    code_card = (By.CSS_SELECTOR, 'input.card-input#code')
    add_finish_card = (By.XPATH, "//button[contains(text(),'Add')]")
    close_button_card = (By.CSS_SELECTOR, '.payment-picker.open .close-button')
    confirm_card = (By.CSS_SELECTOR, '.pp-value-text')


    def __init__(self,driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        self.driver.find_element(*self.from_field).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.to_field).send_keys(to_text)

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def get_from_location_value(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.from_field)).get_attribute('value')

    def get_to_location_value(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.to_field)).get_attribute('value')

    def click_taxi_options(self):
        self.driver.find_element(*self.taxi_option_locator).click()

    def click_comfort_icon(self):
        wait = WebDriverWait(self.driver, 5)
        self.driver.find_element(*self.comfort_icon_locator).click()

    def click_comfort_active(self):
        try:
            active_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((self.comfort_active)))
            return "active" in active_button.get_attribute('class')
        except:
            return False

    def get_from_location_value(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.from_field)).get_attribute('value')

    def click_number_text(self, telefone):
        self.driver.find_element(*self.number_text_locator).click()

        self.driver.find_element(*self.number_enter).send_keys(telefone)

        self.driver.find_element(*self.number_confirm).click()

        code = retrieve_phone_code(self.driver) #Digita código
        code_imput = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((self.number_code)))
        code_imput.clear()
        code_imput.send_keys(code)

        self.driver.find_element(*self.code_confirm).click()

    def numero_confirmado(self):
        numero = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((self.number_finish)))
        return numero.text

    def click_add_cartao(self,cartao,code):
        self.driver.find_element(*self.add_metodo_pagamento).click()
        time.sleep(3)
        self.driver.find_element(*self.add_card).click()
        time.sleep(3)
        self.driver.find_element(*self.number_card).send_keys(cartao)
        time.sleep(3)
        self.driver.find_element(*self.code_card).send_keys(code)
        time.sleep(5)
        self.driver.find_element(*self.add_finish_card).click()
        time.sleep(3)
        self.driver.find_element(*self.close_button_card).click()

    def confirm_cartao(self):
        return self.driver.find_element(*self.confirm_card).text

