import requests
import json
import warnings

def getDriverURL(browser, version, os, bits):
    if browser == 'Google Chrome':
        return getChromedriverURL(version, os, bits)

    elif browser == 'Safari':
        return None # safari selenium support is built-in

    elif browser == 'Edge':
        return getEdgedriverURL(version, os, bits)

    elif browser == 'Internet Explorer':
        return getIEdriverURL(version, os, bits)

    elif browser == 'Opera':
        return getOperadriverURL(version, os, bits)

    elif browser == 'Firefox':
        return getFirefoxdriverURL(version, os, bits)

    else: return ''

def getChromedriverURL(version, os, bits):
    '''
    Get the download url for a specified version of Google Chrome and OS.

    The driver version can be queried using google's LATEST_RELEASE_ API.
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

    elif os == 'Darwin': # need to differentiate between M1 and x86 macos
        file = 'chromedriver_mac64.zip'

    else:
        raise OSError('Invalid operating system name')

    data = 'https://chromedriver.storage.googleapis.com/index.html?path=' + data + '/' + file

    return data

def getOperadriverURL(version, os, bits):
    '''
    Get the download url for a specified version of Opera browser and OS.

    Because the versioning system for the opera driver does not match the versioning system for opera, the matching versions are queried from the GitHub releases API.
    '''
    
    version = int(version.split('.')[0])

    if os == 'Windows':
        if bits == 32:
            file = 'operadriver_win32.zip'

        else:
            file = 'operadriver_win64.zip'

    elif os == 'Linux':
        file = 'operadriver_linux64.zip'

    elif os == 'Darwin': # need to differentiate between M1 and x86 macos
        file = 'operadriver_mac64.zip'

    else:
        raise OSError('Invalid operating system name')
    
    url = 'https://api.github.com/repos/operasoftware/operachromiumdriver/releases'

    with warnings.catch_warnings(): # documented macos issue with GitHub API ssl (https://github.com/guzzle/guzzle/issues/819)
        warnings.simplefilter("ignore")
        data = requests.get(url, verify=False)
        data = json.loads(data.content)

    for release in data:
        if 'Opera ' + str(version) in release['body'] or 'Opera Stable ' + str(version) in release['body']: # corresponding Opera browser version is in release description
            for asset in release['assets']:
                if file == asset['name']:
                    return asset['browser_download_url']

    raise ValueError('Invalid Opera version') # if no opera driver version was found

def getIEdriverURL(version, os, bits):
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

def getEdgedriverURL(version, os, bits):
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

def getFirefoxdriverURL(version, os, bits): # come back to this later
    url = 'https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html' # info on driver support
    version = int(version.split('.')[0])

    if os == 'Windows':
        if bits == 32:
            file = '-win32.zip'

        else:
            file = '-win64.zip'

    elif os == 'Linux':
        if bits == 32: # firefox is the only one that has linux 32
            file = '-linux32.tar.gz'
        else:
            file = '-linux64.tar.gz'

    elif os == 'Darwin': # need to differentiate between M1 and x86 macos
        file = '-macos.tar.gz'

    else:
        raise OSError('Invalid operating system name')

    with warnings.catch_warnings(): # documented macos issue with GitHub API ssl (https://github.com/guzzle/guzzle/issues/819)
        warnings.simplefilter("ignore")
        data = requests.get(url, verify=False)
        data = data.content.decode('utf-8')
        
    data = data.replace('\n', '')
    data = data.replace(' ', '')
    data = data.split('table>')[1][:-2]
    data = data.split('</thead>')[1]
    data = data.split('<tr>')[1:]
    data = [row.split('<td>')[1:] for row in data]

    for row in data:
        if version > int(row[2]):
            return 'https://github.com/mozilla/geckodriver/releases/download/v' + row[0] + '/geckodriver-v' + row[0] + file
    
    raise ValueError('Invalid Firefox version') # if no gecko driver version was found

print(getDriverURL('Google Chrome', '86.0.4240.111', 'Darwin', '64'))
print(getDriverURL('Opera', '72.0', 'Darwin', '64'))
print(getDriverURL('Edge', '75.0.139.20', 'Windows', '64'))
print(getDriverURL('Internet Explorer', '75.0.139.20', 'Windows', '64'))
print(getDriverURL('Firefox', '75.0.139.20', 'Darwin', '64'))
