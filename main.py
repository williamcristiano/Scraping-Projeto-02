from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import logging
import pandas as pd



class MercadoLivre:
    def __init__(self,produto,preco_max=None,preco_min=None):
        self.produto = produto
        self.preco_max = preco_max
        self.preco_min = preco_min

        self.URL='https://www.mercadolivre.com.br/'
        self.logger = self.setup_logger()
        self.browser = self.OpenBrowser()
        self.Searche_input()
    
    def setup_logger(self)->logging:
        logger = logging.basicConfig(filename='log_erros.log',level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S')
        return logging.getLogger(__name__)
    
    def OpenBrowser(self)->webdriver.Chrome:
        browser = webdriver.Chrome()
        browser.get(self.URL)
        return browser
    
    
    def Searche_input(self):
        try:
            input_element = WebDriverWait(self.browser,10).until(
            EC.visibility_of_element_located(
            (By.CSS_SELECTOR,'input[id="cb1-edit"]')))

            input_element.send_keys(self.produto)
            input_element.send_keys(Keys.ENTER)
            sleep(10)
            self.search_prod()
            self.logger.info(f'Input Encontrado e enviado com sucesso..')
        except Exception as e:
            self.logger.error(f'Erro na função {self.Searche_input.__name__} {e}')
        finally:
            self.browser.quit()


    def search_prod(self):
        try:
            produtos = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH,'//ol[@class="ui-search-layout ui-search-layout--grid"]//li[@class="ui-search-layout__item"]//div//div[@class="ui-search-result__wrapper"]')))
            self.logger.info(f'{len(produtos)} Produtos foram encontrados')

        except Exception as e:
            self.logger.error(f'Erro ao buscar os produtos {e}')
        lista_produtos = []

        for produto in produtos:
            dict_prod = {}

            try:
                title = produto.find_element(By.CSS_SELECTOR,'h3[class="poly-component__title-wrapper"]').text 
            except Exception as e:
                self.logger.critical(f'Erro ao buscar o title do produto {e}')
            
            try: 
                preco = produto.find_element(By.CSS_SELECTOR,'span[class="andes-money-amount__fraction"]').text
            except Exception as e:
                self.logger.critical(f'Erro ao buscar o preco do produto {e}') 
            
            try:
                link = produto.find_element(By.CSS_SELECTOR,'a[class="poly-component__title"]').get_attribute('href')
            except Exception as e:
                self.logger.critical(f'Erro ao buscar o link do produto {e}') 

            try:
                
                preco_numerico = int(preco.replace('.','').replace(',',''))
                if self.preco_min and preco_numerico < self.preco_min:
                    continue
                if self.preco_max and preco_numerico > self.preco_max:
                    continue

                dict_prod['Loja']='Mercado Livre'
                dict_prod['Nome']=title
                dict_prod['Preco']=preco
                dict_prod['Link']=link
                if dict_prod not in lista_produtos:
                    lista_produtos.append(dict_prod.copy())
            except Exception as e:
                self.logger.error(f'Um ou mais atributos do produtos nao foram encontrados.{e}')
        
        df = pd.DataFrame(lista_produtos) 
        df.to_csv('Produtos_mercado_livre.csv',index=False)

        self.logger.info(f'{len(lista_produtos)} Produtos cadastrados com sucesso')


    



MercadoLivre(produto='Placa de Video',preco_max=3000,preco_min=1000)



















