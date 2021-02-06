import requests
import warnings
import json

def getURL(version, os, bits):
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
