from pylenium.driver import Pylenium
import time


def test_fwex_local_access(py: Pylenium):
    py.visit('https://169.254.1.1')
    #click "advanced"
    py.get('#details-button').click()
    # time.sleep(1)

    # click "proceed to 169.254.1.1(unsafe)"
    py.get('#proceed-link').click()
    # time.sleep(2)

    # assert login successful
    assert py.get('#menu0')
    # assert py.should().contain_url('https://169.254.1.1/#/common/device')
    # time.sleep(5)
