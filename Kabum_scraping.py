from utils import *
from utils import set_settings 

   


class KabumScraping:
    def __init__(self,produto,preco_max=None,preco_min=None):
        self.settings = set_settings(url="https://www.kabum.com.br/",loja_nome='kabum',)
        
        self.produto = produto
        self.preco_max = preco_max
        self.preco_min = preco_min

        self.browser = self.settings.OpenBrowser()
        self.logger = self.settings.setup_logger()
    

if __name__ == "__main__":
    KabumScraping(produto='Placa de Video')






