import os
from datetime import datetime


def take_screenshot(page, test_name):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    page.screenshot(path=f"screenshots/{test_name}_{timestamp}.png")