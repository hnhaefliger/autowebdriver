import requests
import warnings
import json

def getURL(version):
    '''
    Get the download url for a specified version of Edge browser and OS.

    MS Edge versions match with the correct driver so we just need to check that the version is valid.
    '''
    
    if os == 'Windows':
        if bits == 32:
            file = 'edgedriver_win32.zip'

        else:
            file = 'edgedriver_win64.zip'

    else: # selenium only supports edge on windows
        raise OSError('Invalid operating system name')

    url = 'https://msedgedriver.azureedge.net/' + version + '/' + file
        
    with warnings.catch_warnings(): # documented macos issue with GitHub API ssl (https://github.com/guzzle/guzzle/issues/819)
        warnings.simplefilter("ignore")
        data = requests.get(url, stream=True, verify=False) # stream so that we don't load the whole file

        if data.status_code != 200:
            raise ValueError('Invalid Edge version') # if no edge driver version was found

    return url 
