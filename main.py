from crawler import Crawler
from product import Product


def main():

    product = Product('EpocaCosmeticos', 'https://www.epocacosmeticos.com.br', r'https://www\.epocacosmeticos\.com\.br/.+',
                      r'^https://www.epocacosmeticos.com.br/.+/p$', 'meta[property="og:title"]', '.skuBestPrice')
    crawler = Crawler(product,1000)
    crawler.crawl('https://www.epocacosmeticos.com.br');


if __name__ == '__main__':
    main()
