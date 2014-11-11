from base_component import BaseComponent
class MaterialList(BaseComponent):
    selectors = {
        'all_material': '#searchContent > div > div.menu-left-light.menu-dark.helper-up-down > ul > li:nth-child(2) > a',
        'all_levels':'#content > div.search-from.hidden > div.filter-level > a',
        }
    def choose(self):
        self.driver.find_element_by_css_selector(self.selectors['all_material']).click()
        self.driver.find_element_by_css_selector(self.selectors['all_levels']).click()
