"""
dta.selenium
~~~~~~~~~~~~
"""

import glob
import pickle

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def import_cookies(path, filename, webdriver_browser):
    """Import cookies to browser.

    Parameters
    ----------
    `path` : Full file path.
    `filename` : Full file_name or is prefix.
    `webdriver_browser` : Browser object

    Examples
    --------
    Implement cookie file to bypass login

    >>> importCookies("/home/computer/Desktop/", "cookieFile", driver)
    >>> importCookies("/home/computer/Desktop/", "cookieFile.pkl", driver)
    """
    try:
        for file in glob.glob(f"{path}*{filename}*"):
            pwd_file = str(file)
    except:
        return False
    file = pickle.load(open(f"{pwd_file}", "rb"))
    for cookie in file:
        webdriver_browser.add_cookie(cookie)
    return webdriver_browser


def get_number_of_elements(container):
    element = int(
        len(
            container.find_elements(
                By.CLASS_NAME,
                "tiktok-16r0vzi-DivCommentItemContainer",
            )
        )
    )
    return element
