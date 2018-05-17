import pytest
from product import Product
from productItem import ProductItem
import csv
import os


@pytest.fixture(scope='session')
def product():
    return Product('EpocaCosmeticos',
                   'https://www.epocacosmeticos.com.br',
                   r'https://www\.epocacosmeticos\.com\.br/.+',
                   r'^https://www.epocacosmeticos.com.br/.+/p$',
                   'meta[property="og:title"]',
                   '.skuBestPrice')


@pytest.fixture(scope='session')
def productItem(product):
    item = ProductItem('teste', '35,00', 'http://www.teste.com')
    product.addProductItem(item)
    return item


@pytest.fixture(scope='session')
def csv_file_name(product, productItem):
    product.saveProductItem(productItem)
    fname = 'logs/{}.csv'.format(product.name)
    yield fname
    try:
        os.remove(fname)
    except OSError:
        pass


def read_data(file):
    with open(file, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data


def test_product_hasProductItem(product, productItem):
    assert product.hasProductItem(productItem)


def test_product_productAdded(product, productItem):
    assert productItem in product.products


def test_add_new_product(product):
    name = 'teste2'
    price = '20,00'
    url = 'www.c.com'
    product.addProduct(name, price, url)
    productItem = ProductItem(name, price, url)
    size = len(product.products)
    p = product.products[size-1]
    assert productItem in product.products
    assert p.name == name
    assert p.price == price
    assert p.url == url
    assert productItem in product.products


def test_add_new_productItem(product):
    name = 'teste3'
    price = '20,50'
    url = 'www.c.com'
    productItem = ProductItem(name, price, url)
    product.addProductItem(productItem)
    size = len(product.products)
    p = product.products[size-1]
    assert productItem in product.products
    assert p.name == name
    assert p.price == price
    assert p.url == url


def test_check_priceSelector(product):
    assert product.priceSelector == '.skuBestPrice'


def test_check_titleSelector(product):
    assert product.titleSelector == 'meta[property="og:title"]'


def test_product_saveProductItem(product, productItem, csv_file_name):
    assert os.path.isfile(csv_file_name)


def test_productsList_is_greather_than_zero(product):
    assert len(product.products) > 0

def test_add_termToExclude(product):
    term = 'PS=16'
    product.addTermToExclude(term)
    assert len(product.termsToExclude) > 0
    assert product.termsToExclude[0] == term


def test_if_url_is_allowed_to_scan(product):
    term = 'PS=16'
    product.addTermToExclude(term)
    url = 'https://www.epocacosmeticos.com.br/perfumes/perfume-feminino/'
    assert product.isAllowedUrl(url) == True

def test_if_url_is_not_allowed_to_scan(product):
    term = 'PS=16'
    product.addTermToExclude(term)
    url = 'https://www.epocacosmeticos.com.br/perfumes/perfume-feminino/agatha-ruiz-de-la-prada/Amadeirado?PS=16&map=c,c,b,specificationFilter_7'
    assert product.isAllowedUrl(url) == False


def test_if_is_not_allowed_multiple_terms(product):
    product.addTermToExclude('PS=16')
    product.addTermToExclude('/checkout/')
    url = 'https://www.epocacosmeticos.com.br/perfumes/perfume-feminino/agatha-ruiz-de-la-prada/Amadeirado?PS=16&map=c,c,b,specificationFilter_7'
    assert not product.isAllowedUrl(url)
    url =  'https://www.epocacosmeticos.com.br/checkout/#/cart'
    assert not product.isAllowedUrl(url)