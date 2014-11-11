#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from page import Page

class SeleniumTest(TestCase):
    def test_Search_NotEmpty(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        page.open("http://lingualeo.com/ru/jungle")
        request = 'London'
        page.search_form.search(request)
        assert page.search_list.show() is not None
        driver.close()
    def test_Search_Empty(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        page.open("http://lingualeo.com/ru/jungle")
        request1 = u'Черное море'
        page.search_form.search(request1)
        assert page.search_form.driver.find_element_by_css_selector(page.search_form.selectors['no_results']).is_displayed() is not None
        driver.close()
    def test_Search_DropFilter(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        page.open("http://lingualeo.com/ru/jungle")
        request2 = 'nnnnnnnnnn'
        page.search_form.drop_filter(request2)
        assert page.search_form.driver.find_element_by_css_selector(page.search_form.selectors['h-ref_drop']).is_displayed() is True, "Ссылки - <сбросить фильтр> - нет на странице!"
        driver.close()
    def test_Choose_material(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        page = Page(driver)
        page.open("http://lingualeo.com/ru/jungle")
        page.material_list.choose()
        assert page.choose_level.driver.find_element_by_css_selector(page.choose_level.selectors['self']).is_displayed()
        page.choose_level.choose()

if __name__ == '__main__':
    unittest.main()