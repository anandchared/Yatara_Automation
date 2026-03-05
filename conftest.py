import pytest
from playwright.sync_api import sync_playwright
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
@pytest.fixture(scope="session")
def page(request):
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context()
    page = context.new_page()

    yield page

    browser.close()
    playwright.stop()


# Hook for screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            page.screenshot(
                path=f"screenshots/{item.name}_{timestamp}.png"
            )