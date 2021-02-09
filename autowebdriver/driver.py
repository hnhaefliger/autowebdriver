import warnings
import os

from . import systems
from . import browsers
from . import downloads

def getdriver(path=None):
    '''
    Get the correct driver for a locally installed browser.
    
    Browsers officially supported by selenium [https://www.selenium.dev/documentation/en/webdriver/driver_requirements/]:
    - Google Chrome (windows/macos/linux) [https://chromedriver.storage.googleapis.com/index.html]
    - Mozilla Firefox (windows/macos/linux) [https://github.com/mozilla/geckodriver/releases]
    - Microsoft Edge (windows) [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/]
    - Internet Explorer (windows) [https://selenium-release.storage.googleapis.com/index.html]
    - Opera (windows/macos/linux) [https://github.com/operasoftware/operachromiumdriver/releases]
    - Safari (macos) [built-in]

    Safari support is built into the app but needs to be enabled manually in settings (admin) - I'll come back to this later.
    '''
    operating_system, bits = systems.info()

    browser = systems.getBrowsers(operating_system, bits)[0]

    

    url = browsers.getURL(browser[0], browser[1], operating_system, browser[2])

    if url == None:
        return 'Safari', None

    if path == None:
        slash = '/'
        if operating_system == 'Windows':
            slash = '\\'

        path = os.path.abspath(os.path.dirname(__file__)) + slash + 'drivers' + slash

    location = downloads.downloadAndExtract(url, path)
    
    return browser[0], location
