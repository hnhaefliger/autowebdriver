import requests
import warnings
import json

def getURL(version, os, bits):
    '''
    Get the download url for a specified version of Google Chrome and OS.

    The driver version can be queried using google's LATEST_RELEASE API.
    '''
    
    version = int(version.split('.')[0])
    
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_' + str(version) # chrome LATEST_RELEASE API

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        data = requests.get(url, verify=False)
        data = data.content.decode('utf-8')

    if 'Error' in data: # LATEST_RELEASE will return error if there is no driver for the chrome version
        raise ValueError('Invalid Chrome version')

    if os == 'Windows':
        file = 'chromedriver_win32.zip' # there is no 64-bit windows chromedriver version

    elif os == 'Linux':
        file = 'chromedriver_linux64.zip'

    elif os == 'Darwin': # still need to differentiate between M1 and x86 macos
        file = 'chromedriver_mac64.zip'

    else:
        raise OSError('Invalid operating system name')

    url = 'https://chromedriver.storage.googleapis.com/index.html?path=' + data + '/' + file

    return url
