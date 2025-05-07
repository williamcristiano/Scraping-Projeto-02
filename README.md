
# MercadoLivre Scraping

Este projeto é uma implementação para realizar scraping no Mercado Livre, buscando produtos de acordo com o nome fornecido e possíveis filtros de preço mínimo e máximo. O script captura informações de produtos, como nome, preço e link, e as armazena em um arquivo CSV para análise posterior. 

## Funcionalidades

1. **Busca de produtos**: O script realiza a busca de um produto especificado e filtra os resultados de acordo com o preço mínimo e máximo, se fornecido.
2. **Armazenamento dos resultados**: Todos os produtos encontrados são armazenados em um arquivo CSV.
3. **Registro de erros e ações**: Utilização do `logging` para registrar eventos importantes durante a execução, incluindo erros e informações sobre a busca e produtos encontrados.
4. **Validação de preço**: Filtros de preço (mínimo e máximo) são aplicados aos resultados dos produtos, permitindo que o usuário limite os produtos conforme sua necessidade.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação usada para a implementação do projeto.
- **Selenium**: Biblioteca usada para automação de navegação web e interação com a página do Mercado Livre.
- **Pandas**: Usada para criar o DataFrame e salvar os resultados em um arquivo CSV.
- **Logging**: Para registrar eventos e erros durante a execução do código.

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/williamcristiano/Scraping-Projeto-02
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install selenium pandas
   ```

3. Baixe o [Chromedriver](https://sites.google.com/chromium.org/driver/) correspondente à versão do seu navegador e adicione ao PATH.

4. Execute o script:
   ```bash
   python mercado_livre_scraping.py
   ```

5. O script irá gerar um arquivo CSV contendo todos os produtos encontrados no Mercado Livre com as informações solicitadas.

## Estrutura do Código

- **`MercadoLivre`**: Classe principal do projeto. Contém métodos para:
  - Configuração do logger
  - Abertura do navegador e navegação até a página do Mercado Livre
  - Envio da pesquisa
  - Coleta dos produtos encontrados
  - Armazenamento dos dados em CSV

## Futuras Atualizações

Este projeto tem como objetivo expandir a lógica aplicada no Mercado Livre para diversos outros e-commerces. Algumas atualizações planejadas incluem:

1. **Suporte a múltiplos e-commerces**: Estender a lógica de scraping para incluir outros sites de e-commerce populares (Ex: Amazon, OLX, Submarino, etc.).
   
2. **Interface de usuário**: Criar uma interface gráfica para facilitar a configuração da pesquisa (nome do produto, preço máximo, preço mínimo, etc.) sem precisar editar o código diretamente.
   
3. **Maior controle de erros**: Melhorar o tratamento de exceções e falhas de rede para garantir que o scraping continue de maneira robusta mesmo em caso de problemas.
   
4. **Exportação para diferentes formatos**: Adicionar funcionalidades para exportar os dados coletados não apenas para CSV, mas também para outros formatos como Excel e JSON.

5. **Melhoria na filtragem de preços**: Implementar filtros mais avançados, como faixas de preço dinâmicas, baseado em uma análise preexistente dos produtos.

6. **Agendamento de Execuções**: Permitir que o scraping seja agendado para execução periódica, a fim de atualizar constantemente os dados coletados.

7. **Integração com APIs**: Integrar com APIs de preços de mercado para atualizar os dados de forma dinâmica.

8. **Análise de Dados**: Após a coleta, fornecer uma funcionalidade para análise de dados dos produtos (média de preços, comparação entre e-commerces, etc.).

## Licença

Este projeto é de código aberto e distribuído sob a licença MIT.
