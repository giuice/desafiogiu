import re


class Website:

    def __init__(
            self,
            name,
            url,
            internalLinkPattern,
            targetPattern,
            titleSelector
    ):
        self.name = name
        self.url = url
        # r'https://www\.epocacosmeticos\.com\.br/.+')
        self.internalLinkPattern = internalLinkPattern
        # r'^https://www.epocacosmeticos.com.br/.+/p$'
        self.targetPattern = targetPattern
        self.titleSelector = titleSelector

    def isTargetPage(self, pageUrl):
        if re.search(self.targetPattern, pageUrl):
            return True
        return False
