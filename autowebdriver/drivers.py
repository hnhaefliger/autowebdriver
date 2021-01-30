from . import linux
from . import macos
from . import windows
import requests
import platform
import sys

def getDriver():
    '''
    Get a list of installed browsers based on the current operating system and download matching drivers.
    
    Browsers officially supported by selenium [https://www.selenium.dev/documentation/en/webdriver/driver_requirements/]:
    - Google Chrome (windows/macos/linux) [https://chromedriver.storage.googleapis.com/index.html]
    - Mozilla Firefox (windows/macos/linux) [https://github.com/mozilla/geckodriver/releases]
    - Microsoft Edge (windows) [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/]
    - Internet Explorer (windows) [https://selenium-release.storage.googleapis.com/index.html]
    - Opera (windows/macos/linux) [https://github.com/operasoftware/operachromiumdriver/releases]
    - Safari (macos) [built-in]

    Safari support is built into the app but needs to be enabled manually in settings (admin) - I'll come back to this later.
    '''

    os_name = platform.system()
    bitness = sys.maxsize
    
    if os_name == 'Darwin':
        browsers =  macos.findBrowsers()

    elif os_name == 'Windows':
        browsers =  windows.findBrowsers()

    elif os_name == 'Linux':
        browsers =  linux.findBrowsers()

    else:
        raise OSError('Invalid operating system name')

    return browsers
