# A Simple Crawler

Um crawler simples e generico para varrer sites e salvar o nome, preço e url dos produtos 

## Getting Started

Run the comand: python main.py ou
#### Crie um Produto
``` python
from crawler import Crawler
from product import Product

''' Adicione um site de produto, os parametros são
            nomedosite
            url,
            internalLinkPattern,
            targetPattern,
            titleSelector,
            priceSelector '''
product = Product('EpocaCosmeticos', 'https://www.epocacosmeticos.com.br', r'https://www\.epocacosmeticos\.com\.br/.+',
                      r'^https://www.epocacosmeticos.com.br/.+/p$', 'meta[property="og:title"]', '.skuBestPrice')

# Adicione filtros que deseja excluir das url varridas: obs neste exemplo estes filtros não irão varrer todo o site.
product.addTermToExclude('?PS=')
product.addTermToExclude('/checkout/')
product.addTermToExclude('centralatendimento')

# Finalmente crie o crawler
crawler = Crawler(product)
crawler.crawl('https://www.epocacosmeticos.com.br') 

```
Docker: 

## TODO:
+ Achar uma maneira genérica de ler os paginadores

### Algumas questões


+ Agora você tem de capturar dados de outros 100 sites. Quais seriam suas estratégias para escalar a aplicação?
> Acredito que modificar a aplicação para ser assíncrona seja a solução de escalabilidade, pode ser fazer isso usando uma biblioteca como o asyncio, o que vou tentar fazer na versão 2 do aplicativo. Nosso app permite instanciar vários sites
+ Alguns sites carregam o preço através de JavaScript. Como faria para capturar esse valor.
> Usar Selenium seria uma boa solução.
+ Alguns sites podem bloquear a captura por interpretar seus acessos como um ataque DDOS. Como lidaria com essa situação?
> Nesse caso temos que adotar várias soluções como time.sleep para que o scan não seja tão agressivo, gerar headers de página, randomicamente trocando o cliente a cada requisição tambêm acho ser uma boa ideia.
+ Um cliente liga reclamando que está fazendo muitos acessos ao seu site e aumentando seus custos com infra. Como resolveria esse problema?


## Running the tests

Just command line: 'python -m pytest'



## Authors

* **Giuliano Lemes** - *website* - [Giuice Creative Solutions](http://www.giuice.com)

