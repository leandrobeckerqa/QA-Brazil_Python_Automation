from selenium.webdriver.support.expected_conditions import element_selection_state_to_be
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print('Conectado ao servidor Urban Routes')
        else:
            print('Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução')

    def test_set_route(self):
        # Adicionar em S8
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from_location_value() == data.ADDRESS_FROM
        assert routes_page.get_to_location_value() == data.ADDRESS_TO
        print("função criada para definir a rota")
        pass

    def test_select_plan(self):
        # Adicionar em S8
        print("função criada para selecionar o plano")
        pass

    def test_fill_phone_number(self):
        # Adicionar em S8
        print("função criada para preencher número de telefone")
        pass

    def test_fill_card(self):
        # Adicionar em S8
        print("função criada para preencher número do cartão de crédito")
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("função criada para enviar comentário para motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("função criada para enviar pedidos de cobertor e guardanapos")
        pass

    def test_order_2_ice_creams(self):
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            # Adicionar em S8
            print("função criada para enviar pedido de sorvete")
            pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("função criada para verificar se aparece o modelo do carro")
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


