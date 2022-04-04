from pylenium.driver import Pylenium
import time


def test_g5_local_access_no_pw(py: Pylenium):
    py.visit('https://169.254.1.1')
    #click "advanced"
    # py.get('#details-button').click()
    # time.sleep(1)

    # click "proceed to 169.254.1.1(unsafe)"
    # py.get('#proceed-link').click()
    # time.sleep(2)

    # assert login successful
    assert py.getx('/html/body/app-root/content-layout/div/div/clr-main-container/div/main/device')
    # time.sleep(5)

