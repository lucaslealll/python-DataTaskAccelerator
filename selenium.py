"""
dta.selenium
~~~~~~~~~~~~
"""

import glob
import pickle


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
