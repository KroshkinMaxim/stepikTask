import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    assert browser.find_element_by_xpath("//*[@id='add_to_basket_form']/button").is_displayed()