from crawler import Crawler
from product import Product


def main():

    product = Product('EpocaCosmeticos', 'https://www.epocacosmeticos.com.br', r'https://www\.epocacosmeticos\.com\.br/.+',
                      r'^https://www.epocacosmeticos.com.br/.+/p$', 'meta[property="og:title"]', '.skuBestPrice')

    #product.addTermToExclude('?PS=')
    product.addTermToExclude('/checkout/')
    product.addTermToExclude('centralatendimento')
    crawler = Crawler(product)
    crawler.crawl('https://www.epocacosmeticos.com.br')


if __name__ == '__main__':
    main()
