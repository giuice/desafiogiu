from crawler import Crawler
from product import Product
from bs4 import BeautifulSoup
import pytest
from urllib.parse import quote
import re


@pytest.fixture
def crawler():
    product = Product('EpocaCosmeticos', 'https://www.epocacosmeticos.com.br', r'https://www\.epocacosmeticos\.com\.br/.+',
                      r'^https://www.epocacosmeticos.com.br/.+/p$', 'meta[property="og:title"]', '.skuBestPrice')
    return Crawler(product)


def test_getPageSoup_is_not_none(crawler):
    bs = crawler.getPageSoup('https://www.epocacosmeticos.com.br')
    assert bs is not None


def test_getPageSoup_is_none(crawler):
    bs = crawler.getPageSoup('https://www.asdfasfafafd.com.br')
    assert bs is None


def test_getSafeLink_is_consistent(crawler):
    urlwithspecialchar = 'https://www.epocacosmeticos.com.br/perfumes/perfume-masculino/abercrombie---fitch/Aromático?PS=16&map=c,c,b,specificationFilter_7'
    assert crawler.makeSafeLink(
        urlwithspecialchar) == 'https://www.epocacosmeticos.com.br/perfumes/perfume-masculino/abercrombie---fitch/Arom%C3%A1tico?PS=16&map=c,c,b,specificationFilter_7'


def test_special_char_links_not_raise_error(crawler):
    urlwithspecialchar = 'https://www.epocacosmeticos.com.br/perfumes/perfume-masculino/abercrombie---fitch/Aromático?PS=16&map=c,c,b,specificationFilter_7'
    bs = crawler.getPageSoup(urlwithspecialchar)
    assert bs is not None


def test_getSelector_is_perfume_masculino(crawler):
    urlwithspecialchar = 'https://www.epocacosmeticos.com.br/perfumes/perfume-masculino/abercrombie---fitch/Aromático?PS=16&map=c,c,b,specificationFilter_7'
    bs = crawler.getPageSoup(urlwithspecialchar)
    title = crawler.getSelector(bs, '.titulo-sessao')
    assert title[0:17] == 'Perfume Masculino'


def test_getSelector_name_product_page(crawler):
    url = 'https://www.epocacosmeticos.com.br/pink-ice-eau-de-parfum-omerta-perfume-feminino/p'
    bs = crawler.getPageSoup(url)
    assert crawler.getSelector(
        bs, 'meta[property="og:title"]') == 'Pink Ice Omerta - Perfume Feminino - Eau de Parfum - 100ml'


def test_getSelector_price_product_page(crawler):
    url = 'https://www.epocacosmeticos.com.br/pink-ice-eau-de-parfum-omerta-perfume-feminino/p'
    bs = crawler.getPageSoup(url)
    assert crawler.getSelector(bs, '.skuBestPrice') == 'R$ 47,90'

def test_is_product_page_recognized_as_internal_link_pattern(crawler):
    p = re.compile(r'https://www\.epocacosmeticos\.com\.br/.+')
    assert p.match('https://www.epocacosmeticos.com.br/pink-ice-eau-de-parfum-omerta-perfume-feminino/p')


