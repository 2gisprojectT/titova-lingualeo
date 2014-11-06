#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from helpers.page import Page

class SeleniumTest(TestCase):

    def test_shareLink(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        page.open("http://2gis.ru")
        page.search_bar.search(u'кинортеатры')
        Newlink = page.add_link.giveLink()
        page.open(Newlink)
        assert Newlink is not None
        driver.close()
    # Find Way
    def test_FindRoute(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        page.open("http://2gis.ru")
        step_1 = u'Площадь Ленина'
        step_2 = u'Березовая роща'
        page.search_route.search(step_1, step_2)
        assert page.route_result.is_displayed is not None
        driver.close()

if __name__ == '__main__':
    unittest.main()
