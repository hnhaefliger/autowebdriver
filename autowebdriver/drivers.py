from . import linux
from . import macos
from . import windows
import platform

def getOS():
    os_name = platform.system()

    if os_name == 'Darwin':
        return 'macos'

    if os_name == 'Windows':
        return 'windows'

    if os_name == 'Linux':
        return 'linux'

def findBrowsers(os_name):
    supported = ['Google Chrome', 'Firefox', 'Edge', 'Internet Explorer', 'Opera', 'Safari']
    browsers = []
    
    if os_name == 'macos':
        return macos.findBrowsers()

    if os_name == 'Windows':
        return windows.findBrowsers()

    if os_name == 'Linux':
        return linux.findBrowsers()

    else:
        raise ValueError('Invalid operating system name')

def getDriver(driver):
    pass
