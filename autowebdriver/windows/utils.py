import platform
import os
import subprocess

def getAppVersion(app):
    '''
    Get the version of an app that is installed on windows
    '''
    version = subprocess.Popen(['powershell', '-windowstyle', 'hidden', '-command', '(Get-Item "' + app + '").VersionInfo'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
    version = version.decode('utf-8')
    version = version.split('\n')[3]
    version = version.split(' ')
    version = version[0]
    return version

def findBrowsers():
    '''
    List browsers and versions installed on a windows operating system

    There has to be a better way to do this but windows is a pain
    '''
    supported = ['Google Chrome', 'Firefox', 'Edge', 'Opera', 'Internet Explorer']
    browsers = []

    apps = os.listdir('C:\\Program Files')
    x86_apps = os.listdir('C:\\Program Files (x86)')

    if 'Google' in apps:
        if 'Chrome' in os.listdir('C:\\Program Files\\Google'):
            browsers.append(['Google Chrome', getAppVersion('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')])

    if 'Google' in x86_apps and not('Google Chrome' in [browser[0] for browser in browsers]):
        if 'Chrome' in os.listdir('C:\\Program Files (x86)\\Google'):
            browsers.append(['Google Chrome', getAppVersion('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')])

    if 'Mozilla Firefox' in apps:
        if 'firefox.exe' in os.listdir('C:\\Program Files\\Mozilla Firefox'):
            browsers.append(['Firefox', getAppVersion('C:\\Program Files\\Mozilla Firefox\\firefox.exe')])

    if 'Mozilla Firefox' in x86_apps and not('Firefox' in [browser[0] for browser in browsers]):
        if 'firefox.exe' in os.listdir('C:\\Program Files (x86)\\Mozilla Firefox'):
            browsers.append(['Firefox', getAppVersion('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')])

    if 'Microsoft' in apps:
        if 'Edge' in os.listdir('C:\\Program Files\\Microsoft'):
            browsers.append(['Edge', getAppVersion('C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe')])

    if 'Microsoft' in x86_apps and not('Edge' in [browser[0] for browser in browsers]):
        if 'Edge' in os.listdir('C:\\Program Files (x86)\\Microsoft'):
            browsers.append(['Edge', getAppVersion('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')])

    if 'Internet Explorer' in apps:
        if 'iexplore.exe' in os.listdir('C:\\Program Files\\Internet Explorer'):
            browsers.append(['Internet Explorer', getAppVersion('C:\\Program Files\\Internet Explorer\\iexplore.exe')])

    if 'Internet Explorer' in x86_apps and not('Internet Explorer' in [browser[0] for browser in browsers]):
        if 'iexplore.exe' in os.listdir('C:\\Program Files (x86)\\Internet Explorer'):
            browsers.append(['Internet Explorer', getAppVersion('C:\\Program Files (x86)\\Internet Explorer\\iexplore.exe')])
    
    return browsers
