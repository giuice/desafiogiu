import pytest
from website import Website

@pytest.fixture
def website():
    return Website('EpocaCosmeticos','https://www.epocacosmeticos.com.br',r'https://www\.epocacosmeticos\.com\.br/.+',r'^https://www.epocacosmeticos.com.br/.+/p$','title')

def test_website_isTargetPage(website):
    isTarget = website.isTargetPage('https://www.epocacosmeticos.com.br/pink-ice-eau-de-parfum-omerta-perfume-feminino/p')
    assert isTarget == True

def test_website_isNotTargetPage(website):
    isTarget = website.isTargetPage('https://www.epocacosmeticos.com.br/cabelos')
    assert isTarget == False

def test_website_hastagSelector_title(website):
    assert website.titleSelector == 'title'
