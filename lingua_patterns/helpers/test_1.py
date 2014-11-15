#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from page import Page

class SeleniumTest(TestCase):
    driver = None
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.base_url = "http://lingualeo.com/ru/jungle"
        cls.page = Page(cls.driver)
        cls.page.open(cls.base_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_Search_NotEmpty(self):
        page = self.page
        request = 'London'
        page.search_form.search(request)
        assert page.search_list.show() is not None

    def test_Search_Empty(self):
        page = self.page
        request1 = u'Черное море'
        page.search_form.search(request1)
        assert page.search_form.driver.find_element_by_css_selector(page.search_form.selectors['no_results']).is_displayed() is not None

    def test_Search_DropFilter(self):
        page = self.page
        request2 = 'nnnnnnnnnn'
        page.search_form.drop_filter(request2)
        assert page.search_form.driver.find_element_by_css_selector(page.search_form.selectors['h-ref_drop']).is_displayed() is True, "Ссылки - <сбросить фильтр> - нет на странице!"

    def test_Choose_material(self):
        page = self.page
        page.material_list.choose()
        assert page.choose_level.driver.find_element_by_css_selector(page.choose_level.selectors['self']).is_displayed()
        page.choose_level.choose()


if __name__ == '__main__':
    unittest.main()