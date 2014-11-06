from helpers.base_component import BaseComponent

class SearchRoute(BaseComponent):

    selectors = {
        'self': '.searchBar__tab.searchBar__rsTab',
        'point_1': '//*[@id="module-1-1-2"]/div/input',
        'point_2': '//*[@id="module-1-1-3"]/div/input',
        'submit': '.searchBar__submit._rs'
    }


    def search(self, step1, step2):
        self.driver.find_element_by_css_selector(self.selectors['self']).click()
        self.driver.find_element_by_xpath(self.selectors['point_1']).send_keys(step1)
        self.driver.find_element_by_xpath(self.selectors['point_2']).send_keys(step2)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()
