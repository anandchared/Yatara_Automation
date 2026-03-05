class BasePage:

    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url, wait_until="networkidle")

    def get_title(self):
        return self.page.title()

    def get_current_url(self):
        return self.page.url

    def get_all_links(self):
        return self.page.locator("a")