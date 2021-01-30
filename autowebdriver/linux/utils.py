import platform
import os
import subprocess

def getAppVersion(app):
    '''
    Get the version of an app that is installed on linux
    '''
    version = subprocess.Popen([app, '--version'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
    version = version.decode('utf-8')
    version = version.replace('\n', '')

    while True:
        if version[-1] == ' ':
            version = version[:-1]
        else:
            break

    version = version.split(' ')[-1]
    
    return version

def findBrowsers():
    '''
    List browsers and versions installed on a linux-based operating system
    '''
    supported = ['Google Chrome', 'Firefox', 'Opera']
    browsers = []

    try:
        subprocess.Popen(['google-chrome', '--version'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
        browsers.append(['Google Chrome', getAppVersion('google-chrome'), 64])

    except: pass

    try:
        subprocess.Popen(['firefox', '--version'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
        browsers.append(['Firefox', getAppVersion('firefox'), 64])

    except: pass

    try:
        subprocess.Popen(['opera', '--version'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
        browsers.append(['Opera', getAppVersion('opera'), 64])

    except: pass

    return browsers
