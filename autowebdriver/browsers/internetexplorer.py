import requests
import warnings
import json

def getURL(version, os, bits):
    '''
    Get the download url for a specified version of Internet Explorer and OS.

    Selenium only supports version 11 and lists the most recent driver on their websites
    '''

    if os != 'Windows':
        raise OSError('Invalid operating system name')

    if version.split('.')[0] != '11':
        raise ValueError('Invalid Internet Explorer version') # selenium only compatible with IE 11
    
    url = 'https://www.selenium.dev/downloads/'

    with warnings.catch_warnings(): # documented macos issue with GitHub API ssl (https://github.com/guzzle/guzzle/issues/819)
        warnings.simplefilter("ignore")
        data = requests.get(url, verify=False)
        data = data.content.decode('utf-8')
        
    data = data.split('>' + str(bits) + ' bit Windows IE')[0]
    data = data.split('<a href=')[-1]
    
    return data
