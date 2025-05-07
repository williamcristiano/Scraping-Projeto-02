from utils import *
from utils import set_settings

class MercadoLivre:
    
    def __init__(self,produto,preco_max=None,preco_min=None):
        self.settings = set_settings(url='https://www.mercadolivre.com.br/',loja_nome='mercado_livre')
        
        self.produto = produto
        self.preco_max = preco_max
        self.preco_min = preco_min
        
        self.browser = self.settings.OpenBrowser()
        self.logger = self.settings.setup_logger()

        self.Searche_input()
    
   
    def Searche_input(self):
        try:
            input_element = WebDriverWait(self.browser,10).until(
            EC.visibility_of_element_located((
            By.CSS_SELECTOR,'input[id="cb1-edit"]')))
            
            input_element.send_keys(self.produto)
            input_element.send_keys(Keys.ENTER)
            sleep(5)
            self.search_prod()
            self.logger.info(f'Input Encontrado e enviado com sucesso..')
        except Exception as e:
            self.logger.error(f'Erro na função {self.Searche_input.__name__} ')
        finally:
            self.browser.quit()


    def search_prod(self):
        try:
            produtos = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH,'//ol[@class="ui-search-layout ui-search-layout--grid"]//li[@class="ui-search-layout__item"]//div//div[@class="ui-search-result__wrapper"]')))
            self.logger.info(f'{len(produtos)} Produtos foram encontrados')

        except Exception as e:
            self.logger.error(f'Erro ao buscar os produtos ')
        lista_produtos = []

        for produto in produtos:
            dict_prod = {}

            try:
                title = produto.find_element(By.CSS_SELECTOR,'h3[class="poly-component__title-wrapper"]').text 
            except Exception as e:
                self.logger.critical(f'Erro ao buscar o title do produto ')
            
            try: 
                preco = produto.find_element(By.CSS_SELECTOR,'span[class="andes-money-amount__fraction"]').text
            except Exception as e:
                self.logger.critical(f'Erro ao buscar o preco do produto ') 
            
            try:
                link = produto.find_element(By.CSS_SELECTOR,'a[class="poly-component__title"]').get_attribute('href')
            except Exception as e:
                self.logger.critical(f'Erro ao buscar o link do produto ') 

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
                self.logger.error(f'Um ou mais atributos do produtos nao foram encontrados.')
        
        df = pd.DataFrame(lista_produtos) 
        df.to_csv('data_prod/Produtos_mercado_livre.csv',index=False)

        self.logger.info(f'{len(lista_produtos)} Produtos cadastrados com sucesso')


    

if __name__ == "__main__":
    MercadoLivre(produto='Placa de Video',preco_max=3000,preco_min=1000)



















