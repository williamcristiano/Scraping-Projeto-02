from utils import *
from utils import set_settings 


class KabumScraping:
    def __init__(self,produto,preco_max=None,preco_min=None):
        self.settings = set_settings(url="https://www.kabum.com.br/",loja_nome='kabum',)
        
        self.produto = produto
        self.preco_max = preco_max
        self.preco_min = preco_min

    
    def run_scraping_kabum(self):
        self.browser = self.settings.OpenBrowser()
        self.logger = self.settings.setup_logger()
        try:
            input_button = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR,'input[id="input-busca"]')))
            input_button.send_keys('Placa de Video')
            input_button.send_keys(Keys.ENTER)
            sleep(10)
            self.logger.info(f'Input Encontrado e enviado com sucesso..')
            self.__search_prod()
        except Exception as e:
            self.logger.error(f'Erro na função {self.run_scraping_kabum.__name__} ')
        finally:
            self.browser.quit()

    def __search_prod(self):
        try:
            self.logger.info('Iniciando a busca pelos produtos')
            produtos = WebDriverWait(self.browser,10).until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR,'article[class="sc-27518a44-3 hLEhJe productCard"]')))
            self.logger.info(f'{len(produtos)} Produtos foram encontrados')
        except Exception as e:
            self.logger.error(f'Erro ao encontrar os produtos {e}')
            return
        lista_prod = []

        for prod in produtos:
            dict_prod={}
            title = preco = link = preco_numerico = None

            try:
                title = prod.find_element(By.CSS_SELECTOR,'span[class="sc-d79c9c3f-0 nlmfp sc-27518a44-9 iJKRqI nameCard"]').text
            except Exception as e:
                self.logger.critical('Erros ao buscar o nome produto')

            try:
                preco = prod.find_element(By.CSS_SELECTOR,'span[class="sc-57f0fd6e-2 hjJfoh priceCard"]').text.replace('R$','').replace(' ','')
            except:
                self.logger.critical('Erros ao buscar o preco do  produto')

            try:
                link = prod.find_element(By.CSS_SELECTOR,'a[class="sc-27518a44-4 kVoakD productLink"]').get_attribute('href')
            except:
                self.logger.critical('Erros ao buscar o link do  produto')
            
            # Aqui sera feita a logica para filtrar o preco . 

            try:
                preco_numerico = int(preco.replace('.','').replace(',',' ').split()[0])
                if self.preco_min and preco_numerico < self.preco_min:
                    continue
                if self.preco_max and preco_numerico > self.preco_max:
                    continue
                dict_prod['Loja']='Kabum'
                dict_prod['Nome']=title
                dict_prod['Preco']=preco.replace(',','').split()[0]
                dict_prod['Link']=link
                if dict_prod not in lista_prod:
                    lista_prod.append(dict_prod.copy())
            except:
                self.logger.error(f'Um ou mais atributos do produtos nao foram encontrados.')

        df = pd.DataFrame(lista_prod) 
        df.to_csv('data_prod/produtos_kabum.csv',index=False)

        self.logger.info(f'{len(lista_prod)} Produtos cadastrados com sucesso')




if __name__ == "__main__":
    KabumScraping(produto='Placa de Video',preco_max=3000,preco_min=1000)






