from helpers.base_component import BaseComponent


class AddLink(BaseComponent):

    selectors = {
        'self': '.extras__share',
        'button': '.extras__share',
        'new_link': '.share__popupUrlInput'
    }

    def giveLink(self):
        self.driver.find_element_by_css_selector(self.selectors['button']).click()
        return (self.driver.find_element_by_css_selector(self.selectors['new_link']) != None)
