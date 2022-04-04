from pylenium.driver import Pylenium
import time


def test_g5_local_access_with_pw(py: Pylenium):
    py.visit('https://169.254.1.1')
    #click "advanced"
    # time.sleep(5)
    py.get('#details-button').click()
    # time.sleep(5)

    # click "proceed to 169.254.1.1(unsafe)"
    py.get('#proceed-link').click()
    # time.sleep(5)

    # login
    local_access_pw = 'admin' #todo: figure out a way to abstract the credentials from this file
    py.get('#password').type(local_access_pw)
    # time.sleep(5)
    py.get('[class="btn btn-primary"]').submit()
    # time.sleep(5)

    # assert login successful
    assert py.getx('/html/body/app-root/content-layout/div/div/clr-main-container/div/main/device')
    # time.sleep(5)
