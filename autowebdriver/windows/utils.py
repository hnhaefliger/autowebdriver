import platform
import os
import subprocess

def getAppVersion(app):
    '''
    Get the version of an app that is installed on windows
    '''
    version = subprocess.Popen(['powershell', '-command', '(Get-Item ' + app + ').VersionInfo'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
    version = version.decode('utf-8')
    version = version.split('"')[1]
    return version

def findBrowsers():
    '''
    List browsers and versions installed on a windows operating system

    There has to be a better way to do this but windows is a pain
    '''
    supported = ['Google Chrome', 'Firefox', 'Edge', 'Opera', 'Internet Explorer']
    browsers = []

    apps = os.listdir('C:\Program Files')
    x86_apps = os.listdir('C:\Program Files (x86)')

    if 'Google' in apps:
        if 'Chrome' in os.listdir('C:\Program Files\Google'):
            supported.append(['Google Chrome', getAppVersion('C:\Program Files\Google\chrome.exe')])

    elif 'Google' in apps:
        if 'Chrome' in os.listdir('C:\Program Files (x86)\Google'):
            supported.append(['Google Chrome', getAppVersion('C:\Program Files (x86)\Google\chrome.exe')])

    if 'Internet Explorer' in apps:
        if 'something' in os.listdir('C:\Program Files\Internet Explorer'):
            supported.append(['Google Chrome', getAppVersion('C:\Program Files\Google\chrome.exe')])

    elif 'Internet Explorer' in apps:
        if 'something' in os.listdir('C:\Program Files (x86)\Internet Explorer'):
            supported.append(['Google Chrome', getAppVersion('C:\Program Files (x86)\Google\chrome.exe')])

    if 'Google' in apps:
        if 'Chrome' in os.listdir('C:\Program Files\Google'):
            supported.append(['Google Chrome', getAppVersion('C:\Program Files\Google\chrome.exe')])

    elif 'Google' in apps:
        if 'Chrome' in os.listdir('C:\Program Files (x86)\Google'):
            supported.append(['Google Chrome', getAppVersion('C:\Program Files (x86)\Google\chrome.exe')])

    if 'Google' in apps:
        if 'Chrome' in os.listdir('C:\Program Files\Google'):
            supported.append(['Google Chrome', getAppVersion('C:\Program Files\Google\chrome.exe')])

    elif 'Google' in apps:
        if 'Chrome' in os.listdir('C:\Program Files (x86)\Google'):
            supported.append(['Google Chrome', getAppVersion('C:\Program Files (x86)\Google\chrome.exe')])
    
    browsers = []
    
    return browsers
