class Page():
    def __init__(self, driver):

        self.driver = driver
        self._search_bar = None
        self._search_result = None
        self._search_route = None
        self._route_result = None
        self._add_link = None

    @property
    def search_bar(self):
        from helpers.search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def search_route(self):
        from helpers.search_route import SearchRoute

        if self._search_route is None:
            self._search_route = SearchRoute(self.driver, self.driver.find_element_by_css_selector(SearchRoute.selectors['self']))
        return self._search_route

    @property
    def route_result(self):
        from helpers.route_result import RouteResult

        if self._route_result is None:
            self._route_result = RouteResult(self.driver, self.driver.find_element_by_css_selector(RouteResult.selectors['self']))
        return self._route_result

    @property
    def add_link(self):
        from helpers.add_link import AddLink

        if self._add_link is None:
            self._add_link = AddLink(self.driver, self.driver.find_element_by_css_selector(AddLink.selectors['self']))
        return self._add_link

    @property
    def search_result(self):
        from helpers.search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver, self.driver.find_element_by_css_selector(SearchResult.selectors['self']))
        return self._search_result

    def open(self, url):
        self.driver.get(url)

