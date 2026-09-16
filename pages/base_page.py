from playwright.sync_api import Page


class BasePage:
    base_url = 'http://testshop.qa-practice.com/'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url is not None:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator: str):
        return self.page.locator(locator)
