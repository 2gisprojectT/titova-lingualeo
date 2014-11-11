class Page():
    def __init__(self, driver):
        self.driver = driver
        self._search_form = None
        self._search_list = None
        self._material_list = None
        self._choose_level = None
    @property
    def search_form(self):
        from search_form import SearchForm
        if self._search_form is None:
            self._search_form = SearchForm(self.driver)
        return self._search_form

    @property
    def search_list(self):
        from search_list import SearchList
        if self._search_list is None:
            self._search_list = SearchList(self.driver)
        return self._search_list
    @property
    def material_list(self):
        from material_list import MaterialList
        if self._material_list is None:
            self._material_list = MaterialList(self.driver)
        return self._material_list

    @property
    def choose_level(self):
        from choose_level import ChooseLevel
        if self._choose_level is None:
            self._choose_level = ChooseLevel(self.driver)
        return self._choose_level



    def open(self, url):
        self.driver.get(url)
