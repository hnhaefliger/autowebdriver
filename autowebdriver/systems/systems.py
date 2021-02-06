from . import windows
from . import macos
from . import linux
import platform
import sys

def getBrowsers(operating_system, bits):
    if operating_system == 'Darwin':
        browsers = macos.getBrowsers()

    elif operating_system == 'Windows':
        browsers = windows.getBrowsers()

    elif operating_system == 'Linux':
        browsers = linux.getBrowsers()

    else:
        raise OSError('Unsupported operating system')

    return browsers

def info():
    return platform.system(), sys.maxsize
