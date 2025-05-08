from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import logging
import pandas as pd
from pathlib import Path
from selenium.webdriver.chrome.options import Options

class set_settings:
    def __init__(self,url,loja_nome):
        self.caminho_logs = Path(__file__).parent /"data_logs"
        self.nome_loja = loja_nome  
        self.URL = url

    def setup_logger(self)->logging:
        logging.basicConfig(filename=f'{self.caminho_logs}/log_erros_{self.nome_loja}.log',level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S')
        return logging.getLogger(__name__)
    
    def OpenBrowser(self)->webdriver.Chrome:
        options = Options()
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
        browser.get(self.URL)
        return browser 

if __name__=="__main__":
    pass