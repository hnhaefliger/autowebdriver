from . import chrome
from . import firefox
from . import edge
from . import opera
from . import safari
from . import internetexplorer
import warnings

def getURL(name, version, operating_system, bits):
    if name == 'Google Chrome':
        url = chrome.getURL(version, operating_system, bits)

    elif name == 'Firefox':
        url = firefox.getURL(version, operating_system, bits)

    elif name == 'Edge':
        url = edge.getURL(version, operating_system, bits)

    elif name == 'Internet Explorer':
        url = internetexplorer.getURL(version, operating_system, bits)

    elif name == 'Opera':
        url = opera.getURL(version, operating_system, bits)

    elif name == 'Safari':
        warnings.warn('Only Safari was found and needs to be set up manually')
        return None

    else:
        raise ValueError('Invalid browser')

    return url
