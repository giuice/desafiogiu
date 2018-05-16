from product import Product
from productItem import ProductItem
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse
from urllib.parse import quote
from urllib.error import HTTPError
from urllib.error import URLError
from socket import timeout
from random import choice
import ssl
import re
import time


class Crawler:
    ''' pageLimitToCrawl is for test porposes '''

    def __init__(self, site, pageLimitToCrawl=300):
        self.site = site
        self.pages = []
        self.pageLimitToCrawl = pageLimitToCrawl
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        self.pageCount = 0
       

    ''' Avoid errors in links with special chars '''

    def makeSafeLink(self, pageUrl):
        return quote(pageUrl, safe="%/:=&?~#+!$,;'@()*[]")

    def getPageSoup(self, pageUrl):
        try:
            pageUrl = self.makeSafeLink(pageUrl)
            html = urlopen(pageUrl, context=self.ctx)
            return BeautifulSoup(html, 'html.parser')
        except (HTTPError, URLError) as error:
            print('Data of %s not retrieved in %s\nURL: %s', error, pageUrl)
        except timeout:
            print('socket timed out - URL %s', pageUrl)
            # TODO : salvar links não visitados

    def getPageLinks(self, bs):
        return bs.find_all('a', href=re.compile(self.site.internalLinkPattern))

    def getSelector(self, pageObj, selector):
        selected = pageObj.select(selector)
        if selected is not None and len(selected) > 0:
            if selected[0].has_attr('content'):
                return selected[0].attrs['content']
            return " ".join([el.get_text() for el in selected])
        return ''

    def addItemData(self, bs, pageUrl):
        if(self.site.isTargetPage(pageUrl)):
            pname = self.getSelector(bs, 'meta[property="og:title"]')
            price = self.getSelector(bs, '.skuBestPrice')
            product = ProductItem(pname, price, pageUrl)
            if not self.site.hasProductItem(product):
                self.site.addProductItem(product)
                self.site.saveProductItem(product)

    def crawl(self, pageUrl):
        try:
            bs = self.getPageSoup(pageUrl)
            self.addItemData(bs, pageUrl)
            for link in bs.find_all('a',
                                    href=re.compile(
                                        self.
                                        site.
                                        internalLinkPattern)):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in self.pages:
                        if self.pageCount > self.pageLimitToCrawl:
                            return
                        self.pageCount += 1
                        newPage = link.attrs['href']
                        print('-'*20)
                        print(pageUrl)
                        print(newPage)
                        self.pages.append(newPage)
                        time.sleep(0.05)
                        self.crawl(newPage)
        except RecursionError as er:
            link = self.pages[-1]
            self.crawl(link)
