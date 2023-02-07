from pylenium.driver import Pylenium
from selenium.webdriver.common.keys import Keys


def test_bing(py: Pylenium):
    py.visit('https://bing.com')
    py.get('[name="q"]').type('puppies', Keys.ENTER)
    # py.get('[name="btnk"]').submit()
    assert py.should().contain_title('puppies')
