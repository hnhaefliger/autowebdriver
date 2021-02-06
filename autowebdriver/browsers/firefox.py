import requests
import warnings
import json

def getURL(version, os, bits):
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
