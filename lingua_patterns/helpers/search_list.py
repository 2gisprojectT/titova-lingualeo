from base_component import BaseComponent

class SearchList(BaseComponent):
    selectors = {
       'self': '#searchResults > div.search-content > div.ovh.search-result-inner > div:nth-child(1) > div.left > h3',
       'link': '#searchResults > div.search-content > div.ovh.search-result-inner > div:nth-child(1) > div.left > h3 > a',
        }
    def show(self):
       return self.driver.find_element_by_css_selector(self.selectors['link']).is_displayed()


