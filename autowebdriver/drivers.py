from . import linux
from . import macos
from . import windows
import platform



def getOS():
    '''
    Get the name of the current local operating system
    - Is this necessary?
    - Should this just be built into the findBrowsers function?
    '''
    
    os_name = platform.system()

    if os_name == 'Darwin':
        return 'macos'

    if os_name == 'Windows':
        return 'windows'

    if os_name == 'Linux':
        return 'linux'

def findBrowsers(os_name):
    '''
    Get a list of installed browsers based on the current operating system.
    
    Browsers officially supported by selenium [https://www.selenium.dev/documentation/en/webdriver/driver_requirements/]:
    - Google Chrome (windows/macos/linux) [https://chromedriver.storage.googleapis.com/index.html]
    - Mozilla Firefox (windows/macos/linux) [https://github.com/mozilla/geckodriver/releases]
    - Microsoft Edge (windows) [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/]
    - Internet Explorer (windows) [https://selenium-release.storage.googleapis.com/index.html]
    - Opera (windows/macos/linux) [https://github.com/operasoftware/operachromiumdriver/releases]
    - Safari (macos) [built-in]

    Safari support is built into the app but needs to be enabled manually in settings (admin) - I'll come back to this later.
    '''
    
    if os_name == 'macos':
        return macos.findBrowsers()

    if os_name == 'Windows':
        return windows.findBrowsers()

    if os_name == 'Linux':
        return linux.findBrowsers()

    else:
        raise ValueError('Invalid operating system name')

def getDriver(driver, version, os):
    '''
    Download browser driver.

    Download links:
    - Google Chrome (windows/macos/linux) [https://chromedriver.storage.googleapis.com/index.html]
    - Mozilla Firefox (windows/macos/linux) [https://github.com/mozilla/geckodriver/releases]
    - Microsoft Edge (windows) [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/]
    - Internet Explorer (windows) [https://selenium-release.storage.googleapis.com/index.html]
    - Opera (windows/macos/linux) [https://github.com/operasoftware/operachromiumdriver/releases]
    - Safari (macos) [built-in]

    Safari support is built into the app but needs to be enabled manually in settings (admin) - I'll come back to this later.
    '''
    
    pass
