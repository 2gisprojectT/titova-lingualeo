
from base_component import BaseComponent

class SearchForm(BaseComponent):
    selectors = {
        'input': '#content > div.search-from.hidden > div.text-search-container.ovh.p-rel > div.input.text > input',
        'button':'#content > div.search-from.hidden > div.text-search-container.ovh.p-rel > div.input.text > a.btn-run-search',
        'no_results': '#searchResults > div.search-content > div.ovh.search-result-inner > div > b',
        'h-ref_drop': '#searchResults > div.search-content > div.ovh.search-result-inner > div > a'
        }

    def search(self, request):
        self.driver.find_element_by_css_selector(self.selectors['input']).click()
        self.driver.find_element_by_css_selector(self.selectors['input']).clear()
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(request)
        self.driver.find_element_by_css_selector(self.selectors['button']).click()

    def drop_filter (self, request1):
        self.driver.find_element_by_css_selector(self.selectors['input']).click()
        self.driver.find_element_by_css_selector(self.selectors['input']).clear()
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(request1)
        self.driver.find_element_by_css_selector(self.selectors['button']).click()
        if (self.driver.find_element_by_css_selector(self.selectors['no_results']).is_displayed()):
            return self.driver.find_element_by_css_selector(self.selectors['h-ref_drop']).click()


