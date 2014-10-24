# =*- coding: utf-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumWDTest(TestCase):

    def test_FindSong (self):
        page = webdriver.Firefox()
        page.get("http://lingualeo.com/ru/jungle")
        assert u"Поиск видео, аудио и текстового материал на английском языке" in page.title
        elem = page.find_element_by_class_name("placeholder-light")
        elem.send_keys("Adele")
        elem.send_keys(Keys.RETURN)
        Song = page.find_element_by_css_selector("a[href='/ru/jungle/107226']").click()
        assert u"Поиск видео, аудио и текстового материал на английском языке" is not page.title



if __name__ == '__main__':
    unittest.main()