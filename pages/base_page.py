class BasePage():
    def __init__(self, browser, url):
        self.url = url
        self.browser = browser

    def open(self):
        self.browser.get(self.url)