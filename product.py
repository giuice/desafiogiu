from website import Website
from productItem import ProductItem
import csv


class Product(Website):

    def __init__(
            self,
            name,
            url,
            internalLinkPattern,
            targetPattern,
            titleSelector,
            priceSelector):

        Website.__init__(
            self,
            name,
            url,
            internalLinkPattern,
            targetPattern,
            titleSelector)
        self.products = []
        self.termsToExclude = []
        self.priceSelector = priceSelector

    def hasProductItem(self, product):
        return product in self.products

    def addProduct(
            self,
            name,
            price,
            pageUrl):
        product = ProductItem(name, price, pageUrl)
        if product not in self.products:
            self.products.append(product)

    def addProductItem(self, productItem):
        if productItem not in self.products:
            self.products.append(productItem)

    def addTermToExclude(self, termToExclude):
        if termToExclude not in self.termsToExclude:
            self.termsToExclude.append(termToExclude)

    def isAllowedUrl(self, url):
        return not any(term in url for term in self.termsToExclude)

    def saveProductItem(self, productItem):
        file = open('logs/{}.csv'.format(self.name), 'a')
        try:
            writer = csv.writer(file)
            writer.writerow((productItem.name, productItem.price,
                             productItem.url))
        finally:
            file.close()
