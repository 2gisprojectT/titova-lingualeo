from base_component import BaseComponent
class ChooseLevel(BaseComponent):
    selectors = {
        'self': '#content > div.search-from.hidden > div.filter-level > ul',
        'all_levels':'#content > div.search-from.hidden > div.filter-level > a',
        'simple_level': '#content > div.search-from.hidden > div.filter-level > ul > li.active > a',
        'middle_level':'#content > div.search-from.hidden > div.filter-level > ul > li:nth-child(3) > a',
        'hard_level':'#content > div.search-from.hidden > div.filter-level > ul > li:nth-child(4) > a',
        'simple_middle':'#content > div.search-from.hidden > div.filter-level > ul > li:nth-child(5) > a',
        'middle_hard':'#content > div.search-from.hidden > div.filter-level > ul > li:nth-child(6) > a'
        }
    def choose(self):
        self.driver.find_element_by_css_selector(self.selectors['self']).is_displayed()
        self.driver.find_element_by_css_selector(self.selectors['middle_level']).click()