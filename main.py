from mercado_livre_scraping import MercadoLivre
from Kabum_scraping import KabumScraping
from multiprocessing import Process
from multiprocessing import Pool

from utils import pd
import os

# aqui vamos manipular os scraping feitos nos ecommerce

class FindProd:

    def __init__(self,produto,preco_max=None,preco_min=None):
        self.produto = produto
        self.preco_max = preco_max
        self.preco_min = preco_min

        self.df = pd.DataFrame()
        self._file_prod_kabum = 'data_prod/produtos_kabum.csv'
        self._file_prod_mercado_livre = 'data_prod/Produtos_mercado_livre.csv'
        self._worker_executor()

    def executar_kabum(self):
        scraper = KabumScraping(produto=self.produto,preco_min=self.preco_min,preco_max=self.preco_max)
        scraper.run_scraping_kabum()

    def executar_mercado_livre(self):
        scraper = MercadoLivre(produto=self.produto,preco_min=self.preco_min,preco_max=self.preco_max)
        scraper.run_scraping_mercado_livre()

    def _worker_executor(self):
        process_01 =Process(target=self.executar_kabum)
        process_02 =Process(target=self.executar_mercado_livre)
        
        process_01.start()
        process_02.start()

        process_01.join()
        self.__manipular_data()
        process_02.join()
        self.__manipular_data()

    def __manipular_data(self):
        list_files = []

        if os.path.exists(self._file_prod_kabum):
            file_kabum = pd.read_csv(self._file_prod_kabum)
            list_files.append(file_kabum)

        if os.path.exists(self._file_prod_mercado_livre):
            file_mercado_livre = pd.read_csv(self._file_prod_mercado_livre)
            list_files.append(file_mercado_livre)

        if len(list_files) >1 :
            df = pd.concat(list_files,ignore_index=True)
        else:
            df = pd.DataFrame(list_files[0])

        self.df = df
        self.df.to_csv('data_prod/Produtos_raspados.csv')

if __name__ == "__main__":
    nome_produto = 'Placa de video '
    FindProd(produto=nome_produto)


